import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class AddCustomer:
    # Add Customer Page
    lnkCustomers_menu_xpath="/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/a"
    lnkCustomers_Submenu_xpath="/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/ul/li[1]/a/p"
    btnAddNew_xpath="//a[@class='btn btn-primary']"
    txtEmail_id="Email"
    txtPassword_id="Password"
    txtFirstName_id="FirstName"
    txtLastName_id="LastName"
    rdMaleGender_id="Gender_Male"
    rdFemaleGender_id="Gender_Female"
    txtDOB_id="DateOfBirth"
    txtCompanyName_Xpath="//input[@id='Company']"
    lstItemVendor_id="VendorId"
    txtAdminContent_xpath="//textarea[@id='AdminComment']"
    txtCustomerRoles_xpath="//*[@id='customer-info']/div[2]/div[10]/div[2]/div/div[1]/div/div"
    lstItemRegistered_xpath="//span[normalize-space()='Registered']"
    lstItemAdministrators_xpath="//span[normalize-space()='Administrators']"
    lstItemGuests_Xpath="//*[@id='SelectedCustomerRoleIds_taglist']/li[1]/span[1]"
    lstItemVendors_xpath="//span[normalize-space()='Vendors']"
    btnSave_Xpath="//button[@name='save']"

    def __init__(self,driver):
        self.driver=driver

    def clickOnCustomerMenu(self):
        self.driver.find_element(By.XPATH,self.lnkCustomers_menu_xpath).click()

    def clickOnCustomerMenuItem(self):
        self.driver.find_element(By.XPATH,self.lnkCustomers_Submenu_xpath).click()

    def clickOnAddNew(self):
        self.driver.find_element(By.XPATH,self.btnAddNew_xpath).click()

    def setEmail(self,email):
        self.driver.find_element(By.ID,self.txtEmail_id).send_keys(email)

    def setPassword(self,password):
        self.driver.find_element(By.ID,self.txtPassword_id).send_keys(password)

    def setFirstName(self,fname):
        self.driver.find_element(By.ID,self.txtFirstName_id).send_keys(fname)

    def setLastName(self,lname):
        self.driver.find_element(By.ID,self.txtLastName_id).send_keys(lname)

    def setGender(self,gender):
        if gender=='Male':
            self.driver.find_element(By.ID,self.rdMaleGender_id).click()
        elif gender=='Female':
            self.driver.find_element(By.ID,self.rdFemaleGender_id).click()
        else:
            self.driver.find_element(By.ID,self.rdMaleGender_id).click()

    def setDOB(self,dob):
        self.driver.find_element(By.ID,self.txtDOB_id).send_keys(dob)

    def setCompanyName(self,comname):
        self.driver.find_element(By.XPATH,self.txtCompanyName_Xpath).send_keys(comname)

    def setCustomerRoles(self,role):
        self.driver.find_element(By.XPATH,self.txtCustomerRoles_xpath).click()
        time.sleep(5)
        if role=='Registered':
            self.listItem=self.driver.find_element(By.XPATH,self.lstItemRegistered_xpath)
            time.sleep(5)
        elif role=='Administrators':
            self.listItem=self.driver.find_element(By.XPATH,self.lstItemAdministrators_xpath)
        elif role=='Guests':
            # Here user can be registered or Guest , only one we can select
            self.driver.find_element(By.XPATH,"//*[@title='delete']").click()
            time.sleep(5)
            self.listItem=self.driver.find_element(By.XPATH,self.lstItemGuests_Xpath)
        elif role=='Registered':
            self.listItem=self.driver.find_element(By.XPATH,self.lstItemRegistered_xpath)
        elif role=='Vendors':
            self.listItem=self.driver.find_element(By.XPATH,self.lstItemVendors_xpath)
        else:
            self.driver.find_element(By.XPATH,self.lstItemGuests_Xpath)
        time.sleep(3)
        # self.listItem.click()  We are unable to use click option so we are using java script
        self.driver.execute_script("arguments[0].click;",self.listItem)

    def setManagerOfVendor(self,value):
        drp=Select(self.driver.find_element(By.ID,self.lstItemVendor_id))
        drp.select_by_visible_text(value)


    def setAdminContent(self,content):
        self.driver.find_element(By.XPATH,self.txtAdminContent_xpath).send_keys(content)

    def clickOnSave(self):
        self.driver.find_element(By.XPATH,self.btnSave_Xpath).click()
