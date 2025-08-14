File = open("FH_Practice.txt", "w")  # Opening the file in write mode to create or overwrite it
File.write("This is a practice file for file handling in Python.\n")
File.write("We are learning how to read and write files.\n")
File.close()


File = open("FH_Practice.txt", "r") # Opening the file in read mode to read its content
content = File.read()
print("Content of the file:")
print(content)
File.close()

File = open("FH_Practice.txt", "a")                 # Appending to the file at the end
File.write("Appending a new line to the file.\n")
File.close()

File = open("FH_Practice.txt", "r")
content = File.read()
print("Updated content of the file:")
print(content)
File.close()

File = open("FH_Practice.txt", "r")  # Reading the file line by line
print("Reading the file line by line:")
for line in File:
    print(line.strip())  # Using strip() to remove any leading/trailing whitespace
File.close()



file = open("FH_Practice.txt", "r")  
line1 = file.readline()     # Reading the first line
line2 = file.readline()     # Reading the second line
print("First line:", line1.strip())
print("Second line:", line2.strip())
file.close()

File = open("FH_Practice.txt", "r")  
lines = File.readlines()  # Reading all lines into a list
print("All lines in the file:", lines)


with open("FH_Practice.txt", "r") as file: 
    content = file.read()  # Reading the entire content of the file
    print("Content read using 'with':")
    print(content)
    
#----------------------------------------------------------------------------------
    
with open("FH_Practice.txt", "a") as file:  # Appending to the file using 'with'
    file.write("This is an additional line added using 'with' statement.\n")
with open("FH_Practice.txt", "r") as file:  # Reading the file using 'with'
    updated_content = file.read()
    print("Updated content after appending using 'with':")
    print(updated_content)
    
#----------------------------------------------------------------------------------

# import os
# file_path = "FH_Practice.txt"
# if os.path.exists(file_path):  # Checking if the file exists
#     os.remove(file_path)  # Deleting the file if it exists
#     print(f"{file_path} has been deleted.")
# else:
#     print(f"{file_path} does not exist, so it cannot be deleted.")  

#----------------------------------------------------------------------------------

#rename file
import os
old_file_path = "FH_Practice.txt"
new_file_path = "FH_Practice_Renamed.txt"
if os.path.exists(old_file_path):  # Checking if the old file exists
    os.rename(old_file_path, new_file_path)  # Renaming the file
    print(f"{old_file_path} has been renamed to {new_file_path}.")
else:
    print(f"{old_file_path} does not exist, so it cannot be renamed.")
    
  #-----------------------------------------------------------------------------------  
    
try:
    with open("FH_Practice_Renamed.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("Error: File does not exist!")
    
    
    
    
#----------------------------------------------------------------------------------

with open("FH_Practice_Renamed.txt", "r") as src:
    content = src.read()

with open("copy.txt", "w") as copyFile:
    copyFile.write(content)

print("File copied successfully!")



#----------------------------------------------------------------------------------