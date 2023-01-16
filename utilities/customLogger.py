import logging

class LogGenerator:

    @staticmethod
    def loggen():
        # logging.basicConfig(filename=".\\Logs\\automation.log",
        #                     format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        logger = logging.getLogger()
        fhandler=logging.FileHandler(filename='.\\Logs\\automation.log',mode='a')
        formatter=logging.Formatter('%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        # logger.setLevel(logging.INFO)
        fhandler.setFormatter(formatter)
        logger.addHandler(fhandler)
        return logger