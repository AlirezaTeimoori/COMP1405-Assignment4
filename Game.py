'''
---------------------------------------
-- Created by:     Alireza Teimoori  --
-- Created on:     Nov 11 2019       --
-- Created for:    Assignment 4      --
-- Course Code:    COMP1405          --
-- Teacher Name:   Andrew Runka      --
---------------------------------------
-- This program scans a CSV file and --
-- using some functions makes use of --
-- the file to store and sort some   --
-- data and present them in some way --
---------------------------------------
'''

import csv # Importing required libraries

def readStats(filename): # Read a CSV file and returns a 2D list of the data

    try:
        with open(filename, "r") as file: # Create file with the input name to read
            string = file.read().split("\n")
            output = [] # Create an empty list
            for row in string:
                output.append(row.split(","))
        output.remove(output[0]); output.remove(output[-1]) # Remove the header row and last row which is empty
    except:
        print("Problem! The file does not exist!")
        return
    return output

def statsForPlayer(all, name): # Binary Search in the data to find player and return related data

    start = 0; end = len(all)-1 # Start and end points
    fullname = name.split(); first = fullname[0]; last  = fullname[1] # Split name

    while start <= end: # While in correct range

        middle   = (start + end) // 2 # find middle index
        midname  = all[middle][0]; print(midname)
        midfirst = all[middle][0].split()[0]
        midlast  = all[middle][0].split()[1]
        if midlast > last:
            end = middle - 1
            print(midname, last)
        elif midlast < last:
            start = middle + 1
            print(midname, last)
        elif midfirst > first:
            end = middle - 1
        elif midfirst < first:
            start = middle + 1
        else: return all[middle]

    print("Player not in list!")

def filterByPos(all, pos: str):

    output = []
    for row in all:
        if row[2] == pos:
            output.append(row)
    
    return output

def sortByPoints(all):

    output = [x[:] for x in all]

    for element_index in range(len(output)):

        min_index = element_index

        for next_element in range(element_index+1, len(output)):

            if int(output[min_index][6]) > int(output[next_element][6]):
                min_index = next_element

        output[element_index], output[min_index] = output[min_index], output[element_index]

    file = open("test.csv", "w+")
    out = ""
    for i in output:
        for j in i:
            out += f"{j},"
        out += "\n"
    file.write(str(out))
    file.close()
    return output
    
def buildBestTeam(all):

    lst = sortByPoints(all)
    bestTeam = []
    positions = ["D", "D", "LW", "RW", "C"]
    for player in reversed(lst):
        if player[2] in positions:
            bestTeam.append(player[0])
            positions.pop(positions.index(player[2]))

    output = ""
    for i in bestTeam: output += f"{i}\n"
    try:
        with open("best.txt", "w+") as file:
            file.write(output)
    except:
        print("ERROR!")

print(*sortByPoints(readStats("nhl_2018.csv")), sep = "\n")
print(buildBestTeam(readStats("nhl_2018.csv")))
