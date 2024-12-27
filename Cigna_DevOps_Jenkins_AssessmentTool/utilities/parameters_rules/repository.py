# previously known as version_control_and_branching_strategy

from config import configuration as config

import datetime as dt

class REPOSITORY:
    
    def __init__(self):
        
        self.name="get version_control repository tools"


    def find_repository_tools_in_jenkinsfile(jenkinsfile_content, repository_tools_dict):
        found_tools = []
        for key, value in repository_tools_dict.items():
            if key in jenkinsfile_content:
                found_tools.append(value)
        return found_tools