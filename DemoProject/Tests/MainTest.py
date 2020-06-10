from selenium import webdriver
from selenium.webdriver.common.by import By
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from DemoProject.Pages.loginpage import LoginPage
from DemoProject.Pages.homepage import HomePage
import unittest
import HtmlTestRunner


class MainTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        chromedriverpath = "C:\\Users\\chaitanya.mohammad\\PycharmProjects\\POMFramework_UnitTest_HtmlReports-AutoStepByStep\\webdrivers\\chromedriver.exe"
        cls.driver = webdriver.Chrome(executable_path=chromedriverpath)
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)

# Valid Login
    def test_01_LoginValid(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")
        objLogin = LoginPage(driver)
        objLogin.enter_username("Admin")
        objLogin.enter_password("admin123")
        objLogin.click_login()

# Home Page
        objHome = HomePage(driver)
        objHome.click_welcome()
        objHome.click_logout()


# Invalid Login
    def test_02_InvalidLogin(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")
        objLogin = LoginPage(driver)
        objLogin.enter_username("Admin1")
        objLogin.enter_password("admin123")
        objLogin.click_login()
        invalid_message = objLogin.check_invalid_username_message()
        self.assertEqual(invalid_message, "Invalid credentials")


# Tear Down
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print("Test Execution is completed")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\\Users\\chaitanya.mohammad\\PycharmProjects\\POMFramework_UnitTest_HtmlReports-AutoStepByStep\\Reports'))