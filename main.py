import json, logging, logging.config, os
import requests
from requests.auth import HTTPBasicAuth
from bs4 import BeautifulSoup

logger = logging.getLogger(__name__)
config = json.loads(open('./config.json').read())

def initLogging():
    if os.path.exists(config['logConfigFile']):
        with open(config['logConfigFile']) as f:
            logging.config.dictConfig(json.load(f))
    else:
        logging.basicConfig(level='WARN')

def authenticateWithLightwire():
    payload = { "input-login": config['userName'], 'input-password': config['password'] ,'input-submit':'Login' }
    response = requests.post('https://account.lightwire.co.nz/authenticate', data=payload, verify=True)
    logger.info(response.url)
    return response

def successfullyAuthenticated(page):
    if(page.url == 'https://account.lightwire.co.nz/overview'):
        return True
    return False

def parseDataUsageFromPage(page):
    soup = BeautifulSoup(page.text, 'html.parser')
    legend = soup.find(class_='progress-legend-wrap')
    usage_list = legend.find_all('span')
    remaining_data = float(usage_list[0].string.split(' ', 1)[0])
    used_data = float(usage_list[1].string.split(' ', 1)[0])
    total_data = remaining_data + used_data
    return { 'remaining' : remaining_data, 'used' : used_data, 'total' : total_data }

def main():
    initLogging()
    response = authenticateWithLightwire()
    if successfullyAuthenticated(response):
        logger.debug('success')
        logger.debug(parseDataUsageFromPage(response))
    else:
        logger.debug('failed')

if __name__ == '__main__':
    main()
