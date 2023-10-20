import gspread
import time
from datetime import date, timedelta
import calendar
import numpy as np
from tqdm import tqdm
  

sa = gspread.service_account()
sh = sa.open("2023 Fall Semester Shift Sign-in Sheet, 10/16")
current_date = input("Enter the start date in MM/DD/YYYY format\n")

workStudy_names_dict = {"Mills, Marissa": {}, "Butera, Salvatore": {}, "Cancel, David": {}, "Etyang, Arthur": {}, "Godbey, Kaelyn": {}, "Gomez, Kenny": {}, "Ibarra, Christyanna": {}, "Landes, Mahlon": {}, "Mendoza, Vanessa": {}, "Mihaileanu, George": {}, "Nosike, Austin": {}, "Pembleton, Aidan": {}, "Potter, Chandler": {}, "Quartey, Eric": {}, "Ramirez, Jose": {},  "Rodas, Melvin": {}, "Rojas, Roberto": {}, "Sandoval, Edwin": {}, "Simons, Emma": {}, "Tenet, Brooke": {}, "West, Sydney": {}, "Angelina, Zubricki": {}}

workStudy_names_list = list(workStudy_names_dict.keys())

year = current_date[6:]
#print("year = " + year + "\n")

day = current_date[3:5]
#print("day = " + day + "\n")


month = current_date[:2]
month = month[0:]
print("month = " + month + "\n")

#print("current date " + current_date)

month = int(month)
year = int(year)
day = int(day)

start_date = date(year, month, day)



#print(start_date)

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
    


def dateType_to_dateString(date):
    date = str(date)
    year = date[:4]
    month = date[5:7]
    day = date[8:]
    if(month[0:-1] == "0"):
        month = month[1:]
    if(day[0:-1] == "0"):
        day = day[1:]
    complete_date = month + "/" + day + "/" + year

    ##print("This is year in function " + year)
    ##print("This is month in function " + month)
    ##print("This is day in function " + day)
    return complete_date


worksheet_names = []



def time_sheet_for_name(name, cumulative_hours):
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



def find_hours_in_specific_sheet_for_all_names(worksheet_list_of_lists):
    for name in workStudy_names_list:
        locations_of_name = get_indexs_of_name(name, worksheet_list_of_lists)
        if(locations_of_name == []):
            continue
        total_hours = get_hour_value_for_day(locations_of_name, worksheet_list_of_lists)
        workStudy_names_dict[name][worksheet_name] = total_hours


loop = tqdm (total = 10, position = 0, leave = False)
for x in range(10):
    loop.set_description("Loading...".format(x))
    loop.update(1)
        # calculating end date by adding 10 days
    if(x > 4):
        x = x+2
    new_date = start_date + timedelta(days=x)
    new_date_string = dateType_to_dateString(new_date)
    worksheet_name = new_date_string + " Sign-In Sheet"
    print("worksheet name " + worksheet_name)
    wks = sh.worksheet(worksheet_name)
    worksheet_list_of_lists = wks.get_all_values()
    worksheet_names.append(worksheet_name)
    set_names_to_standard(worksheet_list_of_lists)
    find_hours_in_specific_sheet_for_all_names(worksheet_list_of_lists)

loop.close()
while True:
    print("\n\n")
    current_workstudy = input("Enter the last name of the workstudy you want to get the hours of\n")
    print("\n")
    if(current_workstudy == "exit"):
        break
    cumulative_hours = input("What was their cumulative hours last week\n")
    print("\n")
    cumulative_hours = float(cumulative_hours)
    print("###############################\n")
    time_sheet_for_name(current_workstudy, cumulative_hours)
    


