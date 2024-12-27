from config import configuration as config

import datetime as dt

class PIPELINE_SCRIPT_COMPLEXITY:
    
    def __init__(self):
        
        self.name="identity the pipeline type"
        

    def identify_pipeline_type(jenkinsfile_content):
        if 'pipeline {' in jenkinsfile_content and 'sh' in jenkinsfile_content or 'bat' in jenkinsfile_content:
            return 'Partially Scripted'
        elif 'pipeline {' in jenkinsfile_content and 'sh' not in jenkinsfile_content and 'bat' not in jenkinsfile_content:
            return 'Declarative Pipeline'
        elif 'node {' in jenkinsfile_content:
            return 'Scripted Pipeline'
        else:
            return 'Unknown Pipeline Type'