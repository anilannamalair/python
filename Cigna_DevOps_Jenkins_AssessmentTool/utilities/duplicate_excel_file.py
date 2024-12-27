from config import configuration as config
import os
import shutil

class DUPLICATE_EXCEL_FILE:
    
    def __init__(self):
        
        self.name="assessment per repo"

    def duplicate_excel_file(src_file, dest_folder, dest_file_name):
        try:
            # Create the destination file path
            dest_file_path = os.path.join(dest_folder, dest_file_name)
            # Duplicate the file
            shutil.copy(src_file, dest_file_path)
            return dest_file_path, 200
        except Exception as e:
                print("Error in duplicate_excel_file method: "+str(e))
                return "", 500