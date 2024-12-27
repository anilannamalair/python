from config import configuration as config

import datetime as dt

class NO_OF_STAGES:
    
    def __init__(self):
        
        self.name="number of stages"
        

    def count_stages_in_jenkinsfile(jenkinsfile_content):
    
        # Count the number of stages
        stages_count = jenkinsfile_content.count('stage(')
        return stages_count