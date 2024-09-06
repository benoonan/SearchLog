import sys
import os

# User inputs the file to be processed.
user_input = input("Enter the full path of your file (including the file name at the end): ")

# User defines the output folder and filenames
DirName = input("Enter the name of the file directory to save the files: ")
Filename = input("Enter a meaningful name to create output files: ")
TestType = input("Enter the test type: ")

# Filenames are created from the user input
MrkrFilename = DirName + Filename + "markers.csv"
TestFilename = DirName + Filename + TestType + ".csv"

# Opens the existing file
assert os.path.exists(user_input), "I did not find the file at, " + str(user_input)
path = open(user_input, 'r+')

# Gets the maximum lines of the input files
Lines = path.readlines()
LineTotal = len(Lines)

# Creates the output files
Markers = open(MrkrFilename, 'x')
TestFile = open(TestFilename, 'x')

# Initializes the record indicators
Rec: str = '#'  # Marker Record
BERRec: str = 'B'  # BER Record
RSSIRec: str = 'R'  # RSSI Record
EmptyRec: str = '\n'  # Empty Record


def checkRec(rnum, lst, cont):

    while cont:

        Nrow = lst[rnum]  # Initializes to the next row in the list.
        if Nrow.find(BERRec) != -1:  # If the next line is a BER record, write it to the file.

            with open(TestFilename, 'a') as file:
                file.write(lst[rnum])
            cont = False  # Stop the Loop

        elif Nrow.find(RSSIRec) != -1:  # If the next line is a RSSI record, write it to the file.

            with open(TestFilename, 'a') as file:
                file.write(lst[rnum])
            cont = False  # Stop the Loop

        elif Nrow.find(Rec) != -1:  # If the next line is a marker record, write a space to the file.

            with open(TestFilename, 'a') as file:
                file.write(EmptyRec)
            cont = False  # Stop the Loop

        else:

            rnum += 1  # Continue the loop if no matching records have been found.


IsMrkr = False  # Is there a '#' marker placed in the log file?
rNumb = 0  # Row Number

for row in Lines:

    if row.find(Rec) != 0:  # Basically searches for the '#' entry.
        IsMrkr = False

    else:  # Checks for the Markers and writes them to a file

        IsMrkr = True
        with open(MrkrFilename, 'a') as file:  # Appends the row to the file.
            file.write(row)

        nxtRec = rNumb + 1  # Keeps track of the next entry.
        if nxtRec > LineTotal:
            pass

        else:
            checkRec(nxtRec, Lines, IsMrkr)

    rNumb += 1  # keeps track of the current line

path.close()
Markers.close()
TestFile.close()
