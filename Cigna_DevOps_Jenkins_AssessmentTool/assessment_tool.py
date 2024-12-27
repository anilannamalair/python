from config import configuration as config
from utilities.assessment_per_repo import ASSESSMENT_PER_REPO

import pandas as pd
import shutil,os
from utilities.logging import log_message

if __name__ == "__main__":

    
    log_message ("Assessment Tool started.", "Info")
    # Step 1: Read the `repo_directory.csv` file to get the list of `repo_url` and `repo_token`.
    csv_path= config.REPO_DIRECTORY
    repo_directory = pd.read_csv(csv_path)

    # Step 2: Duplicate the `generic_consolidated_assessment_report.xlsx` file and name it `consolidated_assessment_report.xlsx`.
    generic_excel_path= config.GENERIC_CONSOLIDATED_ASSESSMENT_REPORT
    shutil.copyfile(generic_excel_path, 'consolidated_assessment_report.xlsx')

    # Step 3: For each `repo_url` and `repo_token`, execute the `assess_per_repo_func` function and update the Excel file.
    results = []
  
    local_working_dir = config.LOCAL_DIR

    for index, row in repo_directory.iterrows():
        repo_url = row['repo_url'].rstrip(' /')
        repo_token = row['repo_token']
        
        
        # Create a dynamic folder name
        #repo_number= index+1
        dynamic_folder = repo_url.split('/')[-1]
        #dynamic_folder = f"AssessmentRepo{repo_number}"
        
        # Combine the local working directory with the dynamic folder
        dynamic_path = os.path.join(local_working_dir, dynamic_folder)
        
        # Pass the dynamic path as an additional parameter
        result = ASSESSMENT_PER_REPO.assessment_per_repo_func(repo_url, repo_token, dynamic_path)
        
        results.append(result)


    # Convert results to DataFrame
    results_df = pd.DataFrame(results)

    # Load the duplicated Excel file and append the results
    with pd.ExcelWriter('consolidated_assessment_report.xlsx', mode='a', engine='openpyxl', if_sheet_exists='overlay') as writer:
        results_df.to_excel(writer, sheet_name='Sheet1', index=False, startrow=1, header=False)

    print("The consolidated assessment report has been updated successfully.")
    log_message ("Assessment Tool ended.", "Info")
