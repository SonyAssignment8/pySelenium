from builtins import print

from selenium import webdriver
import time
#1 Open browser
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
#2 Enter URL(bluestone)
driver.get("https://www.bluestone.com/")
driver.maximize_window()
driver.implicitly_wait(12)

#3 click on goldmine 10+1 Scheme
driver.find_element_by_xpath("//a[@title='Gold Mine 10+1 Monthly Plan']").click()
#Scroll Down to start now button
driver.execute_script("window.scrollTo(0,500)")
time.sleep(1)


gold_mine_title = driver.title
print(gold_mine_title)
#4. enter monthly amount and email address and click on start now
driver.find_element_by_xpath("//input[@id='amount']").send_keys("10000")
driver.find_element_by_xpath("//input[@id='Email']").send_keys("abc@gmail.com")

#5 with out entering monthly amount and email address and click on start now
driver.find_element_by_xpath("//input[@id='gmsStart']").click()
time.sleep(2)
nxt_title = driver.title
print(nxt_title)
if gold_mine_title != nxt_title:
    print("Amount & Email is reflected in next page")
else:
    print("Ur in same page")
driver.close()

