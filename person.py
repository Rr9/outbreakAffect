import math
import random

'''
Notes
0-Uninfected, 1-Undiagnosable, 2-Asymptomatic, 3-Symptomatic 4-Recovered
'''


class Person():
    day = 7                # cycles for one day
    # infectionRad = 1        #
    infectionProb = .5      # probability of getting infected upon contact
    homeOutFreq = 7 * day   # infected people leave home every n days

    # mutation coeffs
    undiagDays = 4 * day
    asymDays = 10 * day
    symDays = 7 * day
    # list to make life easier to do calculations in mutate()
    mutations = [0, undiagDays, undiagDays + asymDays, undiagDays + asymDays + symDays, math.inf]
    colors = ['g', 'gold', 'tab:orange', 'r', 'b']
    speeds = [30, 10, 5]      #[outside, hospital, home] movement speeds

    def __init__(self, infectionState, xlim, ylim, homekit=False, infectionProbOverride=0, dividerWidth=5):
        self.inf = infectionState
        # 0-Uninfected, 1-Undiagnosable, 2-Asymptomatic, 3-Symptomatic 4-Recovered
        self.age = 0            # days this person has lived for
        self.diseaseAge = 0     # days since person got disease

        self.xMidLim = (xlim//2)-dividerWidth
        self.xEndLim = xlim
        self.yEndLim = ylim
        self.pos = self.initialPosition(self.xMidLim, ylim)  # [x,y]
        self.place = 0          #0 outside, 1 insde
        self.daysInPlace = 0    #how many days this person has spent in current location

        self.homekit = homekit  # if this is false there is a hospital
        #self.hospital = not homekit
        self.speed = self.speeds[0]

        # this is here to model healthcare workers that wear ppe (if we want later)
        #self.infectionProb = infectionProbOverride if infectionProbOverride != 0 else self.infectionProb

    # create starting point for this person
    def initialPosition(self, xStartLim, yStartLim):
        return [int(random.uniform(0, xStartLim)), int(random.uniform(0, yStartLim))]

    #gets disease
    def contract(self):  # catch disease
        # get infected = if not infected and random num is > than probability
        if (self.inf == 0) and (random.random() > self.infectionProb):
            self.inf = 1
            self.diseaseAge=0

    #incrase severity of disease
    def mutate(self):
        if self.inf > 0:  # if you are infected
            # if age(days) >= amount of days it takes to move to the next state
            # move up in state
            if self.diseaseAge >= self.mutations[self.inf]:
                self.inf += 1

    #what happens in one timestep
    def step(self):
        self.age += 1
        self.daysInPlace+=1
        if(self.inf>0):
            self.diseaseAge+=1

        self.move()

        if self.place==0:   # if person is outside
            self.toHome()
            self.toHospital()
        else:
            self.leaveHome()
            self.leaveHospital()
        self.mutate()

    def move(self):
        if self.place==0:
            self.moveOutside()
        else:
            self.moveInside()

    def moveOutside(self):
        self.pos[0] = (self.pos[0] + random.uniform(-1*self.speed, self.speed)) % self.xMidLim
        self.pos[1] = (self.pos[1] + random.uniform(-1*self.speed, self.speed)) % self.yEndLim

    def moveInside(self):
        x = (self.pos[0] + random.uniform(-1*self.speed, self.speed)) % self.xEndLim
        self.pos[0] = x if x>self.xMidLim else (self.xEndLim-(self.xMidLim-x))
        self.pos[1] = (self.pos[1] + random.uniform(-1*self.speed, self.speed)) % self.yEndLim

    def changePlaces(self, xstart, xlim, ylim):
        self.pos = [int(random.uniform(xstart, xlim)), int(random.uniform(0, ylim))]
        self.place = 1 if self.place==0 else 0 # change state to home/hospital
        self.daysInPlace = 0

    def toHome(self):
        if self.homekit:                    # if this is sim with kits at home
            if self.age % self.day == 0:    # check yourself at the end of every day
                if 4> self.inf >1:          # if disease is diagnosable
                    self.speed = self.speeds[2]     # home speed
                    self.changePlaces(self.xMidLim, self.xEndLim, self.yEndLim)

    def toHospital(self):
        if not self.homekit:                # if this is sim with hospital
            if 4> self.inf > 2:                # if person is symptomatic
                self.speed = self.speeds[1] # hospital speed
                self.changePlaces(self.xMidLim, self.xEndLim, self.yEndLim)

    def leaveHome(self):
        if self.place==1 and self.homekit:          # if at home
            if self.inf>3 or self.daysInPlace>self.homeOutFreq:   # if they need to go outside || cured
                self.speed = self.speeds[0]         # outside speed
                self.changePlaces(0, self.xEndLim, self.yEndLim)    # go back outside

    def leaveHospital(self):
        if self.place==1 and (not self.homekit):    # if in hospital
            if self.inf>3:                          # if recovered
                self.speed = self.speeds[0]         # outside speed
                self.changePlaces(0, self.xEndLim, self.yEndLim)    # go back outside

    # def getPos(self):
    #     return self.pos, self.inf

    def distance(self, other):
        return math.sqrt(((self.pos[0] - other.pos[0]) ** 2) + ((self.pos[1] - other.pos[1]) ** 2))

    # @staticmethod
    # def radius(p1, p2):
    #     return math.sqrt(((p1[0] - p2[0]) ** 2) + ((p1[1] - p2[1]) ** 2))
