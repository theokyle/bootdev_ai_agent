import os

def write_file(working_directory, file_path, content):
    abs_working_directory = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    common_path = os.path.commonpath([abs_working_directory, abs_file_path])
    if common_path != abs_working_directory:
        return f'Error: Cannot list "{file_path}" as it is outside the permitted working directory'