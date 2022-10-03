import logging 
import sys
import os 
import json
import re
from urllib import parse
import requests

parse_price = lambda price: float(price.replace(',', ''))

def get_btc_price() -> float:    
    response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    data = response.json()
    return data["bpi"]["USD"]["rate"].split('.')[0]



def get_dollar_sat(btc_price) -> str: 
    btc_float = parse_price(btc_price)
    dollar_sat = dollar_to_sat(btc_float)
    return str(dollar_sat)

dollar_to_sat = lambda usd_price: int(1 / usd_price * (10 ** 8))

def sats_to_dollar(tot_sats: int, dollar_in_sat: str):
    return tot_sats / int(dollar_in_sat)

    
def is_from_youtube(url:str) -> bool:
    youtube_regex = (
        r'(https?://)?(www\.)?'
        '(youtube|youtu|youtube-nocookie)\.(com|be)/'
        '(watch\?v=|embed/|v/|.+\?v=)?([^&=%\?]{11})')
    return re.match(youtube_regex, url)


def get_youtube_id(url:str) -> str:
    """
    Examples:
    - http://youtu.be/SA2iWivDJiE
    - http://www.youtube.com/watch?v=_oPAwA_Udwc&feature=feedu
    - http://www.youtube.com/embed/SA2iWivDJiE
    - http://www.youtube.com/v/SA2iWivDJiE?version=3&amp;hl=en_US
    """
    query = parse.urlparse(url)
    if query.hostname == 'youtu.be':
        return query.path[1:]
    if query.hostname in ('www.youtube.com', 'youtube.com'):
        if query.path == '/watch':
            p = parse.parse_qs(query.query)
            return p['v'][0]
        if query.path[:7] == '/embed/':
            return query.path.split('/')[2]
        if query.path[:3] == '/v/':
            return query.path.split('/')[2]
    return ""

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