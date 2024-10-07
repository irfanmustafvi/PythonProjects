import os

command = "systeminfo"  # for windows
# # command= "df -h" # Disk space For linux
# # command = "free -h" # RAM for linux
# # command = "date"

print(os.system(command))
########################################
import os

command = "systeminfo"


def check_cpu(command):  # defining a function
    print(os.system(command))


check_cpu("systeminfo")
#####################################################
command = "date"


def check_date(command):  # defining a function
    print(os.system(command))


check_date("date")  # calling a function


############################################################
## We can use return instead of print
import os
import datetime


def run_command(command):
    return os.system(command)


# run_command("date")  # for linux & output by enter date in window
# run_command("df -h")  # For linux


def show_date():
    return datetime.datetime.today()


today = show_date()  # output =>2024-09-04 21:52:35.274535
print(today)
