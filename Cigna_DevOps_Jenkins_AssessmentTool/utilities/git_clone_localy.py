import requests
from github import Github
import os
from config import configuration as config
import subprocess
import math

class GIT_CLONE:
 
    def __init__(self) :
        self.name="git clone locally"
        
 
    # Replace with your GitHub token
    #GITHUB_TOKEN = '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'
    

    def fork_repo(repo_url, repo_token):
        
        # Check if repo_token is a string and not empty
        if isinstance(repo_token, str) and repo_token.strip():
            is_repo_token_valid = True
        # Check if repo_token is a float and NaN
        elif isinstance(repo_token, float) and math.isnan(repo_token):
            is_repo_token_valid = False
        # Any other case is invalid
        else:
            is_repo_token_valid = False
    
        if not is_repo_token_valid:
            try:
            # Directly return the repo URL since it's public
                print(f"Repository URL: {repo_url}")
                return repo_url, 200
            except Exception as e:
                print("Error in fork_repo method: " + str(e))
                return "", 500
        else:
            try:
                # Extract the owner and repo name from the URL
                owner, repo = repo_url.rstrip('/').split('/')[-2:]
                #GITHUB_TOKEN = config.GITHUB_TOKEN
                GITHUB_TOKEN = repo_token
                # Authenticate with GitHub
                g = Github(GITHUB_TOKEN)
                user = g.get_user()
                
                # Fork the repository
                repo_to_fork = g.get_repo(f"{owner}/{repo}")
                forked_repo = user.create_fork(repo_to_fork)
                
                print(f"Forked repository: {forked_repo.clone_url}")
                return forked_repo.clone_url, 200
            except Exception as e:
                print("Error in fork_repo method: "+str(e))
                return "", 500

    def process_repo(repo_url, local_working_dir):
        # Define the local directory
        #local_dir =r"C:\Users\Jawad.SalmanS\Downloads\AssessmentTool"
        local_dir = local_working_dir
        # Create the directory if it doesn't exist
        if not os.path.exists(local_dir):
            os.makedirs(local_dir)
        
        # Clone the forked repository to the specified directory
        #os.system(f"git clone {repo_url} {local_dir}")
        # Using subprocess.run to handle spaces in the path
        subprocess.run(["git", "clone", repo_url, local_dir], check=True)
        
        # Process the files and folders in the cloned repo
        for root, dirs, files in os.walk(local_dir):
            for file in files:
                file_path = os.path.join(root, file)
                print(f"Processing file: {file_path}")
                # Add your file processing logic here

