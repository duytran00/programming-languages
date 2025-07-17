#Duy Tran
#1002190361
#python 3.12.3
#Ubuntu

import os
import sys

def calculateDirectory(folder):

    total = 0
    
    #List of all entries to get info
    entries = os.listdir(folder)

    for entry in entries:
        
        if entry in [".", ".."]:
            continue
        
        #Sim to snprintf but better. Combines folder path with file
        filePath = os.path.join(folder, entry)
        
        if os.path.isdir(filePath):
            total += calculateDirectory(filePath)
        else:
            total += os.path.getsize(filePath)
     
    return total


if __name__ == "__main__":

    #directory = sys.argv[1]
    size = calculateDirectory(".")

    sys.stdout.write(str(size))

    #$ python3 dxt0361_lab01.py .
    #$ python3 dxt0361_lab01.py testdir