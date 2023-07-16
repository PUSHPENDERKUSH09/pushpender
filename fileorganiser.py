import os
import shutil

def organize_files(directory):
    
    files = os.listdir(directory)

   
    extensions = {}

  
    for file in files:
        if os.path.isfile(file):  # Check if it's a file
            file_name, file_ext = os.path.splitext(file)  

           
            if file_ext not in extensions:
                new_directory = os.path.join(directory, file_ext[1:].upper() + " Files")
                os.makedirs(new_directory)
                extensions[file_ext] = new_directory

           
            current_path = os.path.join(directory, file)
            new_path = os.path.join(extensions[file_ext], file)
            shutil.move(current_path, new_path)

    print("File organization completed.")


directory_path = "path/to/directory"

organize_files(directory_path)
