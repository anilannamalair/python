
from config import configuration as config
from utilities.git_clone_localy import GIT_CLONE as local_folder_creator
from utilities.duplicate_excel_file import DUPLICATE_EXCEL_FILE
from utilities.jenkinfile_find_and_read import JENKINFILE_FIND_AND_READ
from utilities.parameters_rules.number_of_stages import NO_OF_STAGES
from utilities.parameters_rules.pipeline_script_complexity import PIPELINE_SCRIPT_COMPLEXITY
from utilities.parameters_rules.triggers_details import TRIGGERS_DETAILS
from utilities.parameters_rules.variables_finder import VARIABLES_FINDER
from utilities.update_assessment_report import UPDATE_ASSESSMENT_REPORT
from utilities.parameters_rules.artifact_management import ARTIFACT_MANAGEMENT
from utilities.parameters_rules.error_handling_and_retry_logic import ERROR_HANDLING_AND_RETRY_LOGIC
from utilities.parameters_rules.approval_gates import APPROVAL_GATES
from utilities.parameters_rules.number_of_parallel_execution import NO_OF_PARALLEL_EXECUTION
from utilities.parameters_rules.number_of_libraries import NO_OF_LIBRARIES
from utilities.parameters_rules.complexity_classifier import COMPLEXITY_CLASSIFIER
from utilities.parameters_rules.external_integrations import EXTERNAL_INTEGRATIONS
from utilities.parameters_rules.testing_and_code_quality_checks import TESTING_AND_CODE_QUALITY_CHECKS
from utilities.parameters_rules.security_and_compliance_checks import SECURITY_AND_COMPLIANCE_CHECKS
from utilities.parameters_rules.cloud_infra_and_containerization import CLOUD_INFRA_AND_CONTAINERIZATION
from utilities.parameters_rules.repository import REPOSITORY
from utilities.parameters_rules.number_of_environments_or_deployments import NUMBER_OF_ENVIRONMENTS_OR_DEPLOYMENTS
from utilities.logging import log_message
import datetime as dt

class ASSESSMENT_PER_REPO:
    
    def __init__(self):
        
        self.name="assessment per repo"

    def assessment_per_repo_func(repo_url,repo_token,local_working_dir):
        log_message ("Working on repo "+str(repo_url), "Info")
        #repo_url = input("Enter the GitHub repository URL: ")
        #repo_url = "https://github.com/subhayanwb/Jenkins2GithubActionsPOC"
        #repo_url = config.GITHUB_REPO_URL
        # Fork the repository
        forked_repo_url, response_code = local_folder_creator.fork_repo(repo_url,repo_token)
        if response_code == 200:
            # Clone the forked repository to the specified directory
            # Process the files and folders in the cloned repo as part of validation
            local_folder_creator.process_repo(forked_repo_url,local_working_dir)

            # Run parameters rules
            #jenkins_folder_path=config.LOCAL_DIR
            jenkins_folder_path=local_working_dir
            #excel_file_path = config.GENERIC_ASSESSMENT_REPORT
            number_of_environments=0
            # Duplicate the excel file
            #duplicated_excel_path, response_code = DUPLICATE_EXCEL_FILE.duplicate_excel_file(excel_file_path, jenkins_folder_path, 'Assessment_report.xlsx')
            
            # Find and read the Jenkinsfile
            jenkinsfile_content,jenkinsfile_path, response_code = JENKINFILE_FIND_AND_READ.find_read_jenkinsfile(jenkins_folder_path)
            if response_code == 200:

                # Count the number of stages in Jenkinsfile
                stages_count = NO_OF_STAGES.count_stages_in_jenkinsfile(jenkinsfile_content)

                # Identify the pipeline type
                pipeline_type = PIPELINE_SCRIPT_COMPLEXITY.identify_pipeline_type(jenkinsfile_content)
                print(pipeline_type)
                
                # Get Triggers count
                triggers_count,triggers_list = TRIGGERS_DETAILS.extract_triggers(jenkinsfile_content)
                print(f"Number of triggers: {triggers_count}")

                # Get environment variables containing lines in a file
                folder_path= local_working_dir
                variable_content_lines_with_dollar = VARIABLES_FINDER.find_lines_with_dollar_sign_environment_varaibles(folder_path)
                environment_variables_lines_file_path, response_code= VARIABLES_FINDER.write_output_to_file(folder_path, variable_content_lines_with_dollar)
                valid_variables = VARIABLES_FINDER.find_valid_variables(folder_path)
                # Get the list of variables
                variables_list = list(valid_variables.keys())
                #print("Variables List:", variables_list)

                # Get the total count of all variables
                #total_count = sum(valid_variables.values())
                total_variables_count = len(variables_list)
                #print("Total Count of Variables:", total_count)

                # Convert the list to a string
                variables_list_str = ', '.join(variables_list)

                # variables_passed_var = "Total Count of Variables: " + str(total_count) + "\n" + "Variables List: " + variables_list_str
                
                #variables_passed_var = "Total Count of Variables: " + str(total_variables_count) +"\n"+ "Variables List: " + str(variables_list)+ "\n" + "Variables List in string: " + variables_list_str


                


                # Check if Artifactory configuration is present in the Jenkinsfile.
                is_artifactory_present, artifactory_lines = ARTIFACT_MANAGEMENT.check_artifactory_in_jenkinsfile(jenkinsfile_content)
                if is_artifactory_present:
                    artifactory_present_msg = "Yes" #, Artifactory configuration is present in the Jenkinsfile."
                    # print("Artifactory configuration is present in the Jenkinsfile.")
                    # print("Artifactory lines:")
                    # for line in artifactory_lines:
                    #     print(line)
                else:
                    artifactory_present_msg = "No" #, Artifactory configuration is NOT present in the Jenkinsfile."
                    #print("Artifactory configuration is NOT present in the Jenkinsfile.")

                #Count number of try blocks and retry blocks from Jenkinsfile
                try_count, retry_count = ERROR_HANDLING_AND_RETRY_LOGIC.count_try_and_retry_blocks(jenkinsfile_content)
                #print(f"Number of try blocks: {try_count}")
                #print(f"Number of retry blocks: {retry_count}")
                try_and_retry_count = "Error handling count = "+str(try_count)+", Retry count = "+str(retry_count)+"."
                
                # Count the number of Approval stages found in the Jenkinsfile
                approval_count = APPROVAL_GATES.count_approval_stages(jenkinsfile_content)
                #print(f"Number of 'Approval' stages: {approval_count}")

                # Count parallel execeution blocks from Jenkinsfile
                job_count, parallel_count = NO_OF_PARALLEL_EXECUTION.count_jobs_and_parallel_blocks(jenkinsfile_content)
                
                # Get the list of libraries mentioned in lines that start with 'library'
                libraries = NO_OF_LIBRARIES.get_libraries_from_jenkinsfile_content(jenkinsfile_content)
                #print(libraries)  # Print the list of libraries
                if len(libraries) == 0:
                    libraries_msg= "No libraries found" # in Jenkinsfile"
                else:
                    libraries_msg = str(libraries)


                # Get the complexity of the pipeline
                complexity_classification = COMPLEXITY_CLASSIFIER.classify_jenkinsfile(jenkinsfile_content)
                

                # Get list of external integration
                tools_first_words = EXTERNAL_INTEGRATIONS.extract_tools_section_first_words(jenkinsfile_path)
                external_integrations_var = tools_first_words
                # if tools_first_words:
                #     print("Integrations in 'tools' section:", tools_first_words)
                #     external_integrations_var = tools_first_words
                # else:
                #     print("'tools' section not found in the Jenkinsfile.")
                #     external_integrations_var = "No integrations found."
                
                # Get tools for testing and code quality checks from jenkinsfile with refernce to TESTING_TOOLS_LIST
                testing_tools_list = config.TOOLS_LIST
                # code is modified to look for Tools list in entire jenkinsfile, not just in tools section
                #found_tools = TESTING_AND_CODE_QUALITY_CHECKS.find_tools_in_jenkinsfile(jenkinsfile_path, testing_tools_list)
                found_tools = TESTING_AND_CODE_QUALITY_CHECKS.find_tools_in_jenkinsfile(jenkinsfile_content, testing_tools_list)

                testing_and_code_quality_checks_var = found_tools
                # if found_tools:
                #     print("Tools found in Jenkinsfile:", found_tools)
                #     testing_and_code_quality_checks_var = found_tools
                # else:
                #     print("No specified tools found in the Jenkinsfile.")
                #     testing_and_code_quality_checks_var = "No testing tools found."
                
                # Security and Compliance Checks -- SECURITY_TOOLS_LIST in jenkinsfile
                security_tools_list = config.SECURITY_TOOLS_LIST
                security_and_compliance_checks_list = SECURITY_AND_COMPLIANCE_CHECKS.find_security_tools_in_jenkinsfile(jenkinsfile_content, security_tools_list)

                # if security_and_compliance_checks_list:
                    
                #     security_and_compliance_checks_list = security_and_compliance_checks_list
                # else:
                    
                #     security_and_compliance_checks_list = "No security and compliance tools found."

                # Cloud Infrastructure and Containerization -- CONTAINERIZATION_LIST in jenkinsfile
                containeration_tools_list = config.CONTAINERIZATION_LIST
                cloud_infrastructure_and_containerization_list = CLOUD_INFRA_AND_CONTAINERIZATION.find_containeration_tools_in_jenkinsfile(jenkinsfile_content, containeration_tools_list)

                # if cloud_infrastructure_and_containerization_list:
                    
                #     cloud_infrastructure_and_containerization_list = cloud_infrastructure_and_containerization_list
                # else:
                    
                #     cloud_infrastructure_and_containerization_list = "No cloud infra or containers found."

                # Repository -- from VERSIONING_TOOLS_DICT search with key in jenkisfile and if found return value
                repository_tools_dict = config.VERSIONING_TOOLS_DICT
                repository_list = REPOSITORY.find_repository_tools_in_jenkinsfile(jenkinsfile_content, repository_tools_dict)

                # if repository_list:
                    
                #     repository_list = repository_list
                # else:
                    
                #     repository_list = "No repository found."


                # Number of Environments/Deployments -- Get the count of stage which has 'deploy' word in it in the Jenkinsfile
                deploy_stage_count = NUMBER_OF_ENVIRONMENTS_OR_DEPLOYMENTS.count_deploy_stages(jenkinsfile_content)


                # Update the excel report with the found details
                #UPDATE_ASSESSMENT_REPORT.update_excel_report(duplicated_excel_path, stages_count, pipeline_type, triggers_count, is_artifactory_present, try_count, retry_count,approval_count, parallel_count)

                

                try_and_retry_count_msg= "Error handling count = "+str(try_count)+", Retry count = "+str(retry_count)+"."

                #return duplicated_excel_path, stages_count, pipeline_type, triggers_count, is_artifactory_present, try_count, retry_count,approval_count, parallel_count
                return {
                        'repo_url': repo_url,
                        'stages_count': stages_count,
                        'parallel_count': parallel_count,
                        'triggers_count': triggers_count,
                        'number_of_environments': deploy_stage_count,
                        'testing_and_code_quality_checks_var': testing_and_code_quality_checks_var,
                        'external_integrations_var': external_integrations_var,
                        'pipeline_type': pipeline_type,
                        'is_artifactory_present': artifactory_present_msg,
                        'try_and_retry_count': try_and_retry_count_msg,
                        'security_and_compliance_checks_var': security_and_compliance_checks_list,
                        'approval_count': approval_count,
                        'cloud_infrastructure_and_containerization_var': cloud_infrastructure_and_containerization_list,
                        'repository_var': repository_list,
                        'variables_passed_var': total_variables_count,
                        'configuration_parameters_or_values_var': variables_list_str,
                        'libraries': libraries_msg,
                        'complexity_var': complexity_classification
                    }

                
            
            
            



        else:
            print("Assessment Tool Stopped.")
            
