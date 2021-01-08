import configparser
config = configparser.ConfigParser()

config.read('config.ini')

PRIVATE_KEY = config["CERTIFICATE"]["PRIVATE_KEY_PATH"]
