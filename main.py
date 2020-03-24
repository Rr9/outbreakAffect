import random

import matplotlib
import seaborn as sns

matplotlib.use( 'tkagg' )
import matplotlib.animation as animation
import matplotlib.pyplot as plt

from person import Person
from hospital import Hospital


NUMPERSONS = 500
INFECTED_START = 0.03
XAXIS = 4000
YAXIS = 2000
DIVIDERWIDTH = 4
DIVIDERRATIO = 3/4
DIVIDERLOC = XAXIS*DIVIDERRATIO+(DIVIDERWIDTH/2)
LEFTMIDDLE = DIVIDERLOC//2
RIGHTMIDDLE = DIVIDERLOC+(XAXIS-DIVIDERLOC)//2

DOTSIZE = 20
COLORS = ['g', 'gold', 'tab:orange', 'r', 'purple', 'k']
INFECTIONRAD = DOTSIZE  #
HOMEKIT = True

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
            # if person.place == 0:           # if outside
            if person.inf==0:           # if !infected/healthy
                notinfected.append(person)
            else:                       # if any stage of infection & person is outside
                infected.append(person)     # this is to prevent people from infecting across hospital border
        elif infection == 4:
            recovered.append(person)
        # else:                               #infection 5 - dead
        #     dead.append(person)

    # Update charts
    scatter.set_color(colors)               # add color list to chart
    scatter.set_offsets(positions)          # add position list to chart
    insideText.set_text(str(insideCount))   # set number count
    outsideText.set_text(str(outsideCount))
    noninfText.set_text(str(len(notinfected)))
    infectedText.set_text(str(len(infected)))
    curedText.set_text(str(len(recovered)))
    # TODO take len(uninfected), len(infected), len(recovered), len(dead)
    # TODO make graph from ^^^

    # Collisons/coughs with infected people
    for inf in infected:
        for good in notinfected:
            if inf.distance(good)<inf.radius and inf.place==0:
                good.contract()

    return scatter

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

# fig, (ax1, ax2) = plt.subplots(2)
sns.set_style("white")
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



ani = animation.FuncAnimation(fig, anim,  interval=50, frames=10, blit=False)
plt.show()


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
