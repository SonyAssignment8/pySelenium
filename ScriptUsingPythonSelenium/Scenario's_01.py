from selenium import webdriver
#launch browser
driver=webdriver.Chrome()
driver.implicitly_wait(20)
#enter the URL
driver.get("http://webmail.testyantra.in/")
#Enter the user name and password and login to the g-mail application
driver.find_element_by_id("user").send_keys("krishna.k@testyantra.in")
driver.find_element_by_name("pass").send_keys("Krishna@123")
driver.find_element_by_id("login_submit").click()
#to get the total mail count
import time
time.sleep(10)
driver.switch_to.frame("mailFrame")
mailcount=driver.find_element_by_id("mailboxName").text
print("Total mail count is :-",mailcount[7:18:])
lst_of_mails=driver.find_elements_by_xpath("//div[@class='msglist']/div")
i=iter(lst_of_mails)
print(next(i).text)


