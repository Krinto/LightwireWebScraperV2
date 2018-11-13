import json, logging, logging.config, os
from pushbullet import Pushbullet, Device

logger = logging.getLogger(__name__)
with open('./config.json', encoding='utf-8') as data_file:
    config = json.loads(data_file.read())
pb = Pushbullet(config['pushbulletApiKey'])

def __initLogging():
    if os.path.exists(config['logConfigFile']):
        with open(config['logConfigFile']) as f:
            logging.config.dictConfig(json.load(f))
    else:
        logging.basicConfig(level='WARN')

def __pushMessage(device, message):
    return device.push_note("Internet Usage Update", message)

def __getUsersDevice():
    return pb.get_device(config['deviceToPush'])

def notifyUser(message):
    __pushMessage(__getUsersDevice(), message)

def main():
    __initLogging()
    logger.debug(pb.devices)
    logger.debug(__pushMessage(__getUsersDevice(), "This is a test"))

if __name__ == '__main__':
    main()
