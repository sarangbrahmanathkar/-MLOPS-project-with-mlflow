import os
import sys
import logging

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"#time log level and module name and message 

log_dir = "logs"
log_filepath = os.path.join(log_dir,"running_logs.log")
os.makedirs(log_dir, exist_ok=True)


logging.basicConfig(
    level= logging.INFO,
    format= logging_str,

    handlers=[
        logging.FileHandler(log_filepath),#it will create the log folder sand save it 
        logging.StreamHandler(sys.stdout)#print the log in terminal
    ]
)

logger = logging.getLogger("mlopsProjectLogger")#iniyialize the logger name 