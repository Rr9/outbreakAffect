import random

import matplotlib.animation as animation
import matplotlib.pyplot as plt

from person import Person

NUMPERSONS = 100
INFECTED_START = 0.4
XAXIS = 4000
YAXIS = 2000
DIVIDERWIDTH = 5
DOTSIZE = 8
COLORS = ['g', 'y', 'tab:orange', 'r']

allpersons = []
positions = []
plots = []


# infection states 0,1,2,3
def step():
    for person in allpersons:
        person.step()


def drawScene(frameCount):
    positions = []
    colors = []

    for i in allpersons:
        colors.append(COLORS[i.inf])
        positions.append(i.pos)

    scatter.set_color(colors)
    scatter.set_offsets(positions)

    return scatter


for i in range(NUMPERSONS):
    infection = 1 if random.random() < INFECTED_START else 0
    allpersons.append(Person(infection, XAXIS, YAXIS))

fig, ax = plt.subplots()

ax.set_xlim(0, XAXIS)  # xlim=(0, XAXIS), ylim=(0, YAXIS)
ax.set_ylim(0, YAXIS)
ax.axvline(XAXIS / 2, linewidth=(DIVIDERWIDTH - 2), color='b')
ax.text(XAXIS // 4 - 100, YAXIS, "Outside", fontsize=10, horizontalalignment='center')
ax.text(XAXIS // 1.3, YAXIS, "Home", fontsize=10, horizontalalignment='center')
scatter = plt.scatter([],[], s=DOTSIZE)

def anim(i):
    step()
    drawScene(i)


ani = animation.FuncAnimation(fig, anim,  interval=500, frames=10, blit=False)
plt.show()
