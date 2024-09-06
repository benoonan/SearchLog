# The purpose of this script is to act as the body for the rest of the program.
import os
import sys
import PySimpleGUI as sg
from PySimpleGUI import one_line_progress_meter

# I probably need to clean this Window up and make it a class or something like that.


def app_window(theme):
    sg.theme(theme)
    menu_def = [['&Application', ['E&xit']],
                ['&Help', ['&About']]]
    right_click_menu_def = [[], ['Edit Me', 'Versions', 'Nothing', 'More Nothing', 'Exit']]
    graph_right_click_menu_def = [[], ['Erase', 'Draw Line', 'Draw', ['Circle', 'Rectangle', 'Image'], 'Exit']]

    # Table Data
    data = [["John", 10], ["Jen", 5]]
    headings = ["Name", "Score"]

    input_layout = [

        # [sg.Menu(menu_def, key='-MENU-')],
        [sg.Text('Anything that requires user-input is in this tab!')],
        [sg.Input(key='-INPUT-')],
        [sg.Multiline(
            'Demo of a Multi-Line Text Element!\nLine 2\nLine 3\nLine 4\nLine 5\nLine 6\nLine 7\nYou get the point.',
            size=(45, 5), expand_x=True, expand_y=True, k='-MLINE-')],
        [sg.Button('Button'), sg.Button('Popup'), sg.Button(image_data=sg.DEFAULT_BASE64_ICON, key='-LOGO-')]]

    asthetic_layout = [[sg.T('Anything that you would use for asthetics is in this tab!')],
                       [sg.Image(data=sg.DEFAULT_BASE64_ICON, k='-IMAGE-')],
                       [sg.ProgressBar(100, orientation='h', size=(20, 20), key='-PROGRESS BAR-'),
                        sg.Button('Test Progress bar')]]

    logging_layout = [[sg.Text("Anything printed will display here!")],
                      [sg.Multiline(size=(60, 15), font='Courier 8', expand_x=True, expand_y=True, write_only=True,
                                    reroute_stdout=True, reroute_stderr=True, echo_stdout_stderr=True, autoscroll=True,
                                    auto_refresh=True)]
                      # [sg.Output(size=(60,15), font='Courier 8', expand_x=True, expand_y=True)]
                      ]

    graphing_layout = [[sg.Text("Anything you would use to graph will display here!")],
                       [sg.Graph((200, 200), (0, 0), (200, 200), background_color="black", key='-GRAPH-',
                                 enable_events=True,
                                 right_click_menu=graph_right_click_menu_def)],
                       [sg.T('Click anywhere on graph to draw a circle')],
                       [sg.Table(values=data, headings=headings, max_col_width=25,
                                 background_color='black',
                                 auto_size_columns=True,
                                 display_row_numbers=True,
                                 justification='right',
                                 num_rows=2,
                                 alternating_row_color='black',
                                 key='-TABLE-',
                                 row_height=25)]]

    popup_layout = [[sg.Text("Popup Testing")],
                    [sg.Button("Open Folder")],
                    [sg.Button("Open File")]]

    theme_layout = [[sg.Text("See how elements look under different themes by choosing a different theme here!")],
                    [sg.Listbox(values=sg.theme_list(),
                                size=(20, 12),
                                key='-THEME LISTBOX-',
                                enable_events=True)],
                    [sg.Button("Set Theme")]]

    layout = [[sg.MenubarCustom(menu_def, key='-MENU-', font='Courier 15', tearoff=True)],
              [sg.Text('Demo Of (Almost) All Elements', size=(38, 1), justification='center', font=("Helvetica", 16),
                       relief=sg.RELIEF_RIDGE, k='-TEXT HEADING-', enable_events=True)]]
    layout += [[sg.TabGroup([[sg.Tab('Input Elements', input_layout),
                              sg.Tab('Asthetic Elements', asthetic_layout),
                              sg.Tab('Graphing', graphing_layout),
                              sg.Tab('Popups', popup_layout),
                              sg.Tab('Theming', theme_layout),
                              sg.Tab('Output', logging_layout)]], key='-TAB GROUP-', expand_x=True, expand_y=True),

                ]]
    layout[-1].append(sg.Sizegrip())
    window = sg.Window('All Elements Demo', layout, right_click_menu=right_click_menu_def,
                       right_click_menu_tearoff=True, grab_anywhere=True, resizable=True, margins=(0, 0),
                       use_custom_titlebar=True, finalize=True, keep_on_top=True)
    window.set_min_size(window.size)
    return window

sg.theme('SystemDefaultForReal')  # Add a touch of color
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
          [sg.Button('Process'), sg.Button('Close')]]



asthetic_layout = [[sg.T('Anything that you would use for asthetics is in this tab!')],
                       [sg.ProgressBar(100, orientation='h', size=(20, 20), key='-PROGRESS BAR-'),
                        sg.Button('Test Progress bar')]]

###################################################################################################

# Create the Window
window = sg.Window('Search Log File', layout)

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Close':  # if user closes window or clicks cancel
        break

    user_input = values[0]  # User inputs the file to be processed.
    DirName = values[1]  # Input the output directory.
    Filename = values[2]  # Input the user defined name.
    TestType = values[3]  # Input the user defined test name.

    # Filenames are created from the user input
    MrkrFilename = DirName + Filename + "Markers.csv"
    TestFilename = DirName + Filename + TestType + ".csv"

    IsPath = os.path.exists(user_input)

    #if IsPath = False:
        #while IsPath = False:
        # I need to have the window change the message to prompt the user to put in the correct path.


    # Terminates the code if the path is incorrect,
    assert os.path.exists(user_input), "I did not find the file at, " + str(user_input)

    # Opens the existing file
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

    progress_bar = window['-PROGRESS BAR-']

    for row in Lines:
        # progress_bar.update(current_count=rNumb + 1)
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
