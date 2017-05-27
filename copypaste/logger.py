#! python

#TODO define JSON configuration file to handle loggers

import logging

logger = logging.getLogger('global_logger')
logger.setLevel(logging.DEBUG) # TODO lower the level
fileHandler = logging.FileHandler('logger.log')
fileHandler.setLevel(logging.DEBUG)
consoleHandler = logging.StreamHandler()
consoleHandler.setLevel(logging.DEBUG)
formatter = logging.Formatter(
        '%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
consoleHandler.setFormatter(formatter)
fileHandler.setFormatter(formatter)
logger.addHandler(consoleHandler)
logger.addHandler(fileHandler)

logger.info("Here we go !")