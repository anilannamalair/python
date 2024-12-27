from config import configuration as config
import os
import shutil
import openpyxl
import re
import datetime as dt

class NO_OF_PARALLEL_EXECUTION:
    
    def __init__(self):
        
        self.name="count parallel execution bloacks"

    def count_jobs_and_parallel_blocks(jenkinsfile_content):
        # with open(file_path, 'r') as file:
        #     jenkinsfile_content = file.read()

        # Regular expressions to find jobs (stages) and parallel blocks
        job_pattern = re.compile(r'stage\s*\(\s*[\'"].+?[\'"]\s*\)', re.IGNORECASE)
        parallel_pattern = re.compile(r'parallel\s*{', re.IGNORECASE)

        # Find all matches
        jobs = job_pattern.findall(jenkinsfile_content)
        parallel_blocks = parallel_pattern.findall(jenkinsfile_content)

        # Count the number of matches
        job_count = len(jobs)
        parallel_count = len(parallel_blocks)

        return job_count, parallel_count