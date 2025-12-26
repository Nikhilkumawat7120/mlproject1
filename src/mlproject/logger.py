import logging
import os
from datetime import datetime

LOG_FILE="{datetime.now().strftime('%m_%d_%Y_%H_%M_%S)}.log"
#datetime ayyega month -date-year,hour-min-sec.
log_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(log_path,exist_ok=True)

LOG_FILE_PATH=os.path.join(log_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,#YE IK formate h jo ki darshata h ki mera log ka message kesa dikhe.
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,#yaha se ham .error .warning bhi setup kar sakte h 

)