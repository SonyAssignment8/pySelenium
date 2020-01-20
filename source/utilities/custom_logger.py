import inspect
import logging
from venv import logger
def customLogger(logLevel=logging.DEBUG):
    # gets the name of the class /methods form where this method is called
    loggerName=inspect.stack()[1][3]
    #logger=logging.getLogger(loggerName)
    #by defaul ,log all messages
    logger.setLevel(logging.DEBUG)

    fileHandler=logging.FileHandler("C:\\Users\\rashmi\\amazon_app\\resources\\reports\\log_report\\automation.log",mode='a')
    fileHandler.setLevel(logLevel)
    formatter=logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s',datefmt='%m/%d/%Y %I:%M:%S %p')
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)
    return logger

