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
#verify th login page
expected="Webmail"
actual=driver.title
if actual.__contains__(expected):
    print("login page loaded successfully...")

driver.switch_to.frame("mailFrame")
driver.find_element_by_id("composelink").click()
window_list=driver.window_handles[1]
driver.switch_to.window(window_list)
driver.find_element_by_xpath("//input[@class='hordeACTrigger impACTrigger']").send_keys("rashmi.n@testyantra.in")
driver.find_element_by_id("subject").send_keys("Test Mail")
driver.find_element_by_id("composeMessage").send_keys("Hi Rashmi..  Test Mail")
driver.find_element_by_id("send_button").click()