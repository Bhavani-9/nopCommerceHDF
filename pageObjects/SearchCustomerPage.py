import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class SearchCustomer():
    txtEmail_id="SearchEmail"
    txtFirstName_id="SearchFirstName"
    txtLastName_id="SearchLastName"
    btnSearch_id="search-customers"
    tdl_Xpath="//*[@id='customers-grid']"
    tblRow_xpath="//*[@id='customers-grid']//tbody/tr"
    tblColumn_xpath="//*[@id='customers-grid']//tbody/tr/td"


    def __init__(self,driver):
        self.driver=driver

    def setEmail(self,email):
        self.driver.find_element(By.ID,self.txtEmail_id).clear()
        self.driver.find_element(By.ID,self.txtEmail_id).send_keys(email)

    def setFirstName(self,fname):
        self.driver.find_element(By.ID,self.txtFirstName_id).clear()
        self.driver.find_element(By.ID,self.txtFirstName_id).send_keys(fname)

    def setLastName(self,lname):
        self.driver.find_element(By.ID,self.txtLastName_id).clear()
        self.driver.find_element(By.ID,self.txtLastName_id).send_keys(lname)

    def searchBtn(self):
        self.driver.find_element(By.ID,self.btnSearch_id).click()

    def numberOfRows(self):
        return len(self.driver.find_elements(By.XPATH,self.tblRow_xpath))

    def numberOfColumns(self):
        return len(self.driver.find_elements(By.XPATH,self.tblColumn_xpath))

    def searchCustomerByEmail(self,email):
        flag=False
        for r in range(1,self.numberOfRows()+1):
            table=self.driver.find_element(By.XPATH,self.tdl_Xpath)
            emailid=table.find_element(By.XPATH,"//*[@id='customers-grid']/tbody/tr["+str(r)+"]/td[2]")
            if emailid==email:
                flag=True
                break
        return flag

    def searchCustomerByName(self,Name):
        flag=False
        for r in range(1,self.numberOfRows()+1):
            table=self.driver.find_element(By.XPATH,self.tdl_Xpath)
            name=table.find_element(By.XPATH,"//*[@id='customers-grid']/tbody/tr["+str(r)+"]/td[3]")
            if name==Name:
                flag=True
                break
        return flag