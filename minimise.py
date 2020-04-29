from main import *

# from scipy.optimize import minimize

filenameOn = "results\JHCanadaOntario.txt"
realpopulationOn = 14570000

filenameIce = "results\JHIceland.txt"
realpopulationIce = 364134

filename = filenameIce
numpersons = 3000
realpopulation = realpopulationIce

realDataFile = open(filename, "r")
realData = realDataFile.read().strip().strip(",").split(",")
realData = np.array([float(data) for data in realData])/realpopulation

# realData = [number/realpopulation for number in realData]
# realData = realData/realpopulation
startpercentage = realData[0]
print(len(realData), realData*numpersons, realpopulation)
print(startpercentage)

def compareAutoPT(args):
    return compareAuto(realData, int(numpersons), float(args[0]), float(args[1]), int(args[2]), int(args[3]), int(args[4]), int(args[5]), int(args[6]), int(args[7]))

def multigraph(la, lb, distances, names):
    # plot two graphs to compare
    plt.plot(range(len(la)), la, 'b')

    mxColor = max(distances)
    mnColor = min(distances)

    for i in range(len(lb)):


        redness = map(distances[i], mnColor, mxColor, 0.75, 1) if len(lb)>1 else 0.75

        plt.plot(range(len(lb[i])), lb[i], color=[redness, 0, 1-redness])

    plt.legend(names)
    plt.show()

def map(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min


## Setup Stats ###########


POPDENSITY = 3  #KiloPX^2
# dimDensity = math.sqrt(NUMPERSONS/POPDENSITY)*1000

BASEMOVEMENTRATIO = 5.4
baseMovementSpeed = np.int( (dimDensity**2)/(4000*6000)*BASEMOVEMENTRATIO )  #BASICALLY SOCIAL VAMPIRISM FACTOR

infectionStart = np.float(startpercentage)
infectionProb = np.float(0.26)
baseRadius =72

day = 12
undiagDays = np.uint8(7 * day)
asymDays = np.uint8(14 * day)
symDays = np.uint8(15 * day)
hosp = math.ceil(3.2*(numpersons/1000)*1)

## Genateate data
data = []
distance = []
for i in range(1):
    gen = compareAuto(realData, numPersons=numpersons, infectedStart=infectionStart, infectionProb=infectionProb, baseradius=baseRadius,
                      day=day, undiagDays=undiagDays, asymDays=asymDays, symDays=symDays, hosp=hosp, baseMovementSpeed=baseMovementSpeed)
    data.append(np.array(gen[0]))
    distance.append(gen[1])
    print(gen[0])
## xopt = scipy.optimize.fmin(func=compareAutoPT, x0=[infectionStart, infectionProb, day, undiagDays, asymDays, asymDays, hosp, baseMovementSpeed])

real = np.array(realData)*numpersons
generated = np.array(distance[0])

# print(real)
# print(generated)
multigraph(real, data, distance, ["Real - Iceland", "Generated"])
