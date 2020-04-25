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
# distance = compareAuto(realData, numPersons=1000, infectedStart=0.03,  infectionProb=False, day=False, undiagDays=False, asymDays=False, symDays=False, hosp=False)

# def compareAutoPT(numPersons=1000, infectedStart=0.03,  infectionProb=False, day=False, undiagDays=False, asymDays=False, symDays=False):
#     return compareAuto(realData, numPersons, infectedStart,  infectionProb, day, undiagDays, asymDays, symDays, hosp=False)
def compareAutoPT(args):

    return compareAuto(realData, numpersons, args[0], args[1], args[2], args[3], args[4], args[5], hosp=False)

infectionProb= np.float(0.2)
day = np.uint8(7)
undiagDays = np.uint8(2*day)
asymDays = np.uint8(15 * day)
symDays = np.uint8(10 * day)

# minimize(compareAuto, x0, args=(a, b, c))
xopt = scipy.optimize.fmin(func=compareAutoPT, x0=[0.03, infectionProb, day, undiagDays, asymDays, asymDays])
# r= run(100)
# print(distance[0])
# print(distance[1])
