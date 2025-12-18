import os

# specify directory
directory_path = '/Riot Games' 
# list all files
contents = os.listdir(directory_path)
# print each file
for item in contents:
    print(item)
