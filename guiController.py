

def collect():
    sheet_name = sheetNameTextBox.get("0.0", "end-1c")
    start_date = startDateTextBox.get("0.0", "end-1c")
    end_date = endDateTextBox.get("0.0", "end-1c")
    total_work_study_names = totalWorkStudyNamesTextBox.get("0.0", "end-1c")
    print("Sheet Name: " + sheet_name)
    print("Start Date: " + start_date)
    print("End Date: " + end_date)
    print("Total Work Study Names: " + total_work_study_names)

# this function initalizes widgets
def generate(widgets):
    global root, mainTitleLabel, sheetNameTextBox, sheetNameLabel, sheetNameInfoButton
    global startDateTextBox, startDateLabel, startDateInfoButton
    global endDateTextBox, endDateLabel, endDateInfoButton
    global totalWorkStudyNamesTextBox, totalWorkStudyNamesLabel, totalWorkStudyNamesInfoButton
    global workStudyNamesListBox, workStudyListBoxInfoButton
    global workStudyResultListBox, workStudyResultListBoxInfoButton
    global generateButton
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
    collect()
