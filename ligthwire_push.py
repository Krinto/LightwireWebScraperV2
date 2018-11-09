import json, logging, logging.config, os
from pushbullet import Pushbullet, Device

logger = logging.getLogger(__name__)
config = json.loads(open('./config.json').read())
pb = Pushbullet(config['pushbulletApiKey'])

def __initLogging():
    if os.path.exists(config['logConfigFile']):
        with open(config['logConfigFile']) as f:
            logging.config.dictConfig(json.load(f))
    else:
        logging.basicConfig(level='WARN')

def pushMessage(device, message):
    return device.push_note("Internet Usage Update", message)

def getUsersDevice():
    return pb.get_device(config['deviceToPush'])

def main():
    __initLogging()
    logger.debug(pb.devices)
    logger.debug(pushMessage(getUsersDevice(), "This is a test"))

if __name__ == '__main__':
    main()
