class SearchCustomer:
    txtEmail_id="//*[@id='SearchEmail']"
    txtFirstname="//*[@id='SearchFirstName']"
    txtLastname="//*[@id='SearchLastName']"
    btnSearch="//*[@id='search-customers']"

    #table part
    tblSearchresult_xpath="//table[@role='grid']"
    table_xpath="//table[@id='customers-grid']"
    tablerows_xpath="//*[@id='customers-grid']/tbody/tr"
    tablecolumns_xpath="//*[@id='customers-grid']/tbody/tr/td"

    def __init__(self,driver):
        self.driver=driver

    def setEmail(self,email):
        self.driver.find_element_by_xpath(self.txtEmail_id).clear()
        self.driver.find_element_by_xpath(self.txtEmail_id).send_keys(email)
    def setFirstname(self,fname):
        self.driver.find_element_by_xpath(self.txtFirstname).clear()
        self.driver.find_element_by_xpath(self.txtFirstname).send_keys(fname)
    def setLastname(self,lname):
        self.driver.find_element_by_xpath(self.txtLastname).clear()
        self.driver.find_element_by_xpath(self.txtLastname).send_keys(lname)
    def clickSearch(self):
        self.driver.find_element_by_xpath(self.btnSearch).click()
    def getNoOfRows(self):
        # note:here use len means return numbers so not use element use "elements"
        return len(self.driver.find_elements_by_xpath(self.tablerows_xpath))
    def getNoOfColmns(self):
        #note:here use len means return numbers so not use element use "elements"
        return len(self.driver.find_elements_by_xpath(self.tablecolumns_xpath))
    def searchCustomerByEmail(self,email):
        flag=True
        for r in range(1,self.getNoOfRows()+1):
            table=self.driver.find_element_by_xpath(self.table_xpath)
            emailid=self.driver.find_element_by_xpath("//table[@id='customers-grid']/tbody/tr["+str(r)+"]/td[2]").text
            if emailid == email:
                flag=True
                #flag=False
                break
        return flag

    def searchCustomerByName(self,Name):
        flag = True
        #flag=False
        for r in range(1, self.getNoOfRows() + 1):
            table = self.driver.find_element_by_xpath(self.table_xpath)
            name=table.find_element_by_xpath("//table[@id='customers-grid']/tbody/tr["+str(r)+"]/td[3]").text
            if name==Name:
                flag=True
                break
        return flag







