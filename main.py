import csv
import math
import random
import time

import matplotlib
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

from hospital import Hospital
from person import Person

matplotlib.use( 'tkagg' )

FILEWRITER = 0

POPDENSITY = 3  #KiloPX^2
NUMPERSONS = 3000

dimDensity = math.sqrt(NUMPERSONS/POPDENSITY)*1000

INFECTED_START = 0.03
DIVIDERRATIO = 4/5
XAXIS = math.ceil(dimDensity/DIVIDERRATIO)
YAXIS = dimDensity
# XAXIS = 6000
# YAXIS=4000
DIVIDERWIDTH = 4
DIVIDERLOC = XAXIS*DIVIDERRATIO+(DIVIDERWIDTH/2)
LEFTMIDDLE = DIVIDERLOC//2
RIGHTMIDDLE = DIVIDERLOC+(XAXIS-DIVIDERLOC)//2

BASEMOVEMENTRATIO = 5
BASEMOVEMENTSPEED = (dimDensity**2)/((4000*6000))*BASEMOVEMENTRATIO

DOTSIZE = 20#XAXIS*YAXIS//(NUMPERSONS**2)#
COLORS = ['g', 'gold', 'tab:orange', 'r', 'blue', 'k']
INFECTIONRAD = 100  #
HOMEKIT = False
SHOW = True
WRITE = True

allpersons = []
# positions = []
plots = []

notinfected = []
infected = []
recovered = []
dead = []

hospital = Hospital(XAXIS//2+DIVIDERWIDTH, XAXIS)



scatter, fig, outsideText, insideText, noninfText, infectedText, curedText, deadText = [None for i in range(8)]
'''
call everyone's step()
'''
# TODO check if this can be done more effitiently inside stepScene
    # it prolly can
def stepAll():
    for person in allpersons:
        person.step()
'''
Big boi step function that updates the chart
'''
def stepScene(headless=False):
    outsideCount=0
    insideCount=0
    deadCount=0

    positions = []
    colors = []

    notinfected.clear()
    infected.clear()
    recovered.clear()
    # dead.clear()

    # extract everyone's infection data and put People into lists
    for person in allpersons:
        person.step()

        infection = person.inf              # get infectiron status
        colors.append(COLORS[infection])    # set their color for the chart

        if person.shouldHospitalise() and hospital.available():
            person.toHospital()
            hospital.admit()
        elif person.shouldDischarge():
            person.leaveHospital()
            hospital.release()

        if person.place==0:
            outsideCount+=1
        else:
            insideCount+=1

        positions.append(person.pos)        # set their postion for chart
        if infection<4:                     # if not cured
            # if person.place == 0:         # if outside
            if person.inf==0:               # if !infected/healthy
                notinfected.append(person)
            else:                           # if any stage of infection & person is outside
                infected.append(person)     # this is to prevent people from infecting across hospital border
        elif infection == 4:
            recovered.append(person)
        elif infection == 5:                 #infection 5 - dead
            deadCount+=1

    if SHOW:   # Update charts
        scatter.set_color(colors)               # add color list to chart
        scatter.set_offsets(positions)          # add position list to chart
        insideText.set_text(str(insideCount))   # set number count
        outsideText.set_text(str(outsideCount))
        noninfText.set_text(str(len(notinfected)))
        infectedText.set_text(str(len(infected)))
        curedText.set_text(str(len(recovered)))
        deadText.set_text(deadCount)

    if WRITE:   #write to csv
        conf = len(infected)+len(recovered)+deadCount
        FILEWRITER.writerow({'uninfected':len(notinfected), 'infected':len(infected), 'cured':len(recovered), 'dead':deadCount, 'capacity':hospital.capacity, 'confirmed':conf})
        # {'emp_name': 'John Smith', 'dept': 'Accounting', 'birth_month': 'November'}

    # Collisons/coughs with infected people
    for inf in infected:
        for good in notinfected:
            if inf.distance(good)<inf.radius:# and inf.place==0:
                good.contract()

    if headless:
        return len(infected)+len(recovered)+deadCount


'''
Animate function use by matplotlib
'''
def anim(i):
    # stepAll()
    stepScene()

def spawn(numPersons, infectedStart, infectionProb=False, baseRadius=INFECTIONRAD, day=False, undiagDays=False, asymDays=False, symDays=False, baseMovementSpeed=False):
    # Spawn everyone
    infCount = 0
    for i in range(numPersons):
        infection = 1 if random.random() < infectedStart else 0
        newp = Person(infection, XAXIS, YAXIS, divider=DIVIDERLOC, homekit=HOMEKIT, size=DOTSIZE, baseRadius=baseRadius)
        newp.setExtraParams(infectionProb, day, undiagDays, asymDays, symDays, baseMovement=baseMovementSpeed)
        allpersons.append(newp)
        infCount+=infection
    return infCount

def run(iters=26, numPersons=1000, infectedStart=0.03, infectionProb=False, baseRadius=INFECTIONRAD, day=False, undiagDays=False, asymDays=False, symDays=False, hosp=False, baseMovementSpeed=False):
    global SHOW; global WRITE;
    SHOW= False
    WRITE=False

    global scatter; global fig; global outsideText; global insideText; global noninfText; global infectedText; global curedText; global deadText; global FILEWRITER;
    scatter, fig, outsideText, insideText, noninfText, infectedText, curedText, deadText = setupShow() if SHOW else [None for i in range(8)]
    FILEWRITER, rfile = setupWrite() if WRITE else [None, None]

    hospital.setCapacity(hosp)
    initInfection = spawn(numPersons, infectedStart, infectionProb, baseRadius, day, undiagDays, asymDays, symDays, baseMovementSpeed=baseMovementSpeed)

    cumulativeList = [initInfection]

    for i in range(iters-1):
        # stepAll()
        for j in range(day-1):
            stepScene(headless=False)
            # print("-", end="")
        thisstep = stepScene(headless=True)
        print(str(i) + ":" + str(thisstep), end=", ")
        cumulativeList.append(thisstep)
        if SHOW:
            plt.pause(0.05)
            plt.show()

    if WRITE:
        rfile.close()

    print()
    allpersons.clear()
    return cumulativeList

def oneDDistance(p1,q1):
    return (p1-q1)**2

def compare(realData, generatedData, persons=False):
    assert(len(realData) == len(generatedData))
    iters = len(realData)
    if persons:
        diffs = [oneDDistance(generatedData[i] , realData[i]*persons) for i in range(iters)]
    else:
        diffs = [oneDDistance(generatedData[i],realData[i]) for i in range(iters)]
    return sum(diffs)**(1/2)

def compareAuto(realData, numPersons=1000, infectedStart=0.03, infectionProb=False, baseradius=INFECTIONRAD, day=False, undiagDays=False, asymDays=False, symDays=False, hosp=False, baseMovementSpeed=False):
    iters = len(realData)
    generate = run(iters, numPersons, infectedStart, infectionProb, baseradius, day, undiagDays, asymDays, symDays, hosp, baseMovementSpeed=baseMovementSpeed)
    return generate,  compare(realData=realData, generatedData=generate, persons=numPersons)

def setupShow():
    sns.set_style("dark")
    # fig, (ax1, ax2) = plt.subplots(2)
    fig, ax1 = plt.subplots()

    ax1.set_xlim(0, XAXIS)  # xlim=(0, XAXIS), ylim=(0, YAXIS)
    ax1.set_ylim(0, YAXIS)
    # ax1.set_xticklabels([])
    # ax1.set_yticklabels([])
    ax1.axvline(DIVIDERLOC, linewidth=(DIVIDERWIDTH - 2), color='grey')
    ax1.text(LEFTMIDDLE, YAXIS+10, "Outside", fontsize=10, horizontalalignment='center')
    if HOMEKIT:
        ax1.text(RIGHTMIDDLE, YAXIS+10, "Home", fontsize=10, horizontalalignment='center')
    else:
        ax1.text(RIGHTMIDDLE, YAXIS+10, "Hospital", fontsize=10, horizontalalignment='center')
    outsideText = ax1.text(LEFTMIDDLE-100, -100, str(NUMPERSONS), fontsize=10, horizontalalignment='center')
    insideText = ax1.text(RIGHTMIDDLE, -100, "0", fontsize=10, horizontalalignment='center')

    noninfText = ax1.text(XAXIS//2-400, -200, "0", horizontalalignment='center', fontdict={'size':10, 'color':COLORS[0],
            'weight': 'bold',})
    infectedText = ax1.text(XAXIS//2-150, -200, "0", horizontalalignment='center', fontdict={'size':10, 'color':COLORS[3],
            'weight': 'bold',})
    curedText = ax1.text(XAXIS//2+150, -200, "0", horizontalalignment='center', fontdict={'size':10, 'color':COLORS[4],
            'weight': 'bold',})
    deadText = ax1.text(XAXIS//2+400, -200, "0", horizontalalignment='center', fontdict={'size':10, 'color':COLORS[5],
            'weight': 'bold',})

    sns.set()
    scatter = ax1.scatter([],[], s=DOTSIZE)
    sns.despine(left=True, bottom=True)
    return scatter, fig, outsideText, insideText, noninfText, infectedText, curedText, deadText

def setupWrite():       # write || Write&Show
    folder = "results/"
    simType = 'HOME_' if HOMEKIT else 'HOSPITAL_'
    resutsFileName = folder+simType + str(NUMPERSONS)+"_"+str(INFECTED_START)+"_"+str(int(time.time())//2)+'.csv'
    rfile = open(resutsFileName, mode='w', newline='')
    fieldnames = ['uninfected', 'infected', 'cured', 'dead', 'capacity', 'confirmed']
    fwriter = csv.DictWriter(rfile, delimiter=',', fieldnames=fieldnames)
    FILEWRITER = fwriter
    fwriter.writeheader()
    return FILEWRITER, rfile

def main():
    startpercentage = 0.0023562754370643774
    POPDENSITY = 3  # KiloPX^2

    numpersons = 3000

    BASEMOVEMENTRATIO = 5.4
    baseMovementSpeed = np.int((dimDensity ** 2) / (4000 * 6000) * BASEMOVEMENTRATIO)

    infectionStart = np.float(startpercentage)
    infectionProb = np.float(0.26)
    baseRadius = 72

    day = 12
    undiagDays = np.uint8(7 * day)
    asymDays = np.uint8(14 * day)
    symDays = np.uint8(15 * day)
    hosp = math.ceil(3.2 * (numpersons / 1000) * 1)

    initInfection = spawn(NUMPERSONS, infectionStart, infectionProb, baseRadius, day, undiagDays, asymDays, symDays,
                          baseMovementSpeed=baseMovementSpeed)
    # spawn(numPersons=NUMPERSONS, infectedStart=INFECTED_START, baseMovementSpeed=BASEMOVEMENTSPEED)
    print(("SHOW " if SHOW else "") + (" WRITE" if WRITE else ""))

    global scatter; global fig; global outsideText; global insideText; global noninfText; global infectedText; global curedText; global deadText; global FILEWRITER;
    scatter, fig, outsideText, insideText, noninfText, infectedText, curedText, deadText = setupShow() if SHOW else [None for i in range(8)]
    FILEWRITER, rfile = setupWrite() if WRITE else [None, None]

    if SHOW:  #Write&|Show
        ani = animation.FuncAnimation(fig, anim,  interval=1, frames=1, blit=False)
        plt.show()
    elif WRITE:
        while len(recovered)<1 or len(infected)>0:
            anim(0)
    if WRITE:
        rfile.close()

if __name__ == "__main__":
    main()

# next meeting
## hospital capacity - people die for lack of resources
## probabilistic behaviours for death & death



# presentation #
## Realted work
### mention where SIR model came from - Uses difffies

## Main ideas
### Expalin what youre trying to achve in the sim

## Figure 1
### 1 Really good figure 1

## Experiaentla result
### Explain what we did and why


## Find critucal population density point