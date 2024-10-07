import os  # importing a new library in code

print(os.system("systeminfo"))  # windows, linux or mac
# print(os.system("uptime"))  # for linux uptime and load average
print(os.system("wmic computersystem get totalphysicalmemory"))  # RAM in window
