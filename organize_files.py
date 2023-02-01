import os
import shutil
import time
from datetime import datetime

def organize_files(path):
    for filename in os.listdir(path):
        file_path = os.path.join(path, filename)
        if os.path.isfile(file_path):
            timestamp = os.path.getctime(file_path)
            year = datetime.fromtimestamp(timestamp).strftime("%Y")
            year_directory = os.path.join(path, year)
            if not os.path.exists(year_directory):
                os.makedirs(year_directory)
            shutil.move(file_path, os.path.join(year_directory, filename))

    for year in os.listdir(path):
        year_path = os.path.join(path, year)
        if os.path.isdir(year_path):
            for filename in os.listdir(year_path):
                file_path = os.path.join(year_path, filename)
                if os.path.isfile(file_path):
                    timestamp = os.path.getctime(file_path)
                    month = datetime.fromtimestamp(timestamp).strftime("%m")
                    month_directory = os.path.join(year_path, month)
                    if not os.path.exists(month_directory):
                        os.makedirs(month_directory)
                    shutil.move(file_path, os.path.join(month_directory, filename))

if __name__ == "__main__":
    path = input("Enter the path to your directory: ")
    organize_files(path)
