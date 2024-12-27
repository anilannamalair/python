import os

import re

class JENKINFILE_FIND_AND_READ:
    
    def __init__(self):
        
        self.name="assessment per repo"

    def find_jenkinsfile(folder_path):
        for root, dirs, files in os.walk(folder_path):
            if 'Jenkinsfile' in files:
                return os.path.join(root, 'Jenkinsfile')
        return None

    # def find_read_jenkinsfile(jenkins_folder_path):
    #     # Find the Jenkinsfile
    #     #jenkinsfile_path = self.find_jenkinsfile(jenkins_folder_path)
    #     for root, dirs, files in os.walk(jenkins_folder_path):
    #         if 'Jenkinsfile' in files:
    #             jenkinsfile_path= os.path.join(root, 'Jenkinsfile')
        
    #     if not jenkinsfile_path:
    #         print("Jenkinsfile not found")
    #         return "Jenkinsfile not found", 500
        
    #     with open(jenkinsfile_path, 'r') as file:
    #         jenkinsfile_content = file.read()
            
    #     return jenkinsfile_content, 200


    def find_read_jenkinsfile(jenkins_folder_path):
        """
        This function finds the Jenkinsfile in the specified folder, reads its content,
        removes comments, and returns the cleaned content.
        """
        # Initialize the jenkinsfile_path variable
        jenkinsfile_path = None

        # Walk through the directory to find the Jenkinsfile
        for root, dirs, files in os.walk(jenkins_folder_path):
            if 'Jenkinsfile' in files:
                jenkinsfile_path = os.path.join(root, 'Jenkinsfile')
                break  # Stop searching once the Jenkinsfile is found

        if not jenkinsfile_path:
            print("Jenkinsfile not found")
            return "Jenkinsfile not found", 500

        # Read the content of the Jenkinsfile
        with open(jenkinsfile_path, 'r') as file:
            jenkinsfile_content = file.read()

        # Remove single-line comments
        jenkinsfile_content = re.sub(r'//.*', '', jenkinsfile_content)
        # Remove multi-line comments, including those with asterisks at the beginning of each line
        jenkinsfile_content = re.sub(r'/\*[\s\S]*?\*/', '', jenkinsfile_content)
        

        return jenkinsfile_content, jenkinsfile_path, 200


