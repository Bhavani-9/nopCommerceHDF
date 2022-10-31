import configparser

config=configparser.RawConfigParser()
config.read(".\\Configurations/config.ini")


class ReadConfig:
    @staticmethod
    def getApplicationUrl():
        url=config.get("Common Data","baseURL")
        return url

    @staticmethod
    def getUserEmail():
        username=config.get("Common Data","username")
        return username

    @staticmethod
    def getPassword():
        password = config.get("Common Data", "password")
        return password

