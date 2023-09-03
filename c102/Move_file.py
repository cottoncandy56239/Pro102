import os
import shutil

from_directory = "/Users/mridinikulkarni/Downloads"
to_directory = "/Users/mridinikulkarni/Documents_Files"

list_of_files = os.listdir(from_directory)
for file_name in list_of_files:
    name, extension = os.path.splitext(file_name)
    if extension == '':
        continue
    if extension in ['.txt', '.doc', '.docx', '.pdf']:
        path1 = from_directory + '/' + file_name
        path2 = to_directory + '/' + "Document_Files"
        path3 = to_directory + '/' + "Document_Files" + '/' + file_name
    
        if os.path.exists(path2):
            print("Moving " + file_name + ".....")
            shutil.move(path1, path3)
        else:
            os.makedirs(path2)
            print("Moving " + file_name + ".....")
            shutil.move(path1, path3)