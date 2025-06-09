import logging


class LogGen:

    @staticmethod
    def loggen():
        logger = logging.getLogger(__name__)

        filehandler = logging.FileHandler(".\\Logs\\automation.log")
        logger.addHandler(filehandler)
        logger.setLevel(logging.INFO)
        return logger
