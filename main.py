from person import Person
import random
import numpy as np
import matplotlib.pyplot as plt

NUMPERSONS = 100
INFECTED_START = 0.4
XAXIS = 4000
YAXIS = 2000
DIVIDERWIDTH = 5
DOTSIZE = 8
COLORS = ['g', 'y', 'tab:orange', 'r']

allpersons = []
positions = [[[], []],
             [[], []],
             [[], []],
             [[], []]]


# infection states 0,1,2,3

def drawScene():
    for i in allpersons:
        p = i.pos
        inf = i.inf
        positions[inf][0].append(p[0])
        positions[inf][1].append(p[1])

    # fig = plt.figure()
    plt.axes(xlim=(0, XAXIS), ylim=(0, YAXIS))

    for i, val in enumerate(positions):
        plt.scatter(val[0], val[1], s=DOTSIZE, c=COLORS[i])

    plt.axvline(XAXIS/2, linewidth=(DIVIDERWIDTH-2), color='b')
    plt.text(XAXIS//4-100, YAXIS, "Outside", fontsize=10, horizontalalignment='center')
    plt.text(XAXIS//1.3, YAXIS, "Home", fontsize=10, horizontalalignment='center')
    plt.show()


def step():
    for person in allpersons:
        person.step()


for i in range(NUMPERSONS):
    infection = 1 if random.random() < INFECTED_START else 0
    allpersons.append(Person(infection, XAXIS, YAXIS))


drawScene()
# print(positions)
step()
