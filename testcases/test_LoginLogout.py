from time import sleep
import unittest
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from testcases.LoginClass_Param import *

class TestLogin(unittest.TestCase):
    def setUp(self):
        login_instance = Login()
        #self.driver = Login().user_login_init_chrome(self)
        self.driver = login_instance.user_login_init_chrome()

    def test_LoginLogout(self):
        Login().user_login(self.driver,'张科','123456')

        title = self.driver.title
        self.assertEqual(title,"红岛经济区应急平台")
        sleep(3)

        Login().user_logout(self.driver)

        title_out = self.driver.title

        self.assertEqual(title_out,"红岛经济区应急平台")

    def test_LoginLogout1(self):
        Login().user_login(self.driver,'张科','123456')

        title = self.driver.title
        self.assertEqual(title,"红岛经济区应急平台1")
        sleep(3)

        Login().user_logout(self.driver)

        title_out = self.driver.title

        self.assertEqual(title_out,"红岛经济区应急平台")

    def tearDown(self):
        self.driver.quit()

class TestLogout(unittest.TestCase):
    def setUp(self):
        self.driver = Login().user_login_init_chrome()

    def test_Logout(self):
        Login().user_login(self.driver,'张科','123456')

        title = self.driver.title
        self.assertEqual(title,"红岛经济区应急平台")
        sleep(3)

        Login().user_logout(self.driver)

        title_out = self.driver.title

        self.assertEqual(title_out,"红岛经济区应急平台")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()