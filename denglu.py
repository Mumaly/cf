from selenium import webdriver
import time

class DL():
    dr=webdriver.Firefox()
    def Login(self):
        self.dr.get("http://123.57.140.190/manage/index.php")
        time.sleep(4)
        self.dr.find_element_by_name("Username").send_keys('admin')
        time.sleep(4)
        self.dr.find_element_by_name("Password").send_keys('admin999')
        self.dr.find_element_by_name("Submit").click()
        time.sleep(4)

    def Logout(self):
        self.dr.quit()
s1=DL()
s1.Login()
