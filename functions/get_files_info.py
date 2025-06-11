import os

def get_files_info(working_directory, directory=None):
    abs_working_directory = os.path.abspath(working_directory)
    abs_directory = os.path.abspath(os.path.join(working_directory, directory))
    common_path = os.path.commonpath([abs_working_directory, abs_directory])
    if common_path != abs_working_directory:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    
    if os.path.isdir(abs_directory) == False:
        return f'Error: "{directory}" is not a directory'

    try:
        files = os.listdir(abs_directory)
        file_info = []
        for file in files:
            file_path = os.path.join(abs_directory, file)
            size = os.path.getsize(file_path)
            is_dir = os.path.isdir(file_path)
            file_info.append(f"- {file}: file_size={size} bytes, is_dir={is_dir}")
    except Exception as e:
        return f"Error: {e}"

    
    return "\n".join(file_info)
    
