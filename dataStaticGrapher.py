import csv

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

filename = "rr/hs4.csv"
# def staticGraph(w=w,x=x,y=y,z=z):
def staticGraph(filename = filename):

    with open(filename) as csvDataFile:
        reader = csv.reader(csvDataFile)
        next(reader)
        uninfected, infected, cured, dead = [], [], [], []
        for row in reader:
            uninfected.append(int(row[0]))
            infected.append(int(row[1]))
            cured.append(int(row[2]))
            dead.append(int(row[3]))
            try:
                [next(reader) for _ in range(0,7)]
            except StopIteration:
                pass


    #plt.ion() # Makes it interactive. Allows for dynamic plotting
    fig = plt.subplots()

    #fig = plt.stackplot()
    #%ax = fig.add_subplot(111)

    # some X and Y data
    w = uninfected
    x = infected
    y = cured
    z = dead

    sns.set()
    dictionary = {'uninfected': w, 'infected': x, 'cured': y, 'dead': z,}
    #dictionary = {'uninfected': uninfected, 'infected': infected, 'cured': cured, 'dead': dead,}
    data = pd.DataFrame(dictionary, index=range(len(infected)))
    data_perc = data.divide(data.sum(axis=1), axis=0)

    plt.stackplot(range(len(x)), data_perc["infected"], data_perc["uninfected"],  data_perc["cured"], data_perc["dead"], labels=['Infected','Susceptible','Cured','Dead'], colors=['red', 'xkcd:cerulean', 'green', 'black'])
    plt.legend(loc='lower left')
    plt.margins(0,0)
    plt.title('100 % stacked area chart')



    plt.show()