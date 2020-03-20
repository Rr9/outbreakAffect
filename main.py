import random

import matplotlib.animation as animation
import matplotlib.pyplot as plt

from person import Person

NUMPERSONS = 500
INFECTED_START = 0.03
XAXIS = 4000
YAXIS = 2000
DIVIDERWIDTH = 4
DOTSIZE = 7
COLORS = ['g', 'gold', 'tab:orange', 'r', 'b']
INFECTIONRAD = 15  #

allpersons = []
positions = []
plots = []


# infection states 0,1,2,3
def stepAll():
    for person in allpersons:
        person.step()


def stepScene():
    positions = []
    colors = []
    notinfected = []
    infected = []

    for person in allpersons:
        infection = person.inf
        colors.append(COLORS[infection])
        positions.append(person.pos)
        if infection<4:
            if person.inf==0:
                notinfected.append(person)
            else:
                infected.append(person)

    scatter.set_color(colors)
    scatter.set_offsets(positions)

    for inf in infected:
        for good in notinfected:
            if inf.distance(good) < INFECTIONRAD:
                good.contract()

    return scatter


for i in range(NUMPERSONS):
    infection = 1 if random.random() < INFECTED_START else 0
    allpersons.append(Person(infection, XAXIS, YAXIS, homekit=True))

fig, ax = plt.subplots()

ax.set_xlim(0, XAXIS)  # xlim=(0, XAXIS), ylim=(0, YAXIS)
ax.set_ylim(0, YAXIS)
ax.axvline(XAXIS / 2, linewidth=(DIVIDERWIDTH - 2), color='b')
ax.text(XAXIS // 4 - 100, YAXIS, "Outside", fontsize=10, horizontalalignment='center')
ax.text(XAXIS // 1.3, YAXIS, "Home", fontsize=10, horizontalalignment='center')
scatter = plt.scatter([],[], s=DOTSIZE)

def anim(i):
    stepAll()
    stepScene()


ani = animation.FuncAnimation(fig, anim,  interval=300, frames=10, blit=False)
plt.show()
