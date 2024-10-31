# save-login-name.py
# Save login name, date and time to tmp file in home directory of current user
# Code by Peter Stackebrandt

"""
Task by Kofler:Python.-2024, 15.7. W1 p. 292
Save the login name (getpass.getuser()), the date, and 
the time in the text file python-test-file.tmp in your 
home directory.

Parts
- get login name
- get date and local time  2024-12-24 12.25 AM/PM
- save them to python-test-file.tmp in home dir

"""

import getpass
import arrow
import os

OUT_FILE_NAME = "python-test-file.tmp"
TIME_FORMAT = "YYYY-MM-DD HH:mm A"

# Save login name and curr. time to temp file in user home directory.
def save_login_to_home_dir(login_name_p, temp_dir_p, out_file_name):
    current_time = arrow.now().format(TIME_FORMAT)
    
    # Create the tmp directory if it doesn't exist
    os.makedirs(temp_dir_p, exist_ok=True)

    file_path = os.path.join(temp_dir_p, out_file_name)

    # Write login name, date, and time to file
    with open(file_path, "w") as file:
        file.write(f"User: {login_name_p}\n")
        file.write(f"Date and time: {current_time}")
        
    return True 

# returns directory as string
def get_home_dir_of_current_user():
    return os.path.expanduser("~")

# returns directory as string    
def get_temporary_dir_within_dir(parent_dir):
    return os.path.join(parent_dir, "tmp")

def main():
    print("Save login name, date and time to tmp file in user home directory")
    
    home_dir = get_home_dir_of_current_user()
    temp_dir = get_temporary_dir_within_dir(home_dir)
    login_name = getpass.getuser() # string
    
    save_login_to_home_dir(login_name, temp_dir, OUT_FILE_NAME)

    print(f"Saved login name {login_name} to {OUT_FILE_NAME}")
    print(f"see at {temp_dir}")
    print(f"Date and time: {arrow.now().format(TIME_FORMAT)}")

if __name__ == "__main__":
    main()