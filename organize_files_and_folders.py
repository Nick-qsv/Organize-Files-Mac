import os
import shutil
import time
from datetime import datetime

def organize_items(path):
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        if os.path.isfile(item_path):
            organize_file(item_path)
        elif os.path.isdir(item_path):
            organize_directory(item_path)

def organize_file(file_path):
    timestamp = os.path.getctime(file_path)
    year = datetime.fromtimestamp(timestamp).strftime("%Y")
    year_directory = os.path.join(os.path.dirname(file_path), year)
    if not os.path.exists(year_directory):
        os.makedirs(year_directory)
    month = datetime.fromtimestamp(timestamp).strftime("%m")
    month_directory = os.path.join(year_directory, month)
    if not os.path.exists(month_directory):
        os.makedirs(month_directory)
    shutil.move(file_path, os.path.join(month_directory, os.path.basename(file_path)))

def organize_directory(dir_path):
    timestamp = os.path.getctime(dir_path)
    year = datetime.fromtimestamp(timestamp).strftime("%Y")
    year_directory = os.path.join(os.path.dirname(dir_path), year)
    if not os.path.exists(year_directory):
        os.makedirs(year_directory)
    month = datetime.fromtimestamp(timestamp).strftime("%m")
    month_directory = os.path.join(year_directory, month)
    if not os.path.exists(month_directory):
        os.makedirs(month_directory)
    shutil.move(dir_path, os.path.join(month_directory, os.path.basename(dir_path)))

if __name__ == "__main__":
    path = input("Enter the path to your directory: ")
    organize_items(path)
