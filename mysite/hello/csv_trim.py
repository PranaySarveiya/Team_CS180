import math
import os
import sys

numberOfRows = int(sys.argv[1])
path = os.path.abspath(os.path.dirname(__file__))

with open(path + "\\US_Accidents_Dec21_updated.csv", "r") as file:
    lines = file.readlines()



newFilename = "US_Accidents_" + str(numberOfRows) + "_rows.csv"
increment = math.floor(len(lines) / numberOfRows)
row = 1
count = 0
with open(path + "\\" + newFilename, "w+") as newFile:
    newFile.write(lines[0]) # Write header

    while (count <= numberOfRows):
            line = lines[row].split(",")
            del line[0] # Remove original index (A-######)
            line.insert(0, "A-" + str(count + 1))
            newFile.write(",".join(line)) # Re-join the list into a string of values separated by commas
            row += increment
            count += 1

    newFile.close()