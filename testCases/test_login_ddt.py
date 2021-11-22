
from selenium import webdriver
import pytest
from pageObjects.LoginPage import Loginpage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import Xlutils
import time
class Test_002_ddt_Login:
    baseURL = ReadConfig.getApplicationURL()
    path="/home/ticvictech/PycharmProjects/nopcommerceProject/testData/nopcommerce_DDT_FIle.xlsx"
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_login_ddt(self, setup):
        self.logger.info("***test_login_ddt***")
        self.logger.info("*****Veryfing login ddt_test*****")
        self.driver = setup
        time.sleep(2)
        self.driver.get(self.baseURL)
        time.sleep(2)
        self.lp = Loginpage(self.driver)
        self.rows=Xlutils.getRowCount(self.path,"Sheet1")
        print("number of rows in excel:",self.rows)
        ls_status=[]
        for r in range(2,self.rows+1):
            self.user=Xlutils.readData(self.path,"Sheet1",r,1)
            self.password=Xlutils.readData(self.path,"Sheet1",r,2)
            self.exp=Xlutils.readData(self.path,"Sheet1",r,3)

            self.lp.setUsername(self.user)
            self.lp.setPassword(self.password)
            self.lp.clicklogin()
            time.sleep(4)

            act_title=self.driver.title
            exp_title="Dashboard / nopCommerce administration"

            if act_title==exp_title:
                if self.exp=="pass":
                    self.logger.info("passed")
                    self.lp.clicklogout()
                    ls_status.append("pass")
                elif self.exp=="fail":
                    self.logger.info("fail")
                    self.lp.clicklogout()
                    ls_status.append("fail")
            elif act_title != exp_title:
                if self.exp=="pass":
                    self.logger.info("failed")
                elif self.exp=="fail":
                    self.logger.info("passed")
                    ls_status.append("pass")

        if "fail" not in ls_status:
            self.logger.info("test login_ddt completed success")
            self.driver.close()
            assert True
        else:
            self.logger.info("test login_ddt completed failed")
            self.driver.close()
            assert False
        self.logger.info("******** Test_002_ddt_Login **********")