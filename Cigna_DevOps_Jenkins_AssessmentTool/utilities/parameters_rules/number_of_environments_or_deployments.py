from config import configuration as config
import re
import datetime as dt

class NUMBER_OF_ENVIRONMENTS_OR_DEPLOYMENTS:
    
    def __init__(self):
        
        self.name="get deploy stages"




    def count_deploy_stages(jenkinsfile_content):
        
        
        # Regex to match stages with 'deploy' in their names
        deploy_stage_pattern = re.compile(r"stage\s*\(\s*'\"['\"]\s*\)", re.IGNORECASE)
        deploy_stages = deploy_stage_pattern.findall(jenkinsfile_content)
        
        return len(deploy_stages)





