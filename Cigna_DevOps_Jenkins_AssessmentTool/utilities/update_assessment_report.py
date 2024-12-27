from config import configuration as config
import os
import shutil
import openpyxl
import re
import datetime as dt

class UPDATE_ASSESSMENT_REPORT:
    
    def __init__(self):
        
        self.name="update the assessment excel report"


    def update_excel_report(excel_file_path, stages_count, pipeline_type, triggers_count, is_artifactory_present, try_count, retry_count, approval_count, parallel_count):
        # Load the workbook and select the active sheet
        workbook = openpyxl.load_workbook(excel_file_path)
        sheet = workbook.active
        
        # Update the number of stages
        sheet['B4'] = stages_count
        
        # Update count of parallel execution blocks
        sheet['B5']= parallel_count

        # Update the number of triggers
        sheet['B6'] = triggers_count

        # Update the pipeline type
        sheet['B10'] = pipeline_type


        # Update the number of triggers
        if is_artifactory_present:
            sheet['B11'] = "Yes, artifact is present"
        else:
            sheet['B11'] = "No artifact present."

        # Update the Error handling count and Retry count
        msg= "Error handling count = "+str(try_count)+", Retry count = "+str(retry_count)+"."
        sheet['B12']=msg
        
        # Update count of approval
        sheet['B14']= approval_count

        

        # Determine the assessment based on the number of stages
        if stages_count <= 3:
            assessment = 'Simple'
            comment = 'Based on 1-3 stages'
        elif 4 <= stages_count <= 7:
            assessment = 'Medium'
            comment = 'Based on 4-7 stages'
        else:
            assessment = 'Complex'
            comment = 'Based on more than 8 stages'
        
        # Update the assessment and comment
        sheet['B1'] = assessment
        sheet['C1'] = comment
        
        workbook.save(excel_file_path)