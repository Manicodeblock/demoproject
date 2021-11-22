import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import select
class AddCustomer:
    lnk_Customers_menu_path="/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/a"
    lnk_Customers_menuitem_xpath="/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/ul/li[1]/a/p"
    btnAddnew_xpath="//a[@class='btn btn-primary']"

    txtEmail_xpath="//input[@id='Email']"
    txtPassword_xpath="//input[@id='Password']"
    txtFirstname_xpath="//input[@name='FirstName']"
    txtLastname_xpath="//input[@name='LastName']"
    rdMaleGender_xpath="//input[@id='Gender_Male']"
    rdFemaleGender_xpath="//input[@id='Gender_Female']"
    txtDOB_xpath="//input[@id='DateOfBirth']"
    txtCompanyname_xpath="//input[@id='Company']"
    txtnewsletter_xpath="//*[@id='customer-info']/div[2]/div[9]/div[2]/div/div[1]/div/div"
    txtCustomerrolexpath="//*[@id='customer-info']/div[2]/div[10]/div[2]/div/div[1]/div/div"
    btnSave_xpath="/html/body/div[3]/div[1]/form/div[1]/div/button[1]/i"
    lstItemAdministrator_xpath="//li[contains(text(),'Administrators')]"
    lstItemGuests_xpath = "//li[contains(text(),'Guests')]"
    lstItemForummoderator_xpath = "//li[contains(text(),'Forum Moderator')]"
    lstItemREgistered_xpath = "//li[contains(text(),'Registered')]"
    lstItemVendors_xpath = "//li[contains(text(),'Vendors')]"
    #drpmngrOfvendor_xpath = "//select[@id='VendorId']"
    drpmngrOfvendor_xpath = "//*[@id='VendorId']"


    def __init__(self,driver):
        self.driver=driver

    def clickOnCustomerMenu(self):
        self.driver.find_element_by_xpath(self.lnk_Customers_menu_path).click()
    def clickOnCustomersMenuItem(self):
        self.driver.find_element_by_xpath(self.lnk_Customers_menuitem_xpath).click()
    def clickOnAddnew(self):
        self.driver.find_element_by_xpath(self.btnAddnew_xpath).click()
    def setEmail(self,email):
        self.driver.find_element_by_xpath(self.txtEmail_xpath).send_keys(email)
    def setPassword(self,password):
        self.driver.find_element_by_xpath(self.txtPassword_xpath).send_keys(password)
    def setFirstname(self,fname):
        self.driver.find_element_by_xpath(self.txtFirstname_xpath).send_keys(fname)
    def setLastname(self,lname):
        self.driver.find_element_by_xpath(self.txtLastname_xpath).send_keys(lname)
    def setGender(self, gender):
        if gender=="Male":
            self.driver.find_element_by_xpath(self.rdMaleGender_xpath).click()
        elif gender=="Female":
            self.driver.find_element_by_xpath(self.rdFemaleGender_xpath).click()
        else:
            self.driver.find_element_by_xpath(self.rdMaleGender_xpath).click()
    def setCompanyname(self,comname):
        self.driver.find_element_by_xpath(self.txtCompanyname_xpath).send_keys(comname)
        time.sleep(3)

    def setNewsletter(self,newslet):
        self.driver.find_element_by_xpath(self.txtnewsletter_xpath).send_keys(newslet)
    def setCustomerRoles(self,role):
        self.driver.find_element_by_xpath(self.txtCustomerrolexpath).click()
        time.sleep(3)
        if role=="Registered":
            self.lstitem=self.driver.find_element_by_xpath(self.lstItemREgistered_xpath)
        elif role=="Administrators":
            self.lstitem = self.driver.find_element_by_xpath(self.lstItemAdministrator_xpath)
        elif role == "Guests":#user can select register either guests only
            time.sleep(3)
            self.driver.find_element_by_xpath("//*[@id='SelectedCustomerRoleIds_taglist']/li/span[2]").click()
            self.lstitem = self.driver.find_element_by_xpath(self.lstItemGuests_xpath)
        elif role == "Registered":
            self.lstitem = self.driver.find_element_by_xpath(self.lstItemREgistered_xpath)
        elif role == "Vendors":
            self.lstitem = self.driver.find_element_by_xpath(self.lstItemVendors_xpath)
        else:#if none of selected by default vendor selected
            self.lstitem = self.driver.find_element_by_xpath(self.lstItemGuests_xpath)
        time.sleep(3)
        #self.lstitem.click()
        #26.55
        self.driver.execute_script("arguments[0].click();",self.lstitem)

    def setManagerOfVendor(self,value):
        drp=Select(self.driver.find_element_by_xpath(self.drpmngrOfvendor_xpath))
        drp.select_by_visible_text(value)
    def setDateOfBirth(self,DOB):
        self.driver.find_element_by_xpath(self.txtDOB_xpath).send_keys(DOB)
    def clickOnSave(self):
        self.driver.find_element_by_xpath(self.btnSave_xpath).click()
