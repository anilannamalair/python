from config import configuration as config
import re
import datetime as dt

class EXTERNAL_INTEGRATIONS:
    
    def __init__(self):
        
        self.name="get external integrations"


    def extract_tools_section_first_words(jenkinsfile_path):
        # Open the Jenkinsfile in read mode
        with open(jenkinsfile_path, 'r') as file:
            # Read all lines from the file
            lines = file.readlines()

        # Initialize a flag to indicate if we are in the 'tools' section
        tools_section = False
        # List to store the first words of each line in the 'tools' section
        first_words = []

        # Iterate over each line in the file
        for line in lines:
            # Remove leading and trailing whitespace from the line
            stripped_line = line.strip()
            # Check if the line indicates the start of the 'tools' section
            if stripped_line.startswith('tools {'):
                tools_section = True
                continue
            # If we are in the 'tools' section
            if tools_section:
                # Check if the line indicates the end of the 'tools' section
                if stripped_line == '}':
                    break
                # Split the line into words and get the first word
                first_word = stripped_line.split()[0]
                # Add the first word to the list
                first_words.append(first_word)

        # Return the list of first words if the 'tools' section was found, otherwise return None
        return first_words if tools_section else None