from selenium.webdriver.common.by import By
from DemoProject.Locators.locators import PageLocators

class LoginPage():

    def __init__(self, driver):
        self.driver = driver
# Locators
        self.txtbx_username = PageLocators.txtbx_username
        self.txtbx_password = PageLocators.txtbx_password
        self.btn_login = PageLocators.btn_login
        self.msg_invalidUsername = PageLocators.msg_invalidUsername

# Events

    def enter_username(self, username):
        self.driver.find_element(By.ID, self.txtbx_username).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.ID, self.txtbx_password).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.ID, self.btn_login).click()

    def check_invalid_username_message(self):
        msg= self.driver.find_element(By.XPATH, self.msg_invalidUsername).text
        return msg


