import PySimpleGUI as pg
import os

#Step 1: Set Theme
pg.theme("default1")

#Step 2: Create Layout
file_list_column = [
    [
        pg.Text("Select CSV File"), 
        pg.In(size=(30,1), enable_events = True, key="-Folder-"), 
        pg.FileBrowse(), 
    ]
]

file_viewer_column = [
    [
        pg.Text("Enter Client Code: ", size = (15,1)),
        pg.InputText(do_not_clear=False)
    ],
    [
        pg.Text("Enter Site Code: ", size = (15,1)),
        pg.InputText(do_not_clear=False)
    ],
    [
        pg.Text("Enter MQTT Topic: ", size = (15,1)),
        pg.InputText(do_not_clear=False)
    ],
    [
        pg.Text("Enter Censor Name: ",size = (15,1)),
        pg.InputText(do_not_clear=False)
    ],
    [   
        pg.Text("Enter Client ID: ", size = (15,1)), 
        pg.InputText(do_not_clear=False)
    ],
    [
        pg.Button("OK"),
        pg.Button("Close")
    ],
]

layout = [
    [   
        pg.Column(file_list_column),       
        pg.VSeperator(),  
        pg.Column(file_viewer_column) 
    ]
]
   
#Step 3: Create Window
window = pg.Window("Form", layout )

#Step 4: Event Loop
while True:
    event, values = window.read()

    if event == pg.WIN_CLOSED or event == "Close":
        break
    elif event == "-FOLDER-":
        folder_location = values ["-FOLDER-"]
        try:
            file_names = os.listdir(folder_location)
        
        except:
            files = []

        file_names = [
            file for file in files
            if os.path.isfile(os.path.join(folder_location, file))
            and file.lower().endswith((".csv"))
        ]
        window["-FILE_LIST-"].update(file_names)

    elif event == "OK":
        print(f"Client Code: {values[1]}")
        print(f"Site Code: {values[2]}")
        print(f"MQTT Topic: {values[3]}")
        print(f"Censor Name: {values[4]}")
        print(f"Client ID: {values[5]}")

    for item in values:
        values[item] = None

#Step 5: Close Window
window.close()





