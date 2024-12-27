from config import configuration as config
import os
import shutil
import openpyxl
import re
import datetime as dt

class APPROVAL_GATES:
    
    def __init__(self):
        
        self.name="count approval stages"

    def count_approval_stages(jenkinsfile_content):
        # with open(file_path, 'r') as file:
        #     jenkinsfile_content = file.read()

        # Regular expression to find 'Approval' stage
        approval_pattern = re.compile(r'stage\s*\(\s*[\'"]Approval[\'"]\s*\)', re.IGNORECASE)

        # Find all matches
        approval_stages = approval_pattern.findall(jenkinsfile_content)

        # Count the number of matches
        approval_count = len(approval_stages)

        return approval_count
