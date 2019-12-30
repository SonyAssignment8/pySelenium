from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://webmail.testyantra.in/cpsess4343257689/webmail/paper_lantern/index.html?login=1&post_login=41798576748722")
driver.maximize_window()
driver.find_element_by_name("user").send_keys("ankita.m@testyantra.in")
#driver.find_element_by_xpath("//span[text()='Next']").click()

driver.find_element_by_id("pass").send_keys("Ankita77$")
driver.find_element_by_name("login").click()
driver.implicitly_wait(20)
fr=driver.find_element_by_id("mailFrame")
driver.switch_to.frame(fr)
a=driver.find_element_by_id("mailboxName").text
print("total number of mail",a[7:18:])
lst=driver.find_elements_by_xpath("//div[@class='msglist']/div")
i=iter(lst)
print(next(i).text)
