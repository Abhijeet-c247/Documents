import os

# Use absolute path for folder_path

folder_path = "Task/"

for count, filename in enumerate(os.listdir(folder_path), start=1):
    
    old_file = os.path.join(folder_path, filename)

   
    if not os.path.isfile(old_file):
        continue

    
    name, extension = os.path.splitext(filename)

   
    new_name = f"Renamed {count}{extension}"

   
    new_file = os.path.join(folder_path, new_name)

  
    os.rename(old_file, new_file)
    
    print(f"Renamed File: {filename} to {new_name}")

print(" All files renamed successfully.")
