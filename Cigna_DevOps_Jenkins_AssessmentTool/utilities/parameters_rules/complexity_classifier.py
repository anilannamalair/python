from config import configuration as config
import re
import datetime as dt

class COMPLEXITY_CLASSIFIER:
    
    def __init__(self):
        
        self.name="classify complexity"


    def classify_jenkinsfile(jenkinsfile_content):
        """
        This function classifies the Jenkinsfile content as 'Complex', 'Medium', 'Simple', or 'Unknown'
        based on the presence of certain keywords and patterns.
        """
        # Regular expression to match any library declaration
        library_pattern = re.compile(r'^\s*library\s+"[^"]+"', re.MULTILINE)

        # Check if the Jenkinsfile is 'Complex'
        if library_pattern.search(jenkinsfile_content):
            return "Complex"
        
        # Check if the Jenkinsfile is 'Medium'
        if 'node {' in jenkinsfile_content or 'sh' in jenkinsfile_content or 'bat' in jenkinsfile_content:
            return "Medium"
        
        # Check if the Jenkinsfile is 'Simple'
        if 'pipeline {' in jenkinsfile_content and 'sh' not in jenkinsfile_content and 'bat' not in jenkinsfile_content:
            return "Simple"
        
        # If none of the above conditions are met, classify as 'Unknown'
        return "Unknown"





