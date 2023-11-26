import re
import gspread
import time
from datetime import date, datetime, timedelta
import calendar
import numpy as np
from tqdm import tqdm
  





def set_names_to_standard(worksheet_list_of_lists):
    for x in range(6,len(worksheet_list_of_lists)):
        curr_last_name = str(worksheet_list_of_lists[x][0])
        if(curr_last_name == None):
            continue
        curr_last_name = curr_last_name.replace(" ", "")
        curr_last_name = curr_last_name.lower()
        curr_last_name = curr_last_name.capitalize()
        worksheet_list_of_lists[x][0] = curr_last_name
        curr_first_name = str(worksheet_list_of_lists[x][1])
        if(curr_first_name == None):
            continue
        curr_first_name = curr_first_name.replace(" ", "")
        curr_first_name = curr_first_name.lower()
        curr_first_name = curr_first_name.capitalize()
        worksheet_list_of_lists[x][1] = curr_first_name




def get_hour_value_for_day(locations_of_name, worksheet_list_of_lists):
    hours = []
    #print("here is the cell list")
    #print(cell_list)
    for x in locations_of_name:
        row = x[0]
        col = x[1]
        val = str(worksheet_list_of_lists[row][col+4])
        if len(val) == 4:
            hour = val[0:1]
            min = val[2:]
        elif len(val) == 5:
            hour = val[0:2]
            min = val[3:]
        if(min == "30"):
            min = 0.5
        elif(min == "00"):
            min = 0.0
        else:
            print("\n\n\n minuet time is " + min)
            print("Hours: " + hour + "mins: " + min)
            print("row: " + str(row) + "col: " + str(col))
            print("error invalid minute time")
    
        total_time = float(min) + float(hour)
        hours.append(total_time)
    total_hours = sum(hours)
    return total_hours


def get_indexs_of_name(name, worksheet_list_of_lists):
    location_of_names = []
    for i in range(0, len(worksheet_list_of_lists)):
        if (str(worksheet_list_of_lists[i][0]) + (", ") + str(worksheet_list_of_lists[i][1])) == name:
            location_of_names.append((i, 0))
    return location_of_names
    

#this function takes in a date object and returns a string in MM/DD/YYYY format
def dateType_to_dateString(date):
    formatted_date = date.strftime("%m/%d/%Y")
    return formatted_date


def time_sheet_for_name(name, cumulative_hours, workStudy_names_dict, worksheet_names):
    print(name + "\n")
    WS_hour_dict = workStudy_names_dict[name]
    cumulative_hours = float(cumulative_hours)
    for date in worksheet_names:
        if(date in WS_hour_dict):
            hours_for_day = WS_hour_dict[date]
            cumulative_hours = cumulative_hours + hours_for_day
            
            print("-------------------")
            print("Date: " + str(date) + " Hours: " + str(hours_for_day) + " Cumulative Hours: " + str(cumulative_hours))
        else:
            continue



def find_hours_in_specific_sheet_for_all_names(worksheet_list_of_lists, workStudy_names_list, worksheet_name, workStudy_names_dict):
    for name in workStudy_names_list:
        locations_of_name = get_indexs_of_name(name, worksheet_list_of_lists)
        if(locations_of_name == []):
            continue
        total_hours = get_hour_value_for_day(locations_of_name, worksheet_list_of_lists)
        workStudy_names_dict[name][worksheet_name] = total_hours

# this function takes in a credentials file name and returns a service account object
def setupGspreadAccount(file_name):
    sa = gspread.service_account(filename=file_name)
    return sa

# this function takes in a service account object and a sheet name and returns a worksheet object
def openSheet(sa, sheet_name):
    sh = sa.open(sheet_name)
    return sh

#this function takes in a date in MM/DD/YYYY format and returns a datetime object
def stringDateToDateTime(date):
    date_str = str(date)
    # Convert the date string to a datetime object
    datetime_obj = datetime.strptime(date_str, "%m/%d/%Y")
    datetime_obj = datetime_obj.date()
    return datetime_obj

#this functioon takes in a string of names in (Last, First), (Last, First) format and returns a dictionary of names in "Last, First" format
def stringNamesToDict(string_names):
    pattern = r'\(([^,]+), ([^)]+)\)'
    matches = re.findall(pattern, string_names)
    # Extract and format the matches
    workStudy_names_dict = {", ".join(match): {} for match in matches}
    return workStudy_names_dict


def find_hours_in_all_sheets_for_all_names(credentials_filename, sheet_name, workstudy_stringNames, start_date, end_date):
    #get service account 
    sa = setupGspreadAccount(credentials_filename)
    #get the spreadsheet
    sh = openSheet(sa, sheet_name)
    #get the start and end date in datetime format\
    start_date = stringDateToDateTime(start_date)
    end_date = stringDateToDateTime(end_date)
    #get the work study names in a dict
    workStudy_names_dict = stringNamesToDict(workstudy_stringNames)
    #get the work study names in a list
    workStudy_names_list = list(workStudy_names_dict.keys())
    #get how many days to calculate worksheets for
    time_difference = end_date - start_date
    number_of_days = time_difference.days + 1
    #how many weeks are between the start and end date to subtarct the amount of weekends
    number_of_weeks = time_difference.days // 7
    number_of_days = number_of_days - (number_of_weeks * 2)
    new_date = start_date
    #intialize the worksheet names list
    worksheet_names = []
    for x in range(number_of_days):
        if (x == 0):
            new_date = new_date
        else:
            #get the new date to calculate
            new_date = new_date + timedelta(days=1)
        #if it is a weekend day skip it
        while(new_date.weekday() == 5 or new_date.weekday() == 6):
            new_date = new_date + timedelta(days=1)
        #get the date in string format
        new_date_string = dateType_to_dateString(new_date)
        #get the worksheet name
        worksheet_name = new_date_string + " Sign-In Sheet"
        #open the worksheet
        wks = sh.worksheet(worksheet_name)
        #get the list of lists of the worksheet
        worksheet_list_of_lists = wks.get_all_values()
        #not sure what this does
        worksheet_names.append(worksheet_name)
        #set the names to standard format
        set_names_to_standard(worksheet_list_of_lists)
        #find the hours for each name in the worksheet
        find_hours_in_specific_sheet_for_all_names(worksheet_list_of_lists, workStudy_names_list, worksheet_name, workStudy_names_dict)

    return workStudy_names_dict, worksheet_names



