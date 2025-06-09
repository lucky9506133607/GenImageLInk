import time
from builtins import print

import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test_homePageTitle(self, setup):
        self.logger.info("*************** Test_001_Login *****************")
        print("Worked")

        self.logger.info("****Started Home page title test ****")

        self.driver = setup
        self.logger.info("****Opening URL****")
        self.driver.get(self.baseURL)
        act_title = self.driver.title


        if act_title == "Your store. Login":
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homepageTitle.png")
            assert True
            self.logger.info("**** Home page title test is passed ****")
            self.driver.close()


        else:
            assert False
            self.logger.error("**** Home page title test failed****")

    def test_login(self,setup):
        self.logger.info("****Started Login Test****")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        self.driver.close()

        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.logger.info("****Login test passed ****")

        else:
            assert False
            self.logger.error("****Login test failed ****")

"For pull check"





