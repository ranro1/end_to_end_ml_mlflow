#####################################################
# Contructor, creates logging format instead of
# creating a seperate file. Also, creates a log
# folder that saves logs to help us debug.
#####################################################

import os
import sys
import logging

# ASCII-time, loglevel, module, message
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

# Creates logging folder
log_dir = "logs"
log_filepath = os.path.join(log_dir,"running_logs.log")
os.makedirs(log_dir, exist_ok=True)

# Configures the logging format
logging.basicConfig(
    level=logging.INFO,
    format=logging_str,

    handlers=[
        logging.FileHandler(log_filepath), # save the logs inside log_filepath
        logging.StreamHandler(sys.stdout) # print the log in the terminal
    ]
)

# Initializes logging
logger =logging.getLogger("mlProjectLogger")