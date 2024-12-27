from config import configuration as config

import datetime as dt

class CLOUD_INFRA_AND_CONTAINERIZATION:
    
    def __init__(self):
        
        self.name="get containeration tools"


    def find_containeration_tools_in_jenkinsfile(jenkinsfile_content, containeration_tools_list):
        found_tools = []
        for tool in containeration_tools_list:
            if tool in jenkinsfile_content:
                found_tools.append(tool)
        return found_tools