from config import configuration as config

import datetime as dt

class SECURITY_AND_COMPLIANCE_CHECKS:
    
    def __init__(self):
        
        self.name="get security tools"


    def find_security_tools_in_jenkinsfile(jenkinsfile_content, security_tools_list):
        found_tools = []
        for tool in security_tools_list:
            if tool in jenkinsfile_content:
                found_tools.append(tool)
        return found_tools