import random
import math

'''
Notes
0-Uninfected, 1-Undiagnosable, 2-Asymptomatic, 3-Recovered
'''


class Person():
    day = 20                # cycles for one day
    infectionRad = 1        #
    infectionProb = .5      # probability of getting infected upon contact
    homeOutFreq = 7 * day   # infected people leave home every n days

    # mutation coeffs
    undiagDays = 5 * day
    asymDays = 5 * day
    symDays = 5 * day
    # list to make life easier to do calculations in mutate()
    mutations = [0, undiagDays, undiagDays + asymDays, undiagDays + asymDays + symDays]
    colors = ['g', 'y', 'tab:orange', 'r']
    speeds = [4, 2, 0]      #[outside, hospital, home] movement speeds

    def __init__(self, infectionState, xlim, ylim, homekit=False, infectionProbOverride=0, deviderWidth=5):
        self.inf = infectionState
        # 0-Uninfected, 1-Undiagnosable, 2-Asymptomatic, 3-Recovered
        self.age = 0            # days this person has lived for
        self.diseaseAge = 0     # days since person got disease
        self.pos = self.initialPosition((xlim//2)-deviderWidth, ylim)  # [x,y]
        self.place = 0          #0 outside, 1 insde
        self.daysInPlace = 0    #how many days this person has spent in this palace
        self.homekit = homekit  # if this is false there is a hospital
        self.hospital = not homekit
        self.speed = self.speeds[0]

        # this is here to model healthcare workers that wear ppe (if we want later)
        self.infectionProb = infectionProbOverride if infectionProbOverride != 0 else self.infectionProb

    # create starting point for this person
    def initialPosition(self, xStartLim, yStartLim):
        return [int(random.uniform(0, xStartLim)), int(random.uniform(0, yStartLim))]

    #gets disease
    def contract(self):  # catch disease
        # get infected = if not infected and random num is > than probability
        if (self.inf == 0) and (random.random() > self.infectionProb):
            self.inf = 1

    #incrase severity of disease
    def mutate(self):
        if self.inf > 0:  # if you are infected
            # if age(days) >= amount of days it takes to move to the next state
            # move up in state
            if self.age >= self.mutations[self.inf + 1]:
                self.inf += 1

    def step(self):
        self.age += 1
        if(self.place==0): #if person is outside
            self.moveOutside()

    def move(self):
        pass

    def moveOutside(self):
        self.loc[0] += random.randint(-1*self.speed, self.speed)
        self.loc[1] += random.randint(-1*self.speed, self.speed)

    def toHome(self):
        self.speed = self.speeds[2]     #home speed

    def toHospital(self):
        self.speed = self.speeds[1]     #hospital speed

    def leaveHome(self):
        self.speed = self.speeds[0]     #outside speed

    def leaveHospital(self):
        self.speed = self.speeds[0]     #outside speed

    # def getPos(self):
    #     return self.pos, self.inf

    @staticmethod
    def radius(p1, p2):
        return math.sqrt(((p1[0] - p2[0]) ** 2) + ((p1[1] - p2[1]) ** 2))
