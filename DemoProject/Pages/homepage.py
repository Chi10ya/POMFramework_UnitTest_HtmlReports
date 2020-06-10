from selenium.webdriver.common.by import By
from DemoProject.Locators.locators import PageLocators

class HomePage():

    def __init__(self, driver):
        self.driver = driver
# Locators
        self.welcome_link_id = PageLocators.welcome_link_id
        self.logout_link_linkTest = PageLocators.logout_link_linkTest

# Events

    def click_welcome(self):
        self.driver.find_element(By.ID, self.welcome_link_id).click()

    def click_logout(self):
        self.driver.find_element(By.LINK_TEXT, self.logout_link_linkTest).click()


