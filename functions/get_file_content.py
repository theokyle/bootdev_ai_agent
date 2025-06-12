import os

def get_file_content(working_directory, file_path):
    # Check if file_path is outside the workign directory
    abs_working_directory = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    common_path = os.path.commonpath([abs_working_directory, abs_file_path])
    if common_path != abs_working_directory:
        return f'Error: Cannot read "{file_path}" is outside the permitted working directory'
    
    if os.path.isfile(abs_file_path) == False:
        return f'Error: File not found or is not a regular file "{file_path}"'
    
    MAX_CHARS = 10000

    with open(abs_file_path, "r") as f:
        file_content_string = f.read(MAX_CHARS)
        if len(file_content_string) == MAX_CHARS:
            file_content_string += f'[...File "{file_path}" truncated at 10000 characters]'

    return file_content_string
    


    
    
