import json, logging, logging.config, os
import requests
from requests.auth import HTTPBasicAuth
from bs4 import BeautifulSoup
from utilities import time_cache
from models.dataUsage import DataUsage

logger = logging.getLogger(__name__)
with open('./config.json', encoding='utf-8') as data_file:
    config = json.loads(data_file.read())
timespan = 60 * 15

def __initLogging():
    if os.path.exists(config['logConfigFile']):
        with open(config['logConfigFile']) as f:
            logging.config.dictConfig(json.load(f))
    else:
        logging.basicConfig(level='WARN')

def __authenticateWithLightwire():
    payload = { "input-login": config['userName'], 'input-password': config['password'] ,'input-submit':'Login' }
    response = requests.post('https://account.lightwire.co.nz/authenticate', data=payload, verify=True)
    return response

def __successfullyAuthenticated(page):
    if(page.url == 'https://account.lightwire.co.nz/overview'):
        return True
    return False

def __parseDataUsageFromPage(page):
    soup = BeautifulSoup(page.text, 'html.parser')
    legend = soup.find(class_='progress-legend-wrap')
    usage_list = legend.find_all('span')
    remaining_data = float(usage_list[0].string.split(' ', 1)[0])
    used_data = float(usage_list[1].string.split(' ', 1)[0])
    
    return DataUsage(used_data, remaining_data)


@time_cache(timespan)
def get_usage_data():
    response = __authenticateWithLightwire()
    if __successfullyAuthenticated(response):
        return __parseDataUsageFromPage(response)
    else:
        return { 'error' : 'failed to authenticate' }

def main():
    __initLogging()
    response = __authenticateWithLightwire()
    if __successfullyAuthenticated(response):
        logger.debug('success')
        logger.debug(__parseDataUsageFromPage(response).formatUsageMessage())
    else:
        logger.debug('failed')

if __name__ == '__main__':
    main()
