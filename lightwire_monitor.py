import json, logging, logging.config, os, time
from apscheduler.schedulers.background import BackgroundScheduler
from scraping_service import get_usage_data
from pushbullet_service import notifyUser

logger = logging.getLogger(__name__)
with open('./config.json', encoding='utf-8') as data_file:
    config = json.loads(data_file.read())
internetAvailable = True
shouldNotify = True
threshold = 400

def __initLogging():
    if os.path.exists(config['logConfigFile']):
        with open(config['logConfigFile']) as f:
            logging.config.dictConfig(json.load(f))
    else:
        logging.basicConfig(level='WARN')

def checkDataUsageThresholds():
    global shouldNotify
    if internetAvailable:
        usageData = get_usage_data()
        if float(usageData.getDataUsed()) > threshold:
            if shouldNotify:
                shouldNotify = False
                notifyUser(usageData.formatUsageMessage())
                logger.debug('Over threshold {}'.format(usageData.getDataUsed()))
        else:
            shouldNotify = True
            logger.debug('Under threshold {}'.format(usageData.getDataUsed()))

def checkCanConnect():
    global internetAvailable
    if canReachLightwire():
        internetAvailable = True
        recordLatency()
    else:
        internetAvailable = False
        recordUnavailable()

def canReachLightwire():
    logger.debug('canReachLightwire')
    return True

def recordLatency():
    # record current ping
    logger.debug('recordLatencyTestResults')

def recordUnavailable():
    # record internet down
    logger.debug('recordUnavailable')       

def main():
    __initLogging()
    scheduler = BackgroundScheduler()
    scheduler.add_job(checkDataUsageThresholds, 'interval', minutes=30)
    #scheduler.add_job(checkCanConnect, 'interval', minutes=5)
    scheduler.start()
    logger.info('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))
    try:
        # This is here to simulate application activity (which keeps the main thread alive).
        while True:
            time.sleep(5)
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()
        logger.info('Shutting down usage monitor')

if __name__ == '__main__':
    main()
