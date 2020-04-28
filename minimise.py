import numpy as np
import scipy.optimize
import matplotlib.pyplot as plt

from main import *

# from scipy.optimize import minimize

filename = "results\JHCanadaOntario.txt"
realDataFile = open(filename, "r")
realData = realDataFile.read().strip().strip(",").split(",")
realData = [float(data) for data in realData]
numpersons = 1000
realData = [number/14570000 for number in realData]
print(realData)
# distance = compareAuto(realData, numPersons=1000, infectedStart=0.03,  infectionProb=False, day=False, undiagDays=False, asymDays=False, symDays=False, hosp=False)


def compareAutoPT(args):
    return compareAuto(realData, numpersons, args[0], args[1], args[2], args[3], args[4], args[5], args[6], args[7])

BASEMOVEMENTRATIO = 15
baseMovementSpeed = np.uint32( (dimDensity**2)/(4000*6000)*BASEMOVEMENTRATIO )

infectionStart = np.float(0.3)
infectionProb = np.float(0.2)
day = np.uint8(7)
undiagDays = np.uint8(2*day)
asymDays = np.uint8(15 * day)
symDays = np.uint8(10 * day)
hosp = np.uint(100)

# minimize(compareAuto, x0, args=(a, b, c))
xopt = scipy.optimize.fmin(func=compareAutoPT, x0=[infectionStart, infectionProb, day, undiagDays, asymDays, asymDays, hosp, baseMovementSpeed])
# r= run(100)
# print(distance[0])
# print(distance[1])

def multigraph(la, lb)
    # plot two graphs to compare
    plt.plot(len(la), la, 'r', len(lb), lb, 'b')
    plt.show()
