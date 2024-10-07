# Backup files by automate in Python
import shutil
import datetime
import os


def backup_files(source, destination):
    today = datetime.datetime.today()
    backup_files_name = os.path.join(
        destination, f"Backups_{today}")  # f means formated str
    shutil.make_archive(backup_files_name, "gztar",source)
    
    
source = "\Users\user\Documents\PythonProjects\PythonLiveWorkshop"
destination = "\Users\user\Documents\PythonProjects\PythonLiveWorkshop\Backups"
backup_files(source,destination)
