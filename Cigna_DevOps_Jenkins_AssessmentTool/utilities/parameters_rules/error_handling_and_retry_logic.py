from config import configuration as config
import os
import shutil
import openpyxl
import re
import datetime as dt

class ERROR_HANDLING_AND_RETRY_LOGIC:
    
    def __init__(self):
        
        self.name="find artifact"


    def count_try_and_retry_blocks(jenkinsfile_content):
        # with open(file_path, 'r') as file:
        #     jenkinsfile_content = file.read()

        # Regular expressions to find try and retry blocks
        try_pattern = re.compile(r'\btry\b', re.MULTILINE)
        retry_pattern = re.compile(r'\bretry\s*\(\d+\)', re.MULTILINE)

        # Find all matches
        try_blocks = try_pattern.findall(jenkinsfile_content)
        retry_blocks = retry_pattern.findall(jenkinsfile_content)

        # Count the number of matches
        try_count = len(try_blocks)
        retry_count = len(retry_blocks)

        return try_count, retry_count