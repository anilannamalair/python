from config import configuration as config
import os

import datetime as dt

# class VARIABLES_FINDER:
    
#     def __init__(self):
        
#         self.name="fetch all variables in the repo"

#     def find_lines_with_dollar_sign_environment_varaibles(folder_path):
#         lines_with_dollar = []

#         for root, dirs, files in os.walk(folder_path):
#             for file in files:
#                 file_path = os.path.join(root, file)
#                 try:
#                     with open(file_path, 'r', encoding='utf-8') as f:
#                         for line in f:
#                             if '${' in line:
#                                 lines_with_dollar.append((file_path, line.strip()))
#                 except Exception as e:
#                     print(f"Error reading {file_path}: {e}")

#         return lines_with_dollar

#     def write_output_to_file(folder_path, lines_with_dollar):
#         output_file_path = os.path.normpath(os.path.join(folder_path, 'Environment_variables_lines.txt'))
        
#         # Check if the file exists and delete it
#         if os.path.exists(output_file_path):
#             os.remove(output_file_path)
        
#         try:
#             with open(output_file_path, 'w', encoding='utf-8') as f:
#                 for file_path, line in lines_with_dollar:
#                     f.write(f"File: {file_path} -> Line: {line}\n")
#             print(f"Output written to {output_file_path}")
#             return output_file_path, 200
#         except Exception as e:
#             print(f"Error writing to {output_file_path}: {e}")
#             return output_file_path, 500

    
import os
import re

class VARIABLES_FINDER:
    
    def __init__(self):
        # Initialize the class with a name attribute
        self.name = "fetch all variables in the repo"

    def find_lines_with_dollar_sign_environment_varaibles(folder_path):
        """
        This function searches for lines containing '${' in all files within the given folder path.
        It recursively traverses all subdirectories and files.
        
        Args:
        folder_path (str): The path to the folder to search in.
        
        Returns:
        list: A list of tuples where each tuple contains the file path and the line containing '${'.
        """
        lines_with_dollar = []

        # Walk through the directory tree
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                try:
                    # Open each file and read line by line
                    with open(file_path, 'r', encoding='utf-8') as f:
                        for line in f:
                            # Check if the line contains '${'
                            if '${' in line:
                                lines_with_dollar.append((file_path, line.strip()))
                except Exception as e:
                    # Handle any exceptions that occur while reading the file
                    print(f"Error reading {file_path}: {e}")

        return lines_with_dollar

    def write_output_to_file(folder_path, lines_with_dollar):
        """
        This function writes the lines containing '${' to an output file.
        
        Args:
        folder_path (str): The path to the folder where the output file will be saved.
        lines_with_dollar (list): A list of tuples containing file paths and lines with '${'.
        
        Returns:
        tuple: The output file path and a status code (200 for success, 500 for failure).
        """
        output_file_path = os.path.normpath(os.path.join(folder_path, 'Environment_variables_lines.txt'))
        
        # Check if the output file already exists and delete it
        if os.path.exists(output_file_path):
            os.remove(output_file_path)
        
        try:
            # Write the lines to the output file
            with open(output_file_path, 'w', encoding='utf-8') as f:
                for file_path, line in lines_with_dollar:
                    f.write(f"File: {file_path} -> Line: {line}\n")
            print(f"Output written to {output_file_path}")
            return output_file_path, 200
        except Exception as e:
            # Handle any exceptions that occur while writing to the file
            print(f"Error writing to {output_file_path}: {e}")
            return output_file_path, 500

    def find_valid_variables(folder_path):
        """
        This function finds and counts valid environment variables in all files within the given folder path.
        Valid variables are in the format ${VAR_NAME} and do not contain '$@' inside the braces.
        
        Args:
        folder_path (str): The path to the folder to search in.
        
        Returns:
        dict: A dictionary where keys are valid variables and values are their counts.
        """
        # Regular expression to match valid variables
        variable_pattern = re.compile(r'\${([A-Za-z0-9_]+)}')
        # Regular expression to match invalid variables containing '$@'
        invalid_pattern = re.compile(r'\${.*\$@.*}')
        variables = {}

        # Walk through the directory tree
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                try:
                    # Open each file and read line by line
                    with open(file_path, 'r', encoding='utf-8') as f:
                        for line in f:
                            # Find all matches of valid variables
                            matches = variable_pattern.findall(line)
                            for match in matches:
                                variable = f"${{{match}}}"
                                # Check if the variable is not invalid
                                if not invalid_pattern.search(variable):
                                    if variable not in variables:
                                        variables[variable] = 0
                                    variables[variable] += 1
                except Exception as e:
                    # Handle any exceptions that occur while reading the file
                    print(f"Error reading {file_path}: {e}")

        return variables


# finder = VARIABLES_FINDER()
# folder_path = 'path_to_your_folder'

# # Find lines with dollar sign environment variables
# lines_with_dollar = finder.find_lines_with_dollar_sign_environment_varaibles(folder_path)
# print(lines_with_dollar)

# # Write output to file
# finder.write_output_to_file(folder_path, lines_with_dollar)

# # Find valid variables and their count
# valid_variables = finder.find_valid_variables(folder_path)
# print(valid_variables)

# # Get the list of variables
# variables_list = list(valid_variables.keys())
# print("Variables List:", variables_list)

# # Get the total count of all variables
# total_count = sum(valid_variables.values())
# print("Total Count of Variables:", total_count)
