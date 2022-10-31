import random
import string
import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import logGen
from pageObjects.AddCustomerPage import AddCustomer

class Test_003_AddCustomer:
    baseURL = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getPassword()

    logger=logGen.loggeneration()

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_addCustomer(self,setUp):
        self.logger.info("************ Test_003_AddCustomer *************")
        self.driver= setUp
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.login()
        self.logger.info("********Login Successful******")
        self.logger.info("***** Starting add customer ****")

        self.addCust=AddCustomer(self.driver)    # AddCustomer id class name
        self.addCust.clickOnCustomerMenu()
        self.addCust.clickOnCustomerMenuItem()
        self.addCust.clickOnAddNew()

        self.logger.info("*****Providing Customer Info *****")

        self.email=random_generator()+"@gmail.com"
        self.addCust.setEmail(self.email)
        self.addCust.setPassword("test123")
        self.addCust.setCustomerRoles("Registered")
        self.addCust.setManagerOfVendor("Vendor 2")
        self.addCust.setGender("Female")
        self.addCust.setFirstName("Hiral")
        self.addCust.setLastName("Bhisetti")
        self.addCust.setDOB("12/06/1994") # Format D/M/Y
        self.addCust.setCompanyName("Amazon")
        self.addCust.setAdminContent("This is for testing.....")
        self.addCust.clickOnSave()


        self.logger.info("**** Saving customer info ****")

        self.logger.info("***** Add Customer Validation started *****")

        self.msg=self.driver.find_element(By.XPATH,"//div[@class='alert alert-success alert-dismissable']").text

        print(self.msg)
        if "The new customer has been added successfully." in self.msg:
            assert True==True
            self.logger.info("****** Add Customer Test Passed ****")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_addCustomer_scr.png")  # Screenshot
            self.logger.error("****** Add Customer Test Failed *****")
            assert True==False
        self.driver.close()
        self.logger.info("***** Ending Home Page Title Test *****")

def random_generator(size=8, chars=string.ascii_lowercase+string.digits):
            return ''.join(random.choice(chars) for x in range(size))

