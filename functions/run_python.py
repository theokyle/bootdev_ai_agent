import os
import subprocess

def run_python_file(working_directory, file_path):
    # Check if file_path is outside the working directory
    abs_working_directory = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    common_path = os.path.commonpath([abs_working_directory, abs_file_path])
    if common_path != abs_working_directory:
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    
    #Check if file_path exists
    if not os.path.exists(abs_file_path):
        return f'Error: File "{file_path}" not found.'
    
    #Check if file_path is a valid Python file
    root, ext = os.path.splitext(abs_file_path)
    if ext != ".py":
        return f'Error: "{file_path}" is not a Python file.'
    
    try:
        completed_process = subprocess.run(["python3", abs_file_path], timeout=30)
        stdout = f'STDOUT: {completed_process.stdout}'
        stderr = f'STDERR: {completed_process.stderr}'

        if completed_process.returncode != 0:
            return f'Process exited with code {completed_process.returncode}'
        
        if stdout == "":
            return "No output produced"
    except Exception as e:
        return f"Error: executing Python file: {e}"
