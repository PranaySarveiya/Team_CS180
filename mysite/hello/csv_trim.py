import math
import time
import os
import sys

numberOfRows = int(sys.argv[1])

with open("US_Accidents_Dec21_updated.csv", "r") as file:
    lines = file.readlines()



newFilename = "US_Accidents_Dec21_updated_deletethisendpart.csv"
with open(newFilename, "w+") as newFile:
    for line in lines:
        if(numberOfRows >= 0):
            newFile.write(line)
            numberOfRows -= 1
        else:
            break