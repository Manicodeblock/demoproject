import time
import pytest
from pageObjects.LoginPage import Loginpage
from pageObjects.addCustomerPage import AddCustomer
from pageObjects.SearchCustomerPage import SearchCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class TestCustomerByEmail_004:
    baseURL=ReadConfig.getApplicationURL()
    username=ReadConfig.getUseremail()
    password=ReadConfig.getPassword()
    logger=LogGen.loggen()


    @pytest.mark.regression
    def test_searchCustomerByEmail(self,setup):
        self.logger.info("***TestCustomerByEmail_004***")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp=Loginpage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clicklogin()
        self.logger.info("***Login Successfull***")

        self.logger.info("***starting search customer by Email***")
        #to click customer menu and customer menu item already code method use it by
        #creating that function by creating variable here.
        self.addcust=AddCustomer(self.driver)
        self.addcust.clickOnCustomerMenu()
        self.addcust.clickOnCustomersMenuItem()

        self.logger.info("***Search customer by Emailid***")
        self.searchcust=SearchCustomer(self.driver)
        self.searchcust.setEmail("victoria_victoria@nopcommerce.com")
        self.searchcust.clickSearch()
        time.sleep(5)
        status=self.searchcust.searchCustomerByEmail("victoria_victoria@nopcommerce.com")
        assert True==status
        self.logger.info("***TestCustomerByEmail_004 finished***")
        self.driver.close()



