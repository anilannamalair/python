from config import configuration as config
import re
import datetime as dt

class NO_OF_LIBRARIES:
    
    def __init__(self):
        
        self.name="number of libraries"


    def get_libraries_from_jenkinsfile_content(jenkinsfile_content):
        """
        This function takes the content of a Jenkinsfile as input,
        and returns a list of libraries mentioned in lines that start with 'library'.
        """
        libraries = []  # Initialize an empty list to store library names
        # Compile a regular expression pattern to match lines starting with 'library'
        # followed by a string in double quotes
        library_pattern = re.compile(r'^\s*library\s+"([^"]+)"')

        # Split the content into lines and iterate over each line
        for line in jenkinsfile_content.splitlines():
            # Check if the line matches the regular expression pattern
            match = library_pattern.match(line)
            if match:
                # If a match is found, extract the library name and add it to the list
                libraries.append(match.group(1))

        # Return the list of libraries found in the Jenkinsfile content
        return libraries



