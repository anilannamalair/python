import os
import datetime
from config import configuration as config

def log_message(message, log_type):
    """
    Logs a message to a file with a timestamp and type.
    
    Parameters:
    message (str): The message to log.
    log_type (str): The type of the log ('Error', 'Info', 'Warning').
    """
    # Define the log file path
    #log_file_path = r'C:\Users\Jawad.SalmanS\Documents\Cigna\workshop\research\Repo\python_execution_log.txt'
    
    # Define the local directory path
    local_dir = config.LOCAL_DIR
    
    # Form the complete log file path
    log_file_path = os.path.join(local_dir, 'python_execution_log.txt')

    # Check if the log file exists, create it if it doesn't
    if not os.path.exists(log_file_path):
        with open(log_file_path, 'w') as log_file:
            log_file.write('')  # Create an empty file
    
    # Get the current timestamp
    current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    # Format the log entry
    log_entry = f"{current_time} - {log_type} - {message}\n"
    
    # Append the log entry to the file
    with open(log_file_path, 'a') as log_file:
        log_file.write(log_entry)


# if __name__ == "__main__":
#     log_message("This is an info message.", "Info")
#     log_message("This is a warning message.", "Warning")
#     log_message("This is an error message.", "Error")
