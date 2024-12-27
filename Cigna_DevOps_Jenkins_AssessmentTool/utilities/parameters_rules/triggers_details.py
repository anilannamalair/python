from config import configuration as config
import os
import shutil
import openpyxl
import re
import datetime as dt

class TRIGGERS_DETAILS:
    
    def __init__(self):
        
        self.name="triggers count"
        

    def extract_triggers(content):
        
        

        # Remove single line comments
        content = re.sub(r'//.*', '', content)
        # Remove multi-line comments
        content = re.sub(r'/\*.*?\*/', '', content, flags=re.DOTALL)

        # Find the triggers section
        triggers_section = re.search(r'triggers\s*{([^}]*)}', content, re.DOTALL)
        if not triggers_section:
            return 0, []

        triggers_content = triggers_section.group(1)

        # Extract triggers
        triggers = re.findall(r'\b\w+\s*\(.*?\)|\b\w+\s*\".*?\"', triggers_content)

        return len(triggers), triggers