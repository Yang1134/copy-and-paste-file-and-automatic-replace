import shutil
import os
import schedule
import time

from datetime import datetime


filename = input("What is the file name? please include the file extension .For example testing.txt  ")
temporary_file_location = input("What is the temporary file location to backup? include the destination path use / . For example C:/Users/Yang1281/Desktop ")

string = "C:/Users/Yang1281/Downloads/" + filename

def run(source_path, destination_path):
        shutil.copy2(source_path, destination_path)
        local_time = datetime.now()
        print(f"{source_path} has been copied to {destination_path} at {local_time}")

while os.path.exists(string):
     run(string, temporary_file_location)
     time.sleep(150)




