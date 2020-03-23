import random, matplotlib

matplotlib.use( 'tkagg' )
import matplotlib.animation as animation
import matplotlib.pyplot as plt

from person import Person

NUMPERSONS = 500
INFECTED_START = 0.03
XAXIS = 4000
YAXIS = 2000
DIVIDERWIDTH = 4
DOTSIZE = 20
COLORS = ['g', 'gold', 'tab:orange', 'r', 'purple']
INFECTIONRAD = 15  #
HOMEKIT = False

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
    allpersons.append(Person(infection, XAXIS, YAXIS, homekit=HOMEKIT))

# fig, (ax1, ax2) = plt.subplots(2)
fig, ax1 = plt.subplots()

ax1.set_xlim(0, XAXIS)  # xlim=(0, XAXIS), ylim=(0, YAXIS)
ax1.set_ylim(0, YAXIS)
ax1.set_xticklabels([])
ax1.set_yticklabels([])
ax1.axvline(XAXIS / 2, linewidth=(DIVIDERWIDTH - 2), color='b')
ax1.text(XAXIS // 4 - 100, YAXIS, "Outside", fontsize=10, horizontalalignment='center')
if HOMEKIT:
    ax1.text(XAXIS // 1.3 -70, YAXIS, "Home", fontsize=10, horizontalalignment='center')
else:
    ax1.text(XAXIS // 1.3 -100, YAXIS, "Hospital", fontsize=10, horizontalalignment='center')
scatter = ax1.scatter([],[], s=DOTSIZE)

def anim(i):
    stepAll()
    stepScene()


ani = animation.FuncAnimation(fig, anim,  interval=70, frames=10, blit=False)
plt.show()
