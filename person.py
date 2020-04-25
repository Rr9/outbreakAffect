import math
import random

'''
Notes
0-Uninfected, 1-Undiagnosable, 2-Asymptomatic, 3-Symptomatic 4-Recovered, 5-Dead
!!! Be careful when adding new states !!!
'''


class Person():
    day = 7                 # cycles for one day
    standardDay = day
    # infectionRad = 1      # now an array inside __INIT__()
    infectionProb = 0.2     # probability of getting infected upon contact
    deathProb=0.25
    homeOutFreq = 7 * day   # infected people leave home every n days
    homekitFalseNeg = 0.25  # percentage of home kit diagnosis that are false negatives

    # mutation coeffs
    undiagDays = 2 * day
    asymDays = 15 * day
    symDays = 10 * day
    # list to make life easier to do calculations in mutate()
    mutations = [0, undiagDays, undiagDays + asymDays, undiagDays + asymDays + symDays, math.inf, math.inf]
    colors = ['g', 'gold', 'tab:orange', 'r', 'b', 'k']
    speeds = [35, 15, 5, 0]      #[outside, hospital, home, dead] movement speeds

    midlinewidth = 15

    def __init__(self, infectionState, xlim, ylim, divider, homekit=False, deviderWidth=5, size=20, baseRadius=20): #infectionProbOverride=0
        self.inf = infectionState
        # 0-Uninfected, 1-Undiagnosable, 2-Asymptomatic, 3-Symptomatic 4-Recovered
        self.age = 0            # days this person has lived for
        self.diseaseAge = 0     # days since person got diseasese
        # self.care = self.symDays

        self.xMidLim = divider-deviderWidth
        self.xEndLim = xlim
        self.yEndLim = ylim
        self.place = 0          # 0 outside, 1 insde
        self.daysInPlace = 0    # how many days this person has spent in this palace
        self.size = size*1.25
        self.size2x = self.size*2
        self.spreadRadius = [baseRadius, baseRadius, baseRadius*1.34]

        self.homekit = homekit  # if this is false there is a hospital
        self.hospital = not homekit
        self.speed = self.speeds[0]

        # this is here to model healthcare workers that wear ppe (if we want later)
        # self.infectionProb = infectionProbOverride if infectionProbOverride != 0 else self.infectionProb

        self.pos = self.initialPosition(self.xMidLim, ylim)  # [x,y]
        self.actualPos = self.determinePosition()

    def setExtraParams(self, infectionProb=False, day=False, undiagDays=False, asymDays=False, symDays=False, baseMovement=False):
        # Set param =  (internal value) if (not provided) else (provided value)
        self.infectionProb = self.infectionProb if (not infectionProb) else infectionProb
        self.day = self.day if (not day) else day
        self.undiagDays = self.undiagDays/self.standardDay*day if (not undiagDays) else undiagDays
        self.asymDays = self.asymDays/self.standardDay*day if (not asymDays) else asymDays
        self.symDays = self.symDays/self.standardDay*day if (not symDays) else symDays
        self.speeds[0] = self.speeds[0] if (not baseMovement) else baseMovement
        self.speeds = [self.speeds[0], self.speeds[0]*.45, self.speeds[0]*0.15, 0]
        self.speed = self.speeds[0]

    '''
    Create starting point for this person
        within x=(0, xEndLim) Y=(0, yEndLim)
        everyone starts off outside
    '''
    def initialPosition(self, xEndLim, yEndLim):
        return [int(random.uniform(self.size2x, xEndLim-self.size2x)), int(random.uniform(self.size2x, yEndLim-self.size2x))]

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
            self.diseaseAge += 1
            if self.inf<3:                            # if not symptomatic
                # self.diseaseAge+=1                  # disease age automatically goes up by 1
                self.radius = self.spreadRadius[1]
            elif self.inf == 3:                       # if you are symptomatic
                self.radius == self.spreadRadius[2]
                # if self.actualPos==1:               # only heal if youre at home or hopsital
                #     self.diseaseAge += 1
            else:
                self.radius == self.spreadRadius[0]

            # if age(days) >= amount of days it takes to move to the next state
            # move up in state
            if self.diseaseAge >= self.mutations[self.inf]:
                if self.inf < 3:                            # not symptomatic
                    self.inf += 1                           #   become symptomatic
                elif self.inf == 3:                         # if symptomatic
                    if self.place==0 and self.daysInPlace>1:  #   if outisde for more than 1 day
                                                            #   (this is so no one going out for groceries die)
                        self.inf += 2 if random.random()<self.deathProb else 1  # possibly die
                        if self.inf==5:
                            self.speed = self.speeds[3]
                    else:                       # if at home/hospital
                        self.inf += 1           #   recover
                        # self.speed = self.speed


    '''
    timesep each person 
    '''
    def step(self):
        self.age += 1
        self.daysInPlace+=1

        # if(self.inf>0):       #moved to mutate
        #     self.diseaseAge+=1

        self.move()
        # self.determinePosition()  #to determine where they actually are
        self.mutate()

        if self.place==0:   # if person is outside
            self.toHome()
            # self.toHospital() #   !! this is called in main now !!
        else:               #if person in inside(hospital or home)
            self.leaveHome()
            # self.leaveHospital()  !! moved to main !!


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
        xNegativeMove = 0 if(self.pos[0]<=self.size2x) else -self.speed                 # dont move left if at x0
        xPositiveMove = 0 if(self.pos[0]>=self.xMidLim-self.midlinewidth-self.size2x) else self.speed   # dont move right if at middle border
        yNegativeMove = 0 if(self.pos[1]<=self.size2x) else -self.speed                 # dont move up if at y0
        yPositiveMove = 0 if(self.pos[1]>=self.yEndLim-self.size2x) else self.speed     # dont move down if at yMax
        self.pos[0] += random.uniform(xNegativeMove, xPositiveMove)                     # % (self.xMidLim-self.midlinewidth-self.size)
        self.pos[1] += random.uniform(yNegativeMove, yPositiveMove)                     # % (self.yEndLim-self.size)

    '''
    Rules on how to move Inside 
        Move X within left border(50%, xMidLim) and the mid line (end, xEndLim)
        Move Y within top and bottom 
        Warp around between the 2 x walls and y edges
    '''
    def moveInside(self):
        xNegativeMove = 0 if(self.pos[0]<=self.xMidLim+self.midlinewidth+self.size2x) else -self.speed
        xPositiveMove = 0 if(self.pos[0]>=self.xEndLim-self.size2x) else self.speed
        yNegativeMove = 0 if(self.pos[1]<=self.size2x) else -self.speed
        yPositiveMove = 0 if(self.pos[1]>=self.yEndLim-self.size2x) else self.speed

        self.pos[0] += random.uniform(xNegativeMove, xPositiveMove)# % self.xEndLim
        self.pos[1] += random.uniform(yNegativeMove, yPositiveMove)# % (self.yEndLim-self.size)

    '''
    Goes from outside -> inside, inside -> outisde
        Spawns person randomly between X=(xstart, xlim) and Y=(0, ylim)
        reset counter for how long person has lived in this palce
    '''
    def changePlaces(self, xstart, xlim, ylim):
        self.pos = [int(random.uniform(xstart+self.size2x, xlim-self.size2x)), int(random.uniform(self.size2x, ylim-self.size2x))]
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
                    if random.random() > self.homekitFalseNeg:
                        self.speed = self.speeds[2]     # home speed
                        self.changePlaces(self.xMidLim, self.xEndLim, self.yEndLim)

    '''
    Uses each person's x pos to determine where they actually are 
    '''
    def determinePosition(self):
        # self.actualPos = 1 if self.xMidLim<=self.pos[0]<self.xEndLim else 0
        return 1 if self.xMidLim<=self.pos[0]<self.xEndLim else 0
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
                self.changePlaces(0, self.xMidLim, self.yEndLim)    # go back outside

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
                self.changePlaces(0, self.xMidLim, self.yEndLim)    # go back outside

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

