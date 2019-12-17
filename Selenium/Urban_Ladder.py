from selenium import webdriver

driver = webdriver.Chrome(r"C:\Users\Jyoti\AppData\Local\Programs\Python\Python35\Scripts\chromedriver.exe")
driver.implicitly_wait(20)
driver.get("https://www.urbanladder.com/")
driver.find_element_by_xpath("//a[@data-gaaction='popup.auth.close']").click()
import time
time.sleep(2)
links = driver.find_elements_by_xpath("//ul[@class='topnav bodytext']/ul/li")
for i in links:
    print(i.text)
    # if i.text == "Living":
    #     i.click()

livingSubList = driver.find_elements_by_xpath("//div[@class='subnavlist_wrapper clearfix']")
print(livingSubList)
for j in livingSubList:
    print(j.text)

