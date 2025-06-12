import os

def write_file(working_directory, file_path, content):
    
    # Check if file_path is outside the workign directory
    abs_working_directory = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    common_path = os.path.commonpath([abs_working_directory, abs_file_path])
    if common_path != abs_working_directory:
        return f'Error: Cannot list "{file_path}" as it is outside the permitted working directory'
    
    #Create file_path if it doesn't exist
    
    directory = os.path.dirname(abs_file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)

    #Overwrite contents of the file with content
    with open(abs_file_path, "w") as f:
        f.write(content)
    
    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
