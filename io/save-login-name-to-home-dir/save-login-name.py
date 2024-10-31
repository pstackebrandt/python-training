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

print("Save login name, date and time to tmp file in user home directory")

login_name = getpass.getuser()
print(f"login-name: {login_name}")

current_time = arrow.now().format("YYYY-MM-DD HH:MM A")
print(current_time)

home_dir = os.path.expanduser("~")
tmp_dir = os.path.join(home_dir, "tmp")

# Create the tmp directory if it doesn't exist
os.makedirs(tmp_dir, exist_ok=True)

# Define the file path within the tmp directory
file_path = os.path.join(tmp_dir, OUT_FILE_NAME)

# Write the login name, date, and time to the file
with open(file_path, "w") as file:
    file.write(f"User: {login_name}\n")
    file.write(f"Date and time: {current_time}")

print(f"Saved login name {login_name} to {OUT_FILE_NAME}")
print(f"see at {tmp_dir}")
 