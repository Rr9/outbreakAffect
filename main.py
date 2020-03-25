import random

import matplotlib
import seaborn as sns

matplotlib.use( 'tkagg' )
import matplotlib.animation as animation
import matplotlib.pyplot as plt

import csv
import time

from person import Person
from hospital import Hospital


NUMPERSONS = 1000
INFECTED_START = 0.03
XAXIS = 6000
YAXIS = 4000
DIVIDERWIDTH = 4
DIVIDERRATIO = 3/4
DIVIDERLOC = XAXIS*DIVIDERRATIO+(DIVIDERWIDTH/2)
LEFTMIDDLE = DIVIDERLOC//2
RIGHTMIDDLE = DIVIDERLOC+(XAXIS-DIVIDERLOC)//2

DOTSIZE = XAXIS*YAXIS//(NUMPERSONS*1000)#20
COLORS = ['g', 'gold', 'tab:orange', 'r', 'blue', 'k']
INFECTIONRAD = DOTSIZE  #
HOMEKIT = False
SHOW = False

allpersons = []
# positions = []
plots = []

notinfected = []
infected = []
recovered = []
dead = []

hospital = Hospital(XAXIS//2+DIVIDERWIDTH, XAXIS)



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
def stepScene():
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

    if SHOW:
    # Update charts
        scatter.set_color(colors)               # add color list to chart
        scatter.set_offsets(positions)          # add position list to chart
        insideText.set_text(str(insideCount))   # set number count
        outsideText.set_text(str(outsideCount))
        noninfText.set_text(str(len(notinfected)))
        infectedText.set_text(str(len(infected)))
        curedText.set_text(str(len(recovered)))
        deadText.set_text(deadCount)
    # TODO take len(uninfected), len(infected), len(recovered), len(dead)
    # TODO make graph from ^^^

    #write to csv
    fwriter.writerow({'uninfected':len(notinfected), 'infected':len(infected), 'cured':len(recovered), 'dead':deadCount, 'capacity':hospital.capacity})
    # {'emp_name': 'John Smith', 'dept': 'Accounting', 'birth_month': 'November'}

    # Collisons/coughs with infected people
    for inf in infected:
        for good in notinfected:
            if inf.distance(good)<inf.radius:# and inf.place==0:
                good.contract()

    #return scatter

'''
Animate function use by matplotlib
'''
def anim(i):
    stepAll()
    stepScene()


# Spawn everyone
for i in range(NUMPERSONS):
    infection = 1 if random.random() < INFECTED_START else 0
    allpersons.append(Person(infection, XAXIS, YAXIS, divider=DIVIDERLOC, homekit=HOMEKIT, size=DOTSIZE, baseRadius=INFECTIONRAD))

if SHOW:
    sns.set_style("dark")
    # fig, (ax1, ax2) = plt.subplots(2)
    fig, ax1 = plt.subplots()

    ax1.set_xlim(0, XAXIS)  # xlim=(0, XAXIS), ylim=(0, YAXIS)
    ax1.set_ylim(0, YAXIS)
    ax1.set_xticklabels([])
    ax1.set_yticklabels([])
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

folder = "results/"
simType = 'HOME_' if HOMEKIT else 'HOSPITAL_'
resutsFileName = folder+simType + str(NUMPERSONS)+"_"+str(INFECTED_START)+"_"+str(int(time.time())//2)+'.csv'
with open(resutsFileName, mode='w', newline='') as rfile:
    fieldnames = ['uninfected', 'infected', 'cured', 'dead', 'capacity']
    fwriter = csv.DictWriter(rfile, delimiter=',', fieldnames=fieldnames)
    fwriter.writeheader()

    if SHOW:
        ani = animation.FuncAnimation(fig, anim,  interval=10, frames=10, blit=False)
        plt.show()
    else:
        while len(recovered)<1 or len(infected)>0:
            anim(0)


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
