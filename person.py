import math
import random

'''
Notes
0-Uninfected, 1-Undiagnosable, 2-Asymptomatic, 3-Symptomatic 4-Recovered
!!! Be careful when adding new states !!!
'''


class Person():
    day = 7                # cycles for one day
    # infectionRad = 1      #
    infectionProb = 1      # probability of getting infected upon contact
    homeOutFreq = 7 * day   # infected people leave home every n days

    # mutation coeffs
    undiagDays = 1 * day
    asymDays = 10 * day
    symDays = 20 * day
    # list to make life easier to do calculations in mutate()
    mutations = [0, undiagDays, undiagDays + asymDays, undiagDays + asymDays + symDays, math.inf]
    colors = ['g', 'gold', 'tab:orange', 'r', 'b']
    speeds = [30, 10, 5]      #[outside, hospital, home] movement speeds

    midlinewidth = 15

    def __init__(self, infectionState, xlim, ylim, divider, homekit=False, infectionProbOverride=0, deviderWidth=5, size=20, baseRadius=20):
        self.inf = infectionState
        # 0-Uninfected, 1-Undiagnosable, 2-Asymptomatic, 3-Symptomatic 4-Recovered
        self.age = 0            # days this person has lived for
        self.diseaseAge = 0     # days since person got disease

        self.xMidLim = divider-deviderWidth
        self.xEndLim = xlim
        self.yEndLim = ylim
        self.pos = self.initialPosition(self.xMidLim, ylim)  # [x,y]
        self.place = 0          #0 outside, 1 insde
        self.daysInPlace = 0    #how many days this person has spent in this palace
        self.size = size+5
        self.spreadRadius = [baseRadius, baseRadius+20]

        self.homekit = homekit  # if this is false there is a hospital
        self.hospital = not homekit
        self.speed = self.speeds[0]

        # this is here to model healthcare workers that wear ppe (if we want later)
        self.infectionProb = infectionProbOverride if infectionProbOverride != 0 else self.infectionProb

    '''
    Create starting point for this person
        within x=(0, xEndLim) Y=(0, yEndLim)
        everyone starts off outside
    '''
    def initialPosition(self, xEndLim, yEndLim):
        return [int(random.uniform(0, xEndLim)), int(random.uniform(0, yEndLim))]

    '''
    Contracts disease 
    '''
    def contract(self):  # catch disease
        # get infected = if not infected and random num is > than probability
        if (self.inf == 0) and (random.random() <= self.infectionProb):
            self.inf = 1
            self.diseaseAge=0

    '''
    Incrase severity of disease
    '''
    def mutate(self):
        if self.inf > 0:  # if you are infected
            # if age(days) >= amount of days it takes to move to the next state
            # move up in state
            if self.diseaseAge >= self.mutations[self.inf]:
                self.inf += 1

            if 1<=self.inf<3:
                self.radius=self.spreadRadius[0]
            elif self.inf==3:
                self.radius==self.spreadRadius[1]
            else:
                self.radius==0

    '''
    timesep each person 
    '''
    def step(self):
        self.age += 1
        self.daysInPlace+=1
        if(self.inf>0):
            self.diseaseAge+=1

        self.move()

        if self.place==0:   # if person is outside
            self.toHome()
            # self.toHospital() #   !! this is called in main now !!
        else:               #if person in inside(hospital or home)
            self.leaveHome()
            # self.leaveHospital()  !! moved to main !!

        self.mutate()

    '''
    Defines how people move, called in step()
    '''
    def move(self):
        if self.place==0:
            self.moveOutside()
        else:
            self.moveInside()

    '''
    Rules on how to move outside 
        Move X within left border(0) and the mid line (50%, xMidLim)
        Move Y within top and bottom 
        Warp around 
    '''
    def moveOutside(self):
        self.pos[0] = (self.pos[0] + random.uniform(-1*self.speed, self.speed)) % (self.xMidLim-self.midlinewidth)
        self.pos[1] = (self.pos[1] + random.uniform(-1*self.speed, self.speed)) % self.yEndLim

    '''
    Rules on how to move Inside 
        Move X within left border(50%, xMidLim) and the mid line (end, xEndLim)
        Move Y within top and bottom 
        Warp around between the 2 x walls and y edges
    '''
    def moveInside(self):
        x = (self.pos[0] + random.uniform(-1*self.speed, self.speed)) % self.xEndLim
        self.pos[0] = x if (x>(self.xMidLim+self.size)) else (self.xEndLim-(self.xMidLim+self.size-x))
        self.pos[1] = (self.pos[1] + random.uniform(-1*self.speed, self.speed)) % self.yEndLim

    '''
    Goes from outside -> inside, inside -> outisde
        Spawns person randomly between X=(xstart, xlim) and Y=(0, ylim)
        reset counter for how long person has lived in this palce
    '''
    def changePlaces(self, xstart, xlim, ylim):
        self.pos = [int(random.uniform(xstart, xlim)), int(random.uniform(0, ylim))]
        self.place = 1 if self.place==0 else 0      # change state to home/hospital
        self.daysInPlace = 0                        # reset how long has been spent here

    '''
    Move person to home under these conditions
        Sim is about home and outside
        If at the end of the day 
            person is infected Asymptomatically 
            
        Move person, change speed
    '''
    def toHome(self):
        if self.homekit:                    # if this is sim with kits at home
            if self.age % self.day == 0:    # check yourself at the end of every day
                if 4> self.inf >1:          # if disease is diagnosable
                    self.speed = self.speeds[2]     # home speed
                    self.changePlaces(self.xMidLim, self.xEndLim, self.yEndLim)

    '''
    Checks if this person should be hospitalised using rules
    '''
    def shouldHospitalise(self):
        if self.place==0 and (not self.homekit):                # if this is sim with hospital
                return 4> self.inf > 2          # if person is symptomatic
        return False

    '''
    Move person to hospital under these conditions
        Sim is about hospital and outside
            person is infected Symptomatically 
            
        Move person, change speed  
    '''
    def toHospital(self):
        # if not self.homekit:                # if this is sim with hospital
        #     if 4> self.inf > 2:                # if person is symptomatic
        self.speed = self.speeds[1] # hospital speed
        self.changePlaces(self.xMidLim, self.xEndLim, self.yEndLim)

    '''
    Move to home->outside under these conditions
        If at home and sim is about home&outside
            if cured or need to do groceries            
        
        Move person, change speed  
    '''
    def leaveHome(self):
        if self.place==1 and self.homekit:          # if at home
            if self.inf>3 or self.daysInPlace>self.homeOutFreq:   # if they need to go outside || cured
                self.speed = self.speeds[0]         # outside speed
                self.changePlaces(0, self.xEndLim, self.yEndLim)    # go back outside

    def shouldDischarge(self):
        if self.place==1 and (not self.homekit):    # if in hospital
            return self.inf>3                       # if recovered
        return False

    '''
    Move to home->outside under these conditions
        If at hospital and sim is about hospital&outside
            if cured

        Move person, change speed  
    '''
    def leaveHospital(self):
        if self.place==1 and (not self.homekit):    # if in hospital
            if self.inf>3:                          # if recovered
                self.speed = self.speeds[0]         # outside speed
                self.changePlaces(0, self.xEndLim, self.yEndLim)    # go back outside

    # def getPos(self):
    #     return self.pos, self.inf

    '''
    Return distance from this person to other person given 
    @:param other - other person
    '''
    def distance(self, other):
        return math.sqrt(((self.pos[0] - other.pos[0]) ** 2) + ((self.pos[1] - other.pos[1]) ** 2))

    # @staticmethod
    # def radius(p1, p2):
    #     return math.sqrt(((p1[0] - p2[0]) ** 2) + ((p1[1] - p2[1]) ** 2))
