from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginPage:
    textbox_username_id="Email"
    textbox_password_id="Password"
    login_button_xpath="//button[@type='submit']"
    logout_button_xpath="//a[normalize-space()='Logout']"

    def __init__(self, driver):
        self.driver = driver

    def setUsername(self,username):
        self.driver.find_element(By.ID,self.textbox_username_id).clear()
        self.driver.find_element(By.ID,self.textbox_username_id).send_keys(username)

    def setPassword(self,password):
        self.driver.find_element(By.ID,self.textbox_password_id).clear()
        self.driver.find_element(By.ID,self.textbox_password_id).send_keys(password)

    def login(self):
        self.driver.find_element(By.XPATH,self.login_button_xpath).click()

    def logout(self):
        self.driver.find_element(By.XPATH,self.logout_button_xpath).click()

