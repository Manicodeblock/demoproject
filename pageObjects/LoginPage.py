import time
class Loginpage:
 textbox_username_id="Email"
 textbox_password_id="Password"
 login_button_xpath="//button[@type='submit']"
 logout_link_text_xpath="//*[@id='navbarText']/ul/li[3]/a"
 def __init__(self,driver):
     self.driver=driver
 def setUsername(self,username):
     self.driver.find_element_by_id(self.textbox_username_id).clear()
     time.sleep(2)
     self.driver.find_element_by_id(self.textbox_username_id).send_keys(username)
 def setPassword(self,password):
     self.driver.find_element_by_id(self.textbox_password_id).clear()
     time.sleep(4)
     self.driver.find_element_by_id(self.textbox_password_id).send_keys(password)
 def clicklogin(self):
    self.driver.find_element_by_xpath(self.login_button_xpath).click()
 def clicklogout(self):
    self.driver.find_element_by_xpath(self.logout_link_text_xpath).click()
