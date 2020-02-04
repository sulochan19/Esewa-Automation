from selenium import webdriver
from time import sleep
from selenium.webdriver.support.select import Select

from credentials import esewa_username,worldlink_username, password

class EsewaAutomation():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get('https://esewa.com.np/#/home')
        sleep(3) #using sleep so that the elements gets load

        username_link=self.driver.find_element_by_xpath('//*[@id="loginForm"]/div[3]/div[1]/input[2]')
        username_link.send_keys(esewa_username) #enter your esewa id i.e your phone number

        password_link=self.driver.find_element_by_xpath('//*[@id="loginForm"]/div[3]/div[2]/input[2]')
        password_link.send_keys(password) #enter your password here

        login_btn=self.driver.find_element_by_xpath('//*[@id="loginForm"]/div[3]/div[3]')
        login_btn.click()

        sleep(3)

        internet_link=self.driver.find_element_by_xpath('//*[@id="showCaseTemplate"]/div/div[6]/div/div/div/data-owl-carousel/div[1]/div/div[4]/div/div/div[2]')
        internet_link.click()

        sleep(3)

        name=self.driver.find_element_by_xpath('//*[@id="username"]')
        name.send_keys(worldlink_username)#enter your worldlink username

        check_btn=self.driver.find_element_by_xpath('//*[@id="paymentForm"]/ng-include[1]/div[1]/button')
        check_btn.click()

        sleep(3)
        selected_plan = self.driver.find_element_by_xpath('//*[@id="planCategory"]')
        selected_plan.click()
        plan_detail=Select(self.driver.find_element_by_xpath('//*[@id="planCategory"]'))
        sleep(3)
        plan_detail.select_by_index(1) #use different index value if you have a different internet plan
        selected_plan.is_selected()
        selected_plan.click()

        proceed_btn=self.driver.find_element_by_xpath('// *[ @ id = "es-payment-proceed"]')
        proceed_btn.click()

        sleep(5)
        confirm_btn=self.driver.find_element_by_xpath('/html/body/div[2]/div[3]/div/div/div/div/div/div[2]/div/div/div[4]/div/div[3]/button[1]')
        confirm_btn.click()


obj=EsewaAutomation()
obj.login()
