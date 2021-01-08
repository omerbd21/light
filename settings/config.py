import configparser
config = configparser.ConfigParser()

config.read('settings/config.ini')

PRIVATE_KEY = config.get("CERTIFICATE","PRIVATE_KEY_PATH")
