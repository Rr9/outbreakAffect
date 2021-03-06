class Hospital():

    capacity = 500

    def __init__(self, xStartLim, xEndLim, yStartLim=0, yEndLim=2000):
        self.xStartLim = xStartLim
        self.xEndLim = xEndLim

        self.occupants = 0

    def available(self):
        return self.occupants<self.capacity

    def admit(self):
        self.occupants+=1
        # print("+\t"+str(self.occupants))

    def release(self):
        self.occupants-=1
        # print("-\t"+str(self.occupants))

    def setCapacity(self, cap=False):
        self.capacity = self.capacity if cap==False else cap
