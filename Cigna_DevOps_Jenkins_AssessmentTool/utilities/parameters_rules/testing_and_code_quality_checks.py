from config import configuration as config

import datetime as dt

class TESTING_AND_CODE_QUALITY_CHECKS:
    
    def __init__(self):
        
        self.name="get tools for testing"

    # def find_tools_in_jenkinsfile(jenkinsfile_path, testing_tools_list):
    #     # Open the Jenkinsfile in read mode
    #     with open(jenkinsfile_path, 'r') as file:
    #         # Read all lines from the file
    #         lines = file.readlines()

    #     # Initialize a flag to indicate if we are in the 'tools' section
    #     tools_section = False
    #     # Set to store found tools
    #     found_tools = set()

    #     # Iterate over each line in the file
    #     for line in lines:
    #         # Remove leading and trailing whitespace from the line
    #         stripped_line = line.strip()
    #         # Check if the line indicates the start of the 'tools' section
    #         if stripped_line.startswith('tools {'):
    #             tools_section = True
    #             continue
    #         # If we are in the 'tools' section
    #         if tools_section:
    #             # Check if the line indicates the end of the 'tools' section
    #             if stripped_line == '}':
    #                 break
    #             # Split the line into words
    #             words = stripped_line.split()
    #             # Check if any word in the line matches a tool in the testing_tools_list
    #             for word in words:
    #                 if word in testing_tools_list:
    #                     found_tools.add(word)

    #     # Return the set of found tools
    #     return list(found_tools)
    def find_tools_in_jenkinsfile(jenkinsfile_content, testing_tools_list):
        found_tools = []
        for tool in testing_tools_list:
            if tool in jenkinsfile_content:
                found_tools.append(tool)
        return found_tools