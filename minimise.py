from main import *
filename = "results\JHCanadaOntario.txt"
realDataFile = open(filename, "r")
realData = realDataFile.read().strip().strip(",").split(",")
realData = [float(data) for data in realData]
# print(float(realData[0]))
print(realData)
realData = [number/14570000 for number in realData]
distance = compareAuto(realData, numPersons=1000, infectedStart=0.03,  infectionProb=False, day=False, undiagDays=False, asymDays=False, symDays=False, hosp=False)

# r= run(100)
print(distance[0])
print(distance[1])
