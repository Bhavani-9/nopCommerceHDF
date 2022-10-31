import time

import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import logGen

class Test_001_Login:
    baseURL = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getPassword()

    logger=logGen.loggeneration()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_homePageTitle(self,setUp):
        self.logger.info("************ Test_001_Login *************")
        self.logger.info("************ Verifying home page title *************")
        self.driver= setUp
        self.driver.get(self.baseURL)
        act_title=self.driver.title
        print("Actual title is in first test ",act_title)
        if act_title=="Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("************ home page title test is passed *************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homePageTitle.png")
            assert False
            self.driver.close()
            self.logger.error("************ home page title test is failed *************")

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self,setUp):
        self.logger.info("************ Verifying login test *************")
        self.driver = setUp
        self.driver.get(self.baseURL)
        self.lp=LoginPage(self.driver)
        time.sleep(5)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.login()
        act_title=self.driver.title
        print("Actual title in second test ",act_title)
        if act_title=="Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
            self.logger.info("************ login test is passed *************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageTitle.png")
            assert False
            self.driver.close()
            self.logger.error("************ login test is failed *************")
