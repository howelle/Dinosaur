# Dinosaur App
# Erin Howell
# Summer 2016
# File to Configure the Database

# import module that will allow the file to read the config file
from configparser import ConfigParser

# Specify the config file
CONFIG_FILE = 'settings.cfg'

# Use the config parser to read the config file
app_config = ConfigParser()
app_config.read(CONFIG_FILE)
