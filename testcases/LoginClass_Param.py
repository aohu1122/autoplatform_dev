from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.chrome.options import Options

chrome_options1 = Options()
chrome_options1.add_argument('--headless')
chrome_options1.add_argument('--no-sandbox')
chrome_options1.add_argument('--disable-dev-shm-usage')

class Login():
    def user_login_init_chrome(self):
        driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver", chrome_options=chrome_options1)
        driver.implicitly_wait(10)
        driver.get('http://192.168.202.112/sso')
        driver.implicitly_wait(10)
        return driver

    def user_login(self,driver,username,password):
        driver.find_element_by_name("id").clear()
        driver.find_element_by_name("id").send_keys(username)

        driver.find_element_by_name("pwd").clear()
        driver.find_element_by_name("pwd").send_keys(password)

        element = driver.find_element_by_id("btlogin")
        ActionChains(driver).click(element).perform()

    def user_logout(self,driver):
        driver.find_element_by_xpath("//li[@class='dropdown user user-menu']").click()
        driver.find_element_by_xpath("//i[@class='ace-icon fa fa-power-off']").click()
        # driver.switch_to_alert().accept()
        driver.find_element_by_xpath("//a[@class='layui-layer-btn0']").click()