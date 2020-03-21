import random

import matplotlib.animation as animation
import matplotlib.pyplot as plt

from person import Person

NUMPERSONS = 500
INFECTED_START = 0.03
XAXIS = 4000
YAXIS = 2000
DIVIDERWIDTH = 7
DOTSIZE = 20
COLORS = ['g', 'gold', 'tab:orange', 'r', 'purple']
INFECTIONRAD = DOTSIZE  #
HOMEKIT = False

allpersons = []
positions = []
plots = []


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
    positions = []
    colors = []
    notinfected = []
    infected = []
    # TODO recovered list or count

    # extract everyone's infection data and put People into lists
    for person in allpersons:
        infection = person.inf              # get infectiron status
        colors.append(COLORS[infection])    # set their color for the chart
        positions.append(person.pos)        # set their postion for chart
        if infection<4:                     # if not cured
            if person.inf==0:               # if !infected/healthy
                notinfected.append(person)
            elif person.place==0:           # if any stage of infection & person is outside
                infected.append(person)     # this is to prevent people from infecting across hospital border
        # TODO else: add to recovered list/count

    # Update charts
    scatter.set_color(colors)               # add color list to chart
    scatter.set_offsets(positions)          # add position list to chart
    # TODO take len(uninfected), len(infected), len(recovered), len(dead)
    # TODO make graph from ^^^

    # Collisons/coughs with infected people
    for inf in infected:
        for good in notinfected:
            if inf.distance(good) < INFECTIONRAD:
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
    allpersons.append(Person(infection, XAXIS, YAXIS, homekit=HOMEKIT))

# fig, (ax1, ax2) = plt.subplots(2)
fig, ax1 = plt.subplots()

ax1.set_xlim(0, XAXIS)  # xlim=(0, XAXIS), ylim=(0, YAXIS)
ax1.set_ylim(0, YAXIS)
ax1.set_xticklabels([])
ax1.set_yticklabels([])
ax1.axvline(XAXIS / 2, linewidth=(DIVIDERWIDTH - 2), color='grey')
ax1.text(XAXIS // 4 - 100, YAXIS+10, "Outside", fontsize=10, horizontalalignment='center')
if HOMEKIT:
    ax1.text(XAXIS // 1.3 -70, YAXIS+10, "Home", fontsize=10, horizontalalignment='center')
else:
    ax1.text(XAXIS // 1.3 -100, YAXIS+10, "Hospital", fontsize=10, horizontalalignment='center')
scatter = ax1.scatter([],[], s=DOTSIZE)



ani = animation.FuncAnimation(fig, anim,  interval=100, frames=10, blit=False)
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