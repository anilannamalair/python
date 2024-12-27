from config import configuration as config
import os
import shutil
import openpyxl
import re
import datetime as dt

class ARTIFACT_MANAGEMENT:
    
    def __init__(self):
        
        self.name="find artifact"


    def check_artifactory_in_jenkinsfile(jenkinsfile_content):
        # with open(file_path, 'r') as file:
        #     jenkinsfile_content = file.read()

        # Regular expression to find the environment section
        env_pattern = re.compile(r'environment\s*{[^}]*}', re.MULTILINE)
        env_section = env_pattern.search(jenkinsfile_content)

        if env_section:
            env_content = env_section.group(0)
            # Check for Artifactory server and credentials
            server_present = 'artifactory_server' in env_content
            cred_present = 'artifactory_cred' in env_content

            if server_present and cred_present:
                # Extract the lines containing the Artifactory configuration
                artifactory_lines = re.findall(r'(artifactory_server\s*=\s*.*|artifactory_cred\s*=\s*.*)', env_content)
                return True, artifactory_lines
            else:
                return False, []
        else:
            return False, []


# file_path = r"C:\Users\Jawad.SalmanS\Downloads\test\Jenkinsfile"
# is_present, artifactory_lines = check_artifactory_in_jenkinsfile(file_path)
# if is_present:
#     print("Artifactory configuration is present in the Jenkinsfile.")
#     print("Artifactory lines:")
#     for line in artifactory_lines:
#         print(line)
# else:
#     print("Artifactory configuration is NOT present in the Jenkinsfile.")

# # Artifactory configuration is present in the Jenkinsfile.
# # Artifactory lines:
# # artifactory_server = 'my-artifactory-server' // Artifactory server ID configured in Jenkins UI
# # artifactory_cred = credentials('artifactory-credentials-id') // Artifactory credentials ID
