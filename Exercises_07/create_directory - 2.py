""" 
directory_utilities.py 
By: JOR 
Date: 01OCT22 
""" 
import os, platform

def create_directory(directory_name: str) ->bool: 
    # Check to see if the directory already exists 
    if os.path.isdir(directory_name):
        # The directory already exists 
        return 2 
    else: 
        # Use try/except to catch errors
        try: 
            # Create the directory
            os.mkdir(directory_name)
            # If this worked, return True
            return 0
        except:
            # Give an explicit error message
            print("Error creating directory {directory_name}")
            # If this did not work, return False
            return 1
    
if create_directory("JOR") == 0: 
    print("Creating a directory worked") 
        # Do other stuff 
elif create_directory("JOR") == 1: 
    print("You couldn't create a directory!") 
        # Do other stuff 
elif create_directory("JOR") == 2: 
    print("Directory already existed!") # Do other stuff