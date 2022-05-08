import os
import math
import os
from sre_parse import State
import sys
from typing import Final
import numpy as np
import matplotlib.pyplot as plt

#x = -126 to -66
#y = 24 to 50
def update_scatter_plot(STATES_ABV):
    Accident_Lines = []
    with open("US_Accidents_60000_rows.csv", "r") as file:
        lines = file.readlines()
        goodLines = []
        for line in lines:
            line = line.rstrip()
            if len(line) != 0:
                goodLines.append(line)

        newLines = []
        for line in goodLines:
            myList = line.split(",")
            Accident_Lines.append(myList)


    State_Lines = []    #State Name, Latitude, Longitude
    with open("statelatlong.csv", "r") as locationData:
        lines = locationData.readlines()
        goodLines = []
        for line in lines:
            line = line.rstrip()
            if len(line) != 0:
                goodLines.append(line)

        newLines = []
        for line in goodLines:
            myList = line.split(",")
            State_Lines.append(myList)

    for state_row in State_Lines:
        cnt = 0
        for accident_row in Accident_Lines:
            if state_row[0] == accident_row[15]:
                cnt += 1
        state_row.append(cnt)

    Final_Data = State_Lines #State Name, Latitude, Longitude, Population Estimate in 2019, Number of Crashes
    del Final_Data[0]

#    with open("Data_For_Scatter.csv", "w+") as outputData:
#        for row in Final_Data:
#            for item in row:
#                outputData.write(str(item) + ',')
#            outputData.write('\n')


    y = []
    x = []
    area = []
    for row in Final_Data[1:]:
        #print(row)
        y.append(float(row[1]))
        x.append(float(row[2]))
        area.append((float(row[4])/float(row[3])) * 3000000)
    #area = np.pi * (25 * np.random.rand(51))**2
    img = plt.imread("us_mercator.jpg")
    fig, ax = plt.subplots()
    ax.imshow(img, extent=[-126, -66, 24, 50])
    plt.xlabel("Latitude")
    plt.ylabel("Longitude")
    plt.title("Scatterplot of Accidents by Population Density Per State")
    plt.xlim(-126, -66)
    plt.ylim(24, 50)
    plt.scatter(x, y, c="blue", linewidths=2, marker ="o", edgecolors="blue", s=area, alpha=0.2)
    plt.savefig('scatter_plot.png')
    plt.show()





