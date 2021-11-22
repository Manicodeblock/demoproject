import pytest
import time
from pageObjects.LoginPage import Loginpage
from pageObjects.addCustomerPage import AddCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import string
import random


class Test_003_AddCustomer:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.sanity  # these two sanity and regression for groping concepts
    def test_addCustomer(self,setup):
        self.logger.info("***Test_003_AddCustomer***")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp=Loginpage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clicklogin()
        self.logger.info("***Login Successfull***")

        self.logger.info("***Starting customer add test***")

        self.addcust=AddCustomer(self.driver)
        self.addcust.clickOnCustomerMenu()
        self.addcust.clickOnCustomersMenuItem()

        self.addcust.clickOnAddnew()

        self.logger.info("***Providing Customer info***")
        self.email=random_generator()+"@gmail.com"
        self.addcust.setEmail(self.email)
        self.addcust.setPassword("test123")
        self.addcust.setCustomerRoles("Guests")
        self.addcust.setManagerOfVendor("Vendor 2")
        self.addcust.setGender("Male")
        self.addcust.setFirstname("Mr")
        self.addcust.setLastname("Madahan")
        self.addcust.setDateOfBirth("2/05/2001")
        self.addcust.setCompanyname("ticvicTech")
        # self.addcust.setNewsletter("Your store name")#38.54
        self.addcust.clickOnSave()

        self.logger.info("***Saving Customer Info***")
        self.logger.info("***Add customer validation started***")
        self.msg=self.driver.find_element_by_tag_name("body").text

        print(self.msg)
        if "customer has been added successfully." in self.msg:
            assert True==True
            self.logger.info("***Add customer test passed***")
        else:
            self.driver.save_screenshot("/home/ticvictech/PycharmProjects/nopcommerceProject/Screenshots/test_addcustomer.png")
            self.logger.info("***Add customer Test failed***")
            assert True==False
        self.driver.close()

def random_generator(size=8,chars=string.ascii_lowercase+string.digits):
    return ''.join(random.choice(chars) for x in range(size))