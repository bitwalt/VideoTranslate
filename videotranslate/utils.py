import logging 
import sys
import os 
import json

def set_logger(output_dir: str, log_file: str):
    # set logger on log file and stdout
    log_dir = os.path.join(output_dir, "logs")
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)        
    logging.basicConfig(filename=os.path.join(log_dir, log_file),
                        encoding='utf-8', 
                        level=logging.INFO,
                        format='%(asctime)s:%(levelname)s:%(message)s')
    logging.getLogger().addHandler(logging.StreamHandler(sys.stdout))
    
def load_config(conf_file: str):
    with open(conf_file, "r") as f:
        conf = json.load(f)
    return conf