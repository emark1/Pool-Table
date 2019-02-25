#Pool table
#- As an admin you should be able to see all the tables (12) 

#- As an admin each table in the list should show, whether the table is 
# OCCUPIED or NOT OCCUPIED. 

#- As an admin if the table is OCCUPIED then show the 
# start time of the table, number of minutes played. (Hardmode - If the 
# minutes are > 60 then show them in terms of hours) 

#- As an admin you can only give out the tables that are NOT OCCUPIED. 
# This means if pool table 8 is occupied and you try to give it out then
#  the app will print a message saying "Pool Table 8 is currently occupied". 

#- As an admin whenever I close the table it should write an 
# entry in the text file / json file. The file should be named in the 
# following format: (11-22-2017.txt or 11-22-2017.json) keeping track of 
# all the tables. The entry can consists of the following information: 

# _________________________________________

# Pool Table Number 

# Start Date Time

# End Date Time 

# Total Time Played 

# Cost (if you are doing the hard mode) 

from datetime import datetime
user_input = ""
table_list = []
import json


def show_main_menu():
    print("""Press 1 to view tables and status.
Press 2 to check out a table.
Press 3 check in a table.
Press Q to quit.""")

def check_out_table():
    show_table_status()
    table_select = int(input("Select a table to check out: "))
    selection = table_list[table_select - 1]
    if selection.isavailable is True:
        selection.checkout()
    else: 
        print("This table is unavailable.")

    # for table in table_list:
    #     if table.isavailable == False:
    #         print("This table is unavailable.")
    #     elif table.isavailable == True:
    #         table_list[table_select-1].checkout()

def check_in_table():
    show_table_status()
    table_select = int(input("Select a table to check in: "))  
    write_to_text()
    table_list[table_select-1].checkin()
    
    
def write_to_text():
    with open('newreport.txt','w') as text_file:
        for table in table_list:
            if table.isavailable is True:
                text_file.write("------------------------- \n")
                text_file.write(f"Table number: {table_list.index(table) + 1} \n")
                text_file.write("Available \n")
            else:
                text_file.write("------------------------- \n")
                text_file.write(f"Table number: {table_list.index(table) + 1} \n")
                text_file.write(f"Start time: {table.start_time} \n")
                text_file.write(f"End time: {table.end_time} \n")
                text_file.write(f"Total time: {datetime.now().minute - table.end_time.minute} minute(s) \n")
                text_file.write(f"Current cost: ${(datetime.now().minute - table.end_time.minute) * 0.5} \n")

def show_table_status():
    for table in table_list:
        print(f'Table number {table_list.index(table) + 1}:')
        if table.isavailable is True:
            print("Available")
        else: 
            print(f"Unavailable. Time started: {table.start_time} Minutes played: {datetime.now().minute - table.end_time.minute}")


class Table:
    def __init__(self,tablenumber):
        self.tablenumber = tablenumber
        self.isavailable = True
        self.start_time = datetime.now()
        self.end_time = datetime.now()

    def checkout(self):
        self.isavailable = False
        self.start_time = datetime.now()
    
    def checkin(self):
        self.isavailable = True
        self.end_time = datetime.now()

#    def jsondictionary(self):
#       return {"number": self.tablenumber, "start_time": self.start_time, "end_time": self.end_time, "total_time": datetime.now().minute - table.end_time.minute}

# def jsonwrite():


# jsondump_dictionary = {"number": }
# for i in table_list:


# y = json.dumps()
# with 
# table_dictionary = {}
# def write_info_for_json():
#     with open()

for index in range(1,13):
    pool_table = Table(index)
    table_list.append(pool_table)

while user_input != "q":
    show_main_menu()
    user_input = input("Enter your choice here: ")
    if user_input == "1":
        show_table_status()
    elif user_input == "2":
        check_out_table()
    elif user_input == "3":
         check_in_table()