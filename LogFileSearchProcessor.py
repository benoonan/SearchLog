# The purpose of this script is to act as the body for the rest of the program.
import os
import sys
import PySimpleGUI as sg

sg.theme('DarkAmber')  # Add a touch of color
# All the stuff inside your window.
layout = [[sg.Text(' ')],
          # Input the path to the file to process.
          [sg.Text('Enter the full path of your file (including the file name at the end):'),
           sg.InputText()],
          # Input the path to spit out the output files.
          [sg.Text('Enter the path to output the processed file with a back slash at the end.'),
           sg.InputText()],
          # Input the path to spit out the output files.
          [sg.Text('Enter the name of the test location.'),
           sg.InputText()],
          # Input the path to spit out the output files.
          [sg.Text('Enter the name of the test (BER or RSSI).'),
           sg.InputText()],
          [sg.Button('Ok'), sg.Button('Cancel')]]

# Create the Window
window = sg.Window('Record Searcher', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':  # if user closes window or clicks cancel
        break

    user_input = values[0]  # User inputs the file to be processed.
    DirName = values[1]  # Input the output directory.
    Filename = values[2]  # Input the user defined name.
    TestType = values[3]  # Input the user defined test name.

    # Filenames are created from the user input
    MrkrFilename = DirName + Filename + "Markers.csv"
    TestFilename = DirName + Filename + TestType + ".csv"

    # Opens the existing file
    assert os.path.exists(user_input), "I did not find the file at, " + str(user_input)
    path = open(user_input, 'r+')

    # Gets the maximum lines of the input files
    Lines = path.readlines()
    LineTotal = len(Lines)

    # Shows you can read the values of the window and modify them.
    print(user_input)
    print(DirName)
    print(MrkrFilename)
    print(TestFilename)

    # Creates the output files
    Markers = open(MrkrFilename, 'w')
    TestFile = open(TestFilename, 'w')

    # Initializes the record indicators
    Rec: str = '#'  # Marker Record
    BERRec: str = 'B'  # BER Record
    RSSIRec: str = 'R'  # RSSI Record
    EmptyRec: str = '\n'  # Empty Record


    def checkRec(rnum, lst, cont):

        while cont:

            Nrow = lst[rnum]  # Initializes to the next row in the list.
            if Nrow.find(BERRec, 0, 1) != -1:  # If the next line is a BER record, write it to the file.

                with open(TestFilename, 'a') as file:
                    file.write(lst[rnum])
                cont = False  # Stop the Loop

            elif Nrow.find(RSSIRec, 0, 1) != -1:  # If the next line is a RSSI record, write it to the file.

                with open(TestFilename, 'a') as file:
                    file.write(lst[rnum])
                cont = False  # Stop the Loop

            elif Nrow.find(Rec, 0, 1) != -1:  # If the next line is a marker record, write a space to the file.

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

window.close()
