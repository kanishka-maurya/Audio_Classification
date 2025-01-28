from logging import *
import os
import sys

logs_dir = "logs"
os.makedirs(logs_dir,exist_ok = True)
log_filepath = os.path.join(logs_dir , "running_logs.log")
log_str = "[%(asctime)s]: %(levelname)s: %(module)s: %(message)s"

# metadata of logging -- logging message to running_logs.log file in logs folder.
basicConfig(
    level = INFO,
    format = log_str,
    handlers = [
        FileHandler(log_filepath),
        StreamHandler(sys.stdout)
]
    )

# creating logger object
logger = getLogger("audioVisionLogger")
