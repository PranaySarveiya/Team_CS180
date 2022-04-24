import math
import os
import sys

numberOfRows = int(sys.argv[1])
path = os.path.abspath(os.path.dirname(__file__))

with open(path + "\\US_Accidents_Dec21_updated.csv", "r") as file:
    lines = file.readlines()



newFilename = "US_Accidents_" + str(numberOfRows) + "_rows.csv"
increment = math.floor(len(lines) / numberOfRows)
row = 0
count = 0
with open(path + "\\" + newFilename, "w+") as newFile:
    while (count <= numberOfRows):
            newFile.write(lines[row])
            row += increment
            count += 1

    newFile.close()