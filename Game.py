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
            reader = csv.reader(file) # Create a variable as CSV reader
            output = [] # Create an empty list
            for row in reader: # for each row in the data
                output.append(row) # append that row as a list to our empty list
        output.remove(output[0]) # Remove the header row
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

def sortByPoints():

    
print(*filterByPos(readStats("nhl_2018.csv"), "LP"), sep = "\n")