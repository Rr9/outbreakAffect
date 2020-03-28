import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd
import time
import sys
import csv

filename = sys.argv[1]
with open(filename) as csvDataFile:
    reader = csv.reader(csvDataFile)
    next(reader)
    uninfected, infected, cured, dead = [], [], [], []
    for row in reader:
        uninfected.append(int(row[0]))
        infected.append(int(row[1]))
        cured.append(int(row[2]))
        dead.append(int(row[3]))


plt.ion() # Makes it interactive. Allows for dynamic plotting
fig, ax = plt.subplots()

#fig = plt.stackplot()
#%ax = fig.add_subplot(111)

# some X and Y data
w = [uninfected[0]]
x = [infected[0]]
y = [cured[0]]
z = [dead[0]]

sns.set()
dictionary = {'uninfected': w, 'infected': x, 'cured': y, 'dead': z,}
#dictionary = {'uninfected': uninfected, 'infected': infected, 'cured': cured, 'dead': dead,}
data = pd.DataFrame(dictionary, index=range(len(infected)))
data_perc = data.divide(data.sum(axis=1), axis=0)

ax.stackplot(range(len(x)), data_perc["infected"], data_perc["uninfected"],  data_perc["cured"], data_perc["dead"], labels=['I','S','C','D'], colors=['red', 'green', 'blue', 'black'])
plt.legend(loc='lower left')
plt.margins(0,0)
plt.title('100 % stacked area chart')


## draw and show it
fig.canvas.draw()
plt.show()#block=False)

# loop to update the data
for i in range(1, len(infected)):
    try:
        w.append(uninfected[i])
        x.append(infected[i])
        y.append(cured[i])
        z.append(dead[i])
        dictionary = {'uninfected': w, 'infected': x, 'cured': y, 'dead': z}
        data = pd.DataFrame(dictionary, index=range(len(x)))
        data_perc = data.divide(data.sum(axis=1), axis=0)
        ax.stackplot(range(len(x)), data_perc["infected"], data_perc["uninfected"],  data_perc["cured"], data_perc["dead"], labels=['I','S','C','D'], colors=['red', 'green', 'blue', 'black'])
        # set the new data
        #li.set_xdata(x)
        #li.set_ydata(y)

        #ax.relim() 
        ax.autoscale_view(True,True,True) 

        fig.canvas.draw()

        #time.sleep(0.001)
    except KeyboardInterrupt:
        plt.close('all')
        break
