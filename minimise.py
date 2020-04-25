import numpy as np
import scipy.optimize

from main import *

# from scipy.optimize import minimize

filename = "results\JHCanadaOntario.txt"
realDataFile = open(filename, "r")
realData = realDataFile.read().strip().strip(",").split(",")
realData = [float(data) for data in realData]
numpersons = 1000
realData = [number/14570000 for number in realData]
print(realData)
# distance = compareAuto(realData, numPersons=1000, infectedStart=0.03,  infectionProb=False, day=False, undiagDays=False, asymDays=False, symDays=False, hosp=100, basemovementratio)

def compareAutoPT(args):
    return compareAuto(realData, int(numpersons), float(args[0]), float(args[1]), int(args[2]), int(args[3]), int(args[4]), int(args[5]), int(args[6]), int(args[7]))


BASEMOVEMENTRATIO = 5
baseMovementSpeed = np.int( (dimDensity**2)/(4000*6000)*BASEMOVEMENTRATIO )  #BASICALLY SOCIAL VAMPIRISM FACTOR

infectionStart = np.float(0.004)
infectionProb = np.float(0.5)

day = np.uint8(10)
undiagDays = np.uint8(4 * day)
asymDays = np.uint8(10 * day)
symDays = np.uint8(10 * day)
hosp = np.uint(100)

# distance = compareAuto(realData, numPersons=1000, infectedStart=infectionStart,  infectionProb=infectionProb, day=False, undiagDays=False, asymDays=False, symDays=False, hosp=10, baseMovementSpeed=baseMovementSpeed)
xopt = scipy.optimize.fmin(func=compareAutoPT, x0=[infectionStart, infectionProb, day, undiagDays, asymDays, asymDays, hosp, baseMovementSpeed])

print(xopt)
# minimize(compareAuto, x0, args=(a, b, c))

# r= run(100)
print(distance[0])
print(distance[1])
