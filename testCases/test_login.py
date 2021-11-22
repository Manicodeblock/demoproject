import time
from selenium import webdriver
import pytest
from pageObjects.LoginPage import Loginpage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    #these two sanity and regression for groping concepts
    @pytest.mark.regression
    def test_homepage_title(self, setup):
        self.logger.info("*****Test_001_login*****")
        self.logger.info("*****verifying home page title*****")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        if act_title == "Yourddd store. Login":
            assert True
            self.driver.close()
            self.logger.info("*****Home page title test is passed*****")
        else:
            self.driver.save_screenshot(
                "/home/ticvictech/PycharmProjects/nopcommerceProject/Screenshots/" + "checkhomepagetitle.png")
            self.driver.close()
            self.logger.error("*****Home page title test is failed*****")
            assert False

    @pytest.mark.sanity  # these two sanity and regression for groping concepts
    @pytest.mark.regression
    def test_login(self, setup):
        self.logger.info("*****Veryfing login test*****")
        self.driver = setup
        time.sleep(4)
        self.driver.get(self.baseURL)
        time.sleep(4)
        self.lp = Loginpage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clicklogin()
        act_title=self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.logger.info("*****Login test successsfull*****")
            self.driver.close()
        else:
            self.driver.save_screenshot("/home/ticvictech/PycharmProjects/nopcommerceProject/Screenshots/" + "checklogin.png")
            self.driver.close()
            self.logger.error("*****Login test failed*****")
            assert False
