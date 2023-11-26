import tkinter as tk
from tkinter import ttk
import customtkinter
from tktooltip import ToolTip
from PIL import Image, ImageTk
from CTkListbox import *
import guiController

#dictonary to store all the widgets

#specify root
root = customtkinter.CTk()
root.title("VA WorkStudy Time Sheets Calculator")

#set window size
window_width = 1000
window_height = 625
root.geometry(f"{window_width}x{window_height}")
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

#make window not resizable
root.resizable(False, False)

#window main title
mainTitleText = "VA Work Study\n Time Sheet Calculator"
mainTitleFont = ("Helvetica", 30, "bold")
mainTitleLabel =  customtkinter.CTkLabel(root, text=mainTitleText, font=mainTitleFont, justify='center', anchor='center')
mainTitleLabel.place(x=350, y=25)

#make a credientials frame
credentialsFrame = customtkinter.CTkFrame(master=root, width=300, height=60)

#place the credientials frame
credentialsFrame.place(x=30, y=125)

#credientials label
credentialsLabelText = "Credientals File Path"
credentialsLabelFont = ("Helvetica", 12, "bold")
credentialsLabel = customtkinter.CTkLabel(credentialsFrame, text=credentialsLabelText, font=credentialsLabelFont, anchor='center')

#make credientials text box
credentialsTextBoxFont = ("Helvetica", 12)
credentialsTextBox = customtkinter.CTkTextbox(credentialsFrame, width=275, height=8, border_width=4, corner_radius=2, font=credentialsTextBoxFont)

#place credientials label and text box
credentialsLabel.place(x=20, y=0)
credentialsTextBox.place(x=10, y=25)

#load info image button
infoButtonImage = Image.open('./guiImages/infoButton.png').resize((15,15))
infoButtonPhoto = customtkinter.CTkImage(infoButtonImage, size=(15, 15))

#info hover button for the image text box
credentialsInfoButton = customtkinter.CTkButton(credentialsFrame, image=infoButtonPhoto, text="", width=0, height=0, border_spacing=0, fg_color='transparent', hover=False)

credentialsInfoButtonText = 'Enter the file path to the credentials.json file'
ToolTip(credentialsInfoButton, msg=credentialsInfoButtonText, delay=0.01, follow=True,
        parent_kwargs={"bg": "#2A2827", "padx": 3, "pady": 3},
        fg="#C6C6C6", bg="#4D4948", padx=7, pady=7)

#place the button
credentialsInfoButton.place(x=135, y=3)




#frame for sheet name label and textbox
inputFrame = customtkinter.CTkFrame(master=root, width=300, height=400)

#place sheet frame
inputFrame.place(x=365, y=125)

#sheetNameFrame text box
sheetNameTextBoxFont = ("Helvetica", 12)
sheetNameTextBox = customtkinter.CTkTextbox(inputFrame, width=275, height=10, border_width=5, corner_radius=2, font=sheetNameTextBoxFont)

#sheetNameFrame label
sheetNameLabel = "Google Worksheet Name"
sheetNameLabelFont = ("Helvetica", 12, "bold")
sheetNameLabel =  customtkinter.CTkLabel(inputFrame, text=sheetNameLabel, font=sheetNameLabelFont, anchor='center')

#place within sheet frame
sheetNameLabel.place(x=20, y=0)
sheetNameTextBox.place(x=10, y=30)

#load info image button
infoButtonImage = Image.open('./guiImages/infoButton.png').resize((15,15))
infoButtonPhoto = customtkinter.CTkImage(infoButtonImage, size=(15, 15))

#info hover button for the image text box
sheetNameInfoButton = customtkinter.CTkButton(inputFrame, image=infoButtonPhoto, text="", width=0, height=0, border_spacing=0, fg_color='transparent', hover=False)

sheetNameInfoButtonButtonText = 'Enter the name of the google sheet'
ToolTip(sheetNameInfoButton, msg=sheetNameInfoButtonButtonText, delay=0.01, follow=True,
        parent_kwargs={"bg": "#2A2827", "padx": 3, "pady": 3},
        fg="#C6C6C6", bg="#4D4948", padx=7, pady=7)

#place the button
sheetNameInfoButton.place(x=162, y=3)

#startDate textBox
startDateTextBoxFont = ("Helvetica", 12)
startDateTextBox = customtkinter.CTkTextbox(inputFrame, width=275, height=10, border_width=5, corner_radius=2, font=startDateTextBoxFont)

#startDate TextBox label
startDateLabelText = "Start Date"
startDateLabelFont = ("Helvetica", 12, "bold")
startDateLabel =  customtkinter.CTkLabel(inputFrame, text=startDateLabelText, font=startDateLabelFont, anchor='center')

#place within sheet frame
startDateLabel.place(x=20, y=70)
startDateTextBox.place(x=10, y=100)

#load info image button
infoButtonImage = Image.open('./guiImages/infoButton.png').resize((15,15))
infoButtonPhoto = customtkinter.CTkImage(infoButtonImage, size=(15, 15))

#info hover button for the startDate text box
startDateInfoButton = customtkinter.CTkButton(inputFrame, image=infoButtonPhoto, text="", width=0, height=0, border_spacing=0, fg_color='transparent', hover=False)

startDateInfoButtonText = 'Enter the starting date of the sign in info you want to recieve in MM/DD/YYYY format'
ToolTip(startDateInfoButton, msg=startDateInfoButtonText, delay=0.01, follow=True,
        parent_kwargs={"bg": "#2A2827", "padx": 3, "pady": 3},
        fg="#C6C6C6", bg="#4D4948", padx=7, pady=7)

#place the button
startDateInfoButton.place(x=78, y=73)

#endDate textBox
endDateTextBoxFont = ("Helvetica", 12)
endDateTextBox = customtkinter.CTkTextbox(inputFrame, width=275, height=10, border_width=5, corner_radius=2, font=endDateTextBoxFont)

#endDate TextBox label
endDateLabelText = "End Date"
endDateLabelFont = ("Helvetica", 12, "bold")
endDateLabel =  customtkinter.CTkLabel(inputFrame, text=endDateLabelText, font=endDateLabelFont, anchor='center')

#place within sheet frame
endDateLabel.place(x=20, y=140)
endDateTextBox.place(x=10, y=170)

#load info image button
infoButtonImage = Image.open('./guiImages/infoButton.png').resize((15,15))
infoButtonPhoto = customtkinter.CTkImage(infoButtonImage, size=(15, 15))

#info hover button for the startDate text box
endDateInfoButton = customtkinter.CTkButton(inputFrame, image=infoButtonPhoto, text="", width=0, height=0, border_spacing=0, fg_color='transparent', hover=False)

endDateInfoButtonText = 'Enter the end date of the sign in info you want to recieve in MM/DD/YYYY format'
ToolTip(endDateInfoButton, msg=endDateInfoButtonText, delay=0.01, follow=True,
        parent_kwargs={"bg": "#2A2827", "padx": 3, "pady": 3},
        fg="#C6C6C6", bg="#4D4948", padx=7, pady=7)

#place the button
endDateInfoButton.place(x=72, y=143)

#total names text label
totalWorkStudyNamesLabelText = "WorkStudy Names"
totalWorkStudyNamesLabelFont = ("Helvetica", 12, "bold")
totalWorkStudyNamesLabel = customtkinter.CTkLabel(inputFrame, text=totalWorkStudyNamesLabelText, font=totalWorkStudyNamesLabelFont, anchor='center')

#totals name text box 
totalWorkStudyNamesTextBoxFont = ("Helvetica", 12, "bold")
totalWorkStudyNamesTextBox = customtkinter.CTkTextbox(inputFrame, width=275, height=140, border_width=5, corner_radius=2, font=totalWorkStudyNamesTextBoxFont)

#place within sheet fame
totalWorkStudyNamesLabel.place(x=20, y=210)
totalWorkStudyNamesTextBox.place(x=10, y=240)

#load info image button
infoButtonImage = Image.open('./guiImages/infoButton.png').resize((15,15))
infoButtonPhoto = customtkinter.CTkImage(infoButtonImage, size=(15, 15))

#info hover button for the total name text box
totalWorkStudyNamesInfoButton = customtkinter.CTkButton(inputFrame, image=infoButtonPhoto, text="", width=0, height=0, border_spacing=0, fg_color='transparent', hover=False)

totalWorkStudyNamesInfoButtonText = 'Enter Work Study names in the folowing format:\n (Last, First), (Last, First)'
ToolTip(totalWorkStudyNamesInfoButton, msg=totalWorkStudyNamesInfoButtonText, delay=0.01, follow=True,
        parent_kwargs={"bg": "#2A2827", "padx": 3, "pady": 3},
        fg="#C6C6C6", bg="#4D4948", padx=7, pady=7)

#place the button
totalWorkStudyNamesInfoButton.place(x=125, y=213)

#create workstudy nasme option menu frame
workStudyNameListBoxFrame = customtkinter.CTkFrame(master=root, width=300, height=400)

#place frame
workStudyNameListBoxFrame.place(x=35, y=125)

#Defime work study name listbox 
workStudyNamesListBox = CTkListbox(workStudyNameListBoxFrame, width=250, height=325)
#defime work studyListBoxLabel
workStudyNameListBoxLabelText = "Work Studies"
workStudyNameListBoxLabelFont = ("Helvetica", 12, "bold")
totalWorkStudyNamesLabel = customtkinter.CTkLabel(workStudyNameListBoxFrame, text=workStudyNameListBoxLabelText, font=workStudyNameListBoxLabelFont, anchor='center')

#place the work study name list box within the workStudyListBoxFrame
totalWorkStudyNamesLabel.place(x=20, y=2)
workStudyNamesListBox.place(x=10,y=30)


#load info image button
infoButtonImage = Image.open('./guiImages/infoButton.png').resize((15,15))
infoButtonPhoto = customtkinter.CTkImage(infoButtonImage, size=(15, 15))

#info hover button for the workStudy ListBox
workStudyListBoxInfoButton = customtkinter.CTkButton(workStudyNameListBoxFrame, image=infoButtonPhoto, text="", width=0, height=0, border_spacing=0, fg_color='transparent', hover=False)

workStudyListBoxInfoButtonText = 'Select one of the work study names below to display their total hours'
ToolTip(workStudyListBoxInfoButton, msg=workStudyListBoxInfoButtonText, delay=0.01, follow=True,
        parent_kwargs={"bg": "#2A2827", "padx": 3, "pady": 3},
        fg="#C6C6C6", bg="#4D4948", padx=7, pady=7)

#place button
workStudyListBoxInfoButton.place(x=97 ,y=5)


#create a resultFrame for the work study results 
resultFrame = customtkinter.CTkFrame(master=root, width=450, height=400)
#place result frame
resultFrame.place(x=525,y=125)


#Defime work study result list 
workStudyResultListBox = CTkListbox(resultFrame, width=395, height=325)

#define work studyListBoxLabel
workStudyResultListBoxLabelText = "Work Study Results"
workStudyResultListBoxLabelFont = ("Helvetica", 12, "bold")
WorkStudyResultListBoxLabel = customtkinter.CTkLabel(resultFrame, text=workStudyResultListBoxLabelText, font=workStudyResultListBoxLabelFont, anchor='center')

#place the work study name list box within the workStudyListBoxFrame
WorkStudyResultListBoxLabel.place(x=20, y=2)
workStudyResultListBox.place(x=10,y=30)

#create a label for workStudy Name
currentWorkStudyNameLabelText = ""
currentWorkStudyNameLabelFont = ("Helvetica", 12, "bold")
currentWorkStudyNameLabel = customtkinter.CTkLabel(resultFrame, text=currentWorkStudyNameLabelText, font=currentWorkStudyNameLabelFont, anchor='center')

#place the work study name label
currentWorkStudyNameLabel.place(x=200, y=1)

#make a cumulative hour frame
cumulativeHoursFrame = customtkinter.CTkFrame(master=root, width=135, height=60)

#place the cumulative hour frame
cumulativeHoursFrame.place(x=360, y=125)

#define cumulative Hour labe
cumulativeHoursLabelText = "Cumulative Hours"
cumulativeHoursLabelFont = ("Helvetica", 12, "bold")
cumulativeHoursLabel = customtkinter.CTkLabel(cumulativeHoursFrame, text=cumulativeHoursLabelText, font=cumulativeHoursLabelFont, anchor='center')

#define cumulative hour text box
cumulativeHoursTextBoxFont = ("Helvetica", 12, "bold")
cumulativeHoursTextBox = customtkinter.CTkTextbox(cumulativeHoursFrame, width=100, height=10, border_width=5, corner_radius=2, font=cumulativeHoursTextBoxFont)

#place the cumulative hour frame
cumulativeHoursLabel.place(x=14, y=0)
cumulativeHoursTextBox.place(x=14, y=25)

#create display button
displayButtonFont = ("Helvetica", 12, "bold")
displayButtonText = "Display"
displayButton = customtkinter.CTkButton(root, height=30, width=120, text=displayButtonText)

#place button
displayButton.place(x=365, y=200)

#load info image button
infoButtonImage = Image.open('./guiImages/infoButton.png').resize((15,15))
infoButtonPhoto = customtkinter.CTkImage(infoButtonImage, size=(15, 15))

#info hover button for the cumulative hours text box
cumulativeHoursInfoButton = customtkinter.CTkButton(cumulativeHoursFrame, image=infoButtonPhoto, text="", width=0, height=0, border_spacing=0, fg_color='transparent', hover=False)

cumulativeHoursInfoButtonText = 'Eneter the current work studies cumulative hours'
ToolTip(cumulativeHoursInfoButton, msg=cumulativeHoursInfoButtonText, delay=0.01, follow=True,
        parent_kwargs={"bg": "#2A2827", "padx": 3, "pady": 3},
        fg="#C6C6C6", bg="#4D4948", padx=7, pady=7)

cumulativeHoursInfoButton.place(x=115, y=3)

#load info image button
infoButtonImage = Image.open('./guiImages/infoButton.png').resize((15,15))
infoButtonPhoto = customtkinter.CTkImage(infoButtonImage, size=(15, 15))

#info hover button for the workStudy ListBox
workStudyResultListBoxInfoButton = customtkinter.CTkButton(resultFrame, image=infoButtonPhoto, text="", width=0, height=0, border_spacing=0, fg_color='transparent', hover=False)

workStudyResultListBoxInfoButtonText = 'Displays the currently selected work studies hours.'
ToolTip(workStudyResultListBoxInfoButton, msg=workStudyResultListBoxInfoButtonText, delay=0.01, follow=True,
        parent_kwargs={"bg": "#2A2827", "padx": 3, "pady": 3},
        fg="#C6C6C6", bg="#4D4948", padx=7, pady=7)

workStudyResultListBoxInfoButton.place(x=125 ,y=5)

#initalize widgest 
widgets = {}

#generate button
generateButtonFont = ("Helvetica", 12, "bold")
generateButtonText = "Generate"
generateButton = customtkinter.CTkButton(root, text=generateButtonText, command=lambda:guiController.generate(widgets))

#place button
generateButton.place(x=438, y=565)

#make a back button
backButtonFont = ("Helvetica", 12, "bold")
backButtonText = "Back"
backButton = customtkinter.CTkButton(root, text=backButtonText, command=lambda:guiController.backButtonClick())

#place button
backButton.place(x=30, y=75)

#puts all the widget in the widget dictonary 
widgets["root"] = root
widgets["mainTitleLabel"] = mainTitleLabel
widgets["sheetNameTextBox"] = sheetNameTextBox
widgets["sheetNameLabel"] = sheetNameLabel
widgets["sheetNameInfoButton"] = sheetNameInfoButton
widgets["startDateTextBox"] = startDateTextBox
widgets["startDateLabel"] = startDateLabel
widgets["startDateInfoButton"] = startDateInfoButton
widgets["endDateTextBox"] = endDateTextBox
widgets["endDateLabel"] = endDateLabel
widgets["endDateInfoButton"] = endDateInfoButton
widgets["totalWorkStudyNamesTextBox"] = totalWorkStudyNamesTextBox
widgets["totalWorkStudyNamesLabel"] = totalWorkStudyNamesLabel
widgets["totalWorkStudyNamesInfoButton"] = totalWorkStudyNamesInfoButton
widgets["workStudyNameListBoxFrame"] = workStudyNameListBoxFrame
widgets["workStudyNamesListBox"] = workStudyNamesListBox
widgets["workStudyListBoxInfoButton"] = workStudyListBoxInfoButton
widgets["workStudyResultListBox"] = workStudyResultListBox
widgets["workStudyResultListBoxInfoButton"] = workStudyResultListBoxInfoButton
widgets["resultFrame"] = resultFrame
widgets["credentialsTextBox"] = credentialsTextBox
widgets["credentialsInfoButton"] = credentialsInfoButton
widgets["credentialsLabel"] = credentialsLabel
widgets["generateButton"] = generateButton
widgets["cumulativeHoursTextBox"] = cumulativeHoursTextBox
widgets["cumulativeHoursLabel"] = cumulativeHoursLabel
widgets["displayButton"] = displayButton
widgets["inputFrame"] = inputFrame
widgets["credentialsFrame"] = credentialsFrame
widgets["cumulativeHoursFrame"] = cumulativeHoursFrame
widgets["backButton"] = backButton    
widgets["currentWorkStudyNameLabel"] = currentWorkStudyNameLabel

#hide every frame but the input frame and the credientials frame

workStudyNameListBoxFrame.place_forget()
resultFrame.place_forget()
cumulativeHoursFrame.place_forget()
displayButton.place_forget()
backButton.place_forget()

root.mainloop()