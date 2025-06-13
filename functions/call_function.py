from .get_file_content import get_file_content
from .get_files_info import get_files_info
from .run_python import run_python_file
from .write_file import write_file
from google import genai
from google.genai import types

def call_function(function_call_part, verbose=False):
    if verbose:
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")
    else:
        print(f" - Calling function: {function_call_part.name}")

    args = function_call_part.args
    args["working_directory"] = "./calculator"

    functions = {
        "get_file_content": get_file_content,
        "get_files_info": get_files_info,
        "run_python_file": run_python_file,
        "write_file": write_file
    }

    if function_call_part.name not in functions:
            return types.Content(
                role="tool",
                parts=[
                 types.Part.from_function_response(
                 name=function_call_part.name,
                 response={"error": f"Unknown function: {function_call_part.name}"},
                )
                ],
            )
    
    result = functions[function_call_part.name](**args)
    
    return types.Content(
    role="tool",
    parts=[
        types.Part.from_function_response(
            name=function_call_part.name,
            response={"result": result},
        )
    ],
)
