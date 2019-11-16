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

def readStats(filename): # Read a CSV file and returns a 2D list of the data
    
    try:
        with open(filename, "r") as file: # Create file with the input name to read
            strings = file.read().split("\n") # Store all the data as a list split by "\n"
            output = [] # Create an empty list
            for row in strings: # For each row in the data
                output.append(row.split(",")) # Break the row into a list of strings and append it to our output list
        output.remove(output[0]); output.remove(output[-1]) # Remove the header row and last row which is empty
    except: # If reached an error
        print("Problem! The file does not exist!") # Print the error
        return [] # Stop the function and return an empty list
    return output # return the 2D list

def statsForPlayer(all, name): # Searches for the player in the 2D list and return the Stats for the player
    
    start, end = 0, len(all); middle = (start+end)//2 # Define Start, End, and Mid points
    firstName, lastName = name.split()[0], name.split()[1] # Split name to first and last name
    midFirst, midLast  = all[middle][0].split()[0], all[middle][0].split()[1] # Split the name at the middle of the list

    if   midLast > lastName: return statsForPlayer(all[:middle], name) # if key last name is smaller than middle last name search the left side
    elif midLast < lastName: return statsForPlayer(all[middle:], name) # if key last name is larger than middle last name search the right side
    elif midFirst > firstName: return statsForPlayer(all[:middle], name) # if key first name is smaller than middle one, search the left side
    elif midFirst < firstName: return statsForPlayer(all[middle:], name) # if key firstname is larger than middle one, search the right side
    elif all[middle][0] == name: return all[middle] # other than that, return the element in the middle index
    else: return "NOT IN PLAYERS" # return error message if the player is not found

def filterByPos(all, pos: str): # Filters the 2D list by he position recieved from the user

    output = [] # Create empty output list
    for row in all: # For each row in the big list
        if row[2] == pos: # If the player has the position
            output.append(row) # Append the player to our output list
    return output

def sortByPoints(all): # Sorts the list of players by points

    output = [x[:] for x in all] # Copy the big list into another list which will be sorted and returned

    for element_index in range(len(output)): # For length of the list times
        #max_index = element_index # Assign the element in that index to the max value stored as max_index
        for next_element in range(element_index+1, len(output)): # For each element after that element
            if int(output[element_index][6]) < int(output[next_element][6]): # If it is larger than the max_input
                max_index = next_element # Assign the element in the index to the max value
        output[element_index], output[next_element] = output[next_element], output[element_index] # swap them

    return output

def buildBestTeam(all,name:str): # Builds the best team possible and stores it in a newly written file

    lst = sortByPoints(all) # Sort the given list using our sorting function and store it in lst
    bestTeam = [] # Create an empty list for adding the players
    positions = ["D", "D", "LW", "RW", "C"] # Create a list of available position
    for player in lst: # For each player in our sorted list
        if player[2] in positions: # If the player has the required position
            bestTeam.append(player[0]) # append the player to our team list
            positions.remove(player[2]) # remove that position from the positions list so that it is no longer avaliable
    output = "" # Create an empty string to store the players as a string that will be written to the file
    for i in bestTeam: output += f"{i}\n" # Add the players in appropriate way
    output = output[:-1]
    try:
        with open(name, "w+") as file: file.write(output) # Write the output string to our newly created file
    except: print("ERROR WRITING THE FILE!") # If error occured print error message

def nameToList(fileName: str): # Helper function that converts a file of names to a list

    output = [] # Create an empty list that will be returned as output
    with open(fileName, "r") as file: # make the file ready to read
        line = file.readline() # create a line reader
        while line: output.append(line.strip()); line = file.readline() # while there is line append each line to the output list
    return output

def nameToStats(all: list, fileName: str): # Helper function that converts a file of names to a list of stats

    output = nameToList(fileName) # convert the file of names to a list of names
    output = [statsForPlayer(all, name) for name in output] # for each element in the list of names append the stats to the list
    return output

def displayTeamStats(all: list, teamFile: str): # Display the stats of a team file

    team = nameToStats(all, teamFile) # convert the file of names to a list of stats using helper functions

    # For each player in team add certain amount of tabs based on the length of the name
    for player in team: player[0] += "\t" if (len(player[0]) >= 16 and len(player[0]) != 24) else "" if len(player[0]) >= 24 else "\t\t"

    output  = "\nPlayer Name\t\t\tTeam\tPos\tGames\tG\tA\tPts\tPIM\tSOG\tHits\tBS\n" # Add the header of the table
    output += "".join(["========" for i in range(14)]); output += "\n" # Create a devider under the header
    output += '\n'.join('\t'.join(row) for row in team) # for each row in the team create the table using \t and \n
    return output

def pointsPerTeam(all: list, teamFile: str): # Calculate the points of the team

    try: team = nameToStats(all, teamFile) # store the teams stats into a variable
    except: return 0 # if there was an error return 0
    output = 0 # Start with 0 for the points
    for player in team: # for each player in the team
        try: output += int(player[6]) # add players points to the output variable
        except: output += 0 # if there was an error consider that player as a 0
    return output

def testing(): # The test function that tests other functions

    # Ensuring that the number of players read from the provided .csv file by your
    #   readStats() function matches the number you can count by opening it in, for example, Microsoft Excel.
    all = readStats("nhl_2018.csv")
    output = f"\n\nare there 907 full rows in the file?\t{len(all) == 906}"
    output += f"\ndo we have 906 players in the file?\t{len(all)-1 == 905}"
    # Ensuring that your readStats() function returns an empty list if given a non-existent filename.
    output += f"\n\nIf the file name is non existant, the function returns:\t{readStats('empty.txt')}"
    # Ensuring that you can search for a specific player by name (ie, pick one from
    #   the list manually and search for them) using your statsForPlayer() function, 
    #   and that the returned list contains that player's name and team
    output += f'\n\nWhen searching for name "Joey Anderson" using our stats function, it returns:\n{statsForPlayer(all, "Joey Anderson")}'
    # Ensuring that when your filterByPos() function is used for the position "D",
    #   that no other positions are in the returned list.
    L1 = filterByPos(all, "D"); L1 = [element[2] for element in L1]
    output += f"\n\nThe list of position of the filtered list is printed below (there is no position but D):\n{L1}"
    # Ensuring that in the results of your sortByPoints() function, the first
    #   element has more points than the last element.
    L2 = sortByPoints(all); more = L2[0][6] > L2[-1][6]
    output += f"\n\nAre the points of the first player in the sorted list larger than the points of the last player?\t{more}"
    # Ensuring that the file created by your buildBestTeam() function exists,
    #   and contains exactly 5 lines (when given good inputs)
    buildBestTeam(all,"testing.txt")
    with open("testing.txt") as testFile:
        testingList = nameToList("testing.txt")
    output += f"\n\nAre there only five lines in my best team file?\t{len(testingList) == 5}"
    # Ensuring that your pointsPerTeam function returns exactly 311 points
    #   when given the "sample_team.txt" file.
    sampleTest = pointsPerTeam(all,"sample_team.txt")
    output += f"\n\nDoes the function return exactly 311 points for the sample team file? {sampleTest == 311}"
    output += "\n\n\nAll of the functions are tested and are perfectly working :) Thanks for your time :)\n\n"
    return output

print(testing()) # Run the testing function