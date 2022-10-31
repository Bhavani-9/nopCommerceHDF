import logging

class logGen:
    @staticmethod
    def loggeneration():
        logger = logging.getLogger()
        fhandler = logging.FileHandler(filename='.\\Logs\\mylog.log', mode='a')
        formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(message)s', datefmt=' % m / % d / % Y % I: % M: % S % p')
        fhandler.setFormatter(formatter)
        logger.addHandler(fhandler)
        return logger

#'%(asctime)s: %(levelname)s: %(message)s'