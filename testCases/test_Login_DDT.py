import time

import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import logGen
from utilities import XLUtils

class Test_002_DDT_Login:                            # (Data Driven Testing)
    baseURL = ReadConfig.getApplicationUrl()
    path=".//TestData/nopcommerceTestData.xlsx"
    logger=logGen.loggeneration()

    @pytest.mark.regression
    def test_login_ddt(self,setUp):
        self.logger.info("************ Verifying login DDT test *************")
        self.driver = setUp
        self.driver.get(self.baseURL)
        self.lp=LoginPage(self.driver)
        self.rows=XLUtils.getRowCount(self.path,'Data')
        print("Number of rows in an excel",self.rows)
        list_status=[]
        for r in range(2,self.rows+1):
            self.user=XLUtils.readData(self.path,'Data',r,1)
            self.password=XLUtils.readData(self.path,'Data',r,2)
            self.exp=XLUtils.readData(self.path,'Data',r,3)
            self.lp.setUsername(self.user)
            self.lp.setPassword(self.password)
            self.lp.login()
            time.sleep(5)

            act_title=self.driver.title
            exp_title="Dashboard / nopCommerce administration"

            if act_title==exp_title:
                if self.exp=="Pass":
                    self.logger.info("****** Passed ******")
                    time.sleep(5)
                    self.lp.logout()
                    time.sleep(5)
                    list_status.append("Pass")
                elif self.exp=="Fail":
                    self.logger.info("****** Failed ******")
                    time.sleep(5)
                    self.lp.logout()
                    time.sleep(5)
                    list_status.append("Pass")
            elif act_title!=exp_title:
                if self.exp=="Pass":
                    self.logger.info("****** Failed ******")
                    list_status.append("Fail")
                elif self.exp=="Fail":
                    self.logger.info("****** Passed ******")
                    list_status.append("Pass")

        if "Fail" not in list_status:
            self.logger.info("******* Login DDT test passed ******")
            print("Login DDT testing passed")
            self.driver.close()
            assert True
        else:
            self.logger.info("******* Login DDT test failed ******")
            print("Login DDT testing failed")
            self.driver.close()
            assert False
        self.logger.info("***** End of login DDT test *****")
        self.logger.info("***** Test_002_DDT_Login is completed *****")
