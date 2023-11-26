import workStudySheetsReader

#this function collects all the data from the gui and sends it to the main function in python
def collect():
    sheet_name = sheetNameTextBox.get("0.0", "end-1c")
    start_date = startDateTextBox.get("0.0", "end-1c")
    end_date = endDateTextBox.get("0.0", "end-1c")
    total_work_study_names = totalWorkStudyNamesTextBox.get("0.0", "end-1c")
    credentials_filename = credentialsTextBox.get("0.0", "end-1c")


    sheet_name = "Copy of 2023 Fall Semester Shift Sign-in Sheet, 10/30"
    start_date = "10/16/2023"
    end_date = "10/27/2023"
    total_work_study_names = "(Mills, Marissa), (Butera, Salvatore), (Cancel, David), (Etyang, Arthur), (Godbey, Kaelyn), (Gomez, Kenny), (Ibarra, Christyanna), (Landes, Mahlon), (Mendoza, Vanessa), (Mihaileanu, George), (Nosike, Austin), (Pembleton, Aidan), (Potter, Chandler), (Quartey, Eric), (Ramirez, Jose), (Rodas, Melvin), (Rojas, Roberto), (Sandoval, Edwin), (Simons, Emma), (Tenet, Brooke), (West, Sydney), (Angelina, Zubricki)"
    credentials_filename = r"C:\Users\slopo\OneDrive\Desktop\firm-champion-381221-a86377f468ed.json"
    #collect the data from the gui and send it to the main function in python
    getTheHoursOfEveryWorkStudy(credentials_filename, sheet_name, total_work_study_names, start_date, end_date)

#this function gets the hours of every work study from the main function in python
def getTheHoursOfEveryWorkStudy(credentials_filename, sheet_name, total_work_study_names, start_date, end_date):
    workStudy_names_dict, worksheet_names = workStudySheetsReader.find_hours_in_all_sheets_for_all_names(credentials_filename, sheet_name, total_work_study_names, start_date, end_date)
    #now that the data is collected we just need to control clicks on the gui
    control(workStudy_names_dict, worksheet_names)
    

#this function populates the workStudyNamesListBox with the names of the work studies
def putAllTheNamesInTheListBox(workStudy_names_dict):
    iter = 0
    for name in workStudy_names_dict:
        workStudyNamesListBox.insert(iter, name)
        iter += 1

#put the hours of the currently selected work study in the workStudyResultListBox
def displayButtonClick(workStudy_names_dict, worksheet_names):
    #get the name of the currently selected work study
    currentName = workStudyNamesListBox.get(workStudyNamesListBox.curselection())
    #get the cumulative hours of the currently selected work study
    cumulative_hours = cumulativeHoursTextBox.get("0.0", "end-1c")
    #delete the cumulative hours from the textbox
    cumulativeHoursTextBox.delete("0.0", "end")
    #set the curremt work study name label
    currentWorkStudyNameLabel.configure(text=currentName)
    #get the currently selected workstudies hours
    listOfDailyHours = convertWorkStudyNametoWorkStudyHours(workStudy_names_dict, currentName, worksheet_names, cumulative_hours)
    #clear the workStudyResultListBox
    if (workStudyResultListBox.size() > 0):
        workStudyResultListBox.delete(0, workStudyResultListBox.size())
    iter = 0
    for day in listOfDailyHours:
        workStudyResultListBox.insert(iter, day)
        iter += 1
        

def convertWorkStudyNametoWorkStudyHours(workStudy_names_dict, currentName, worksheet_names, cumulative_hours):
    WS_hour_dict = workStudy_names_dict[currentName]
    cumulative_hours = float(cumulative_hours)
    listOfHours = []
    for date in worksheet_names:
        if(date in WS_hour_dict):
            hours_for_day = WS_hour_dict[date]
            cumulative_hours = cumulative_hours + hours_for_day
            dateHours = "Date: " + str(date) + " Hours: " + str(hours_for_day) + " Cumulative Hours: " + str(cumulative_hours)
            listOfHours.append(dateHours)
        else:
            continue
    return listOfHours
    
def backButtonClick():
    #CLEAR WS LIST BOX
    if (workStudyResultListBox.size() > 0):
        workStudyResultListBox.delete(0, workStudyResultListBox.size())
    #CLEAR CUMULATIVE HOURS TEXT BOX
    cumulativeHoursTextBox.delete("0.0", "end")
    #CLEAR CURRENT WORK STUDY NAME LABEL
    currentWorkStudyNameLabel.configure(text="")
    #CLEAR WORK STUDY NAME LIST BOX
    if (workStudyNamesListBox.size() > 0):
        workStudyNamesListBox.delete(0, workStudyNamesListBox.size())
    workStudyNameListBoxFrame.place_forget()
    resultFrame.place_forget()
    cumulativeHoursFrame.place_forget()
    displayButton.place_forget()
    backButton.place_forget()
    inputFrame.place(x=365, y=125)
    credentialsFrame.place(x=30, y=125)
    generateButton.place(x=438, y=565)





def control(workStudy_names_dict, worksheet_names):
    #populate the listbox with the names
    putAllTheNamesInTheListBox(workStudy_names_dict)
    #when the display button is clicked
    displayButton.configure(state="normal")
    displayButton.configure(command=lambda: displayButtonClick(workStudy_names_dict, worksheet_names))

# this function initalizes widgets
def generate(widgets):
    global root, mainTitleLabel, sheetNameTextBox, sheetNameLabel, sheetNameInfoButton
    global startDateTextBox, startDateLabel, startDateInfoButton
    global endDateTextBox, endDateLabel, endDateInfoButton
    global totalWorkStudyNamesTextBox, totalWorkStudyNamesLabel, totalWorkStudyNamesInfoButton
    global workStudyNamesListBox, workStudyListBoxInfoButton
    global workStudyResultListBox, workStudyResultListBoxInfoButton
    global generateButton
    global credentialsTextBox, credentialsLabel, credentialsInfoButton
    global cumulativeHoursTextBox, cumulativeHoursTextBox
    global displayButton
    global resultFrame, workStudyNameListBoxFrame, inputFrame, credentialsFrame
    global backButton, cumulativeHoursFrame
    global currentWorkStudyNameLabel
    cumulativeHoursTextBox = widgets["cumulativeHoursTextBox"]
    cumulativeHoursLabel = widgets["cumulativeHoursLabel"]
    credentialsTextBox = widgets["credentialsTextBox"]
    credentialsInfoButton = widgets["credentialsInfoButton"]
    credentialsLabel = widgets["credentialsLabel"]
    root = widgets["root"]
    mainTitleLabel = widgets["mainTitleLabel"]
    sheetNameTextBox = widgets["sheetNameTextBox"]
    sheetNameLabel = widgets["sheetNameLabel"]
    sheetNameInfoButton = widgets["sheetNameInfoButton"]
    startDateTextBox = widgets["startDateTextBox"]
    startDateLabel = widgets["startDateLabel"]
    startDateInfoButton = widgets["startDateInfoButton"]
    endDateTextBox = widgets["endDateTextBox"]
    endDateLabel = widgets["endDateLabel"]
    endDateInfoButton = widgets["endDateInfoButton"]
    totalWorkStudyNamesTextBox = widgets["totalWorkStudyNamesTextBox"]
    totalWorkStudyNamesLabel = widgets["totalWorkStudyNamesLabel"]
    totalWorkStudyNamesInfoButton = widgets["totalWorkStudyNamesInfoButton"]
    workStudyNamesListBox = widgets["workStudyNamesListBox"]
    workStudyListBoxInfoButton = widgets["workStudyListBoxInfoButton"]
    workStudyResultListBox = widgets["workStudyResultListBox"]
    workStudyResultListBoxInfoButton = widgets["workStudyResultListBoxInfoButton"]
    generateButton = widgets["generateButton"]
    displayButton = widgets["displayButton"]
    resultFrame = widgets["resultFrame"] 
    workStudyNameListBoxFrame = widgets["workStudyNameListBoxFrame"]
    inputFrame = widgets["inputFrame"]
    credentialsFrame = widgets["credentialsFrame"]
    cumulativeHoursFrame = widgets["cumulativeHoursFrame"]
    backButton = widgets["backButton"]
    currentWorkStudyNameLabel = widgets["currentWorkStudyNameLabel"]
    #forget the first screen widgets
    inputFrame.place_forget()
    credentialsFrame.place_forget()
    generateButton.place_forget()
    #place the second screen widgets
    workStudyNameListBoxFrame.place(x=35, y=125)
    resultFrame.place(x=525,y=125)
    cumulativeHoursFrame.place(x=360, y=125)
    displayButton.place(x=365, y=200)
    backButton.place(x=35, y=70)


    collect()
