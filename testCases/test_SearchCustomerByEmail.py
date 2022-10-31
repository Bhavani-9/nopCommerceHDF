import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from pageObjects.LoginPage import LoginPage
from pageObjects.SearchCustomerPage import SearchCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import logGen
from pageObjects.AddCustomerPage import AddCustomer

class Test_SearchCustomerByEmail_004:
    baseURL = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getPassword()

    logger = logGen.loggeneration()

    def test_searchCustomerByEmail(self,setUp):
        self.logger.info("*****SearchCustomerBtEmail_004*****")
        self.driver=setUp
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp=LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.login()
        self.logger.info("****** Login Successful ******")

        self.addCust = AddCustomer(self.driver)  # AddCustomer id class name
        self.addCust.clickOnCustomerMenu()
        self.addCust.clickOnCustomerMenuItem()

        self.logger.info("******* Searching customer by emailId ******")
        searchCust=SearchCustomer(self.driver)
        searchCust.setEmail("victoria_victoria@nopCommerce.com")
        searchCust.searchBtn()
        time.sleep(5)
        status=searchCust.searchCustomerByEmail("victoria_victoria@nopCommerce.com")
        assert True == status
        self.logger.info("******* TC_SearchCustomerByEmail_004 Finished ********")
        self.driver.close()

