'''Scenario 24
1. Open browser
2. enter URL(bluestone)
3. go to search and search for rings
4. go to gold purity
5. get count of 22k
6. close browser '''
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
driver=webdriver.Chrome("./chromedriver.exe")
#Navigate to bluestone page
driver.get("https://www.bluestone.com/")
driver.maximize_window()
#go to search and search for rings

driver.find_element_by_xpath("//a[@title='Rings']").click()
driver.execute_script("window.scrollBy(0,1000);")
#Navigate to gold purity
purity=driver.find_element_by_xpath("//span[text()='Gold Purity']")
Carat=driver.find_element_by_xpath("//span[@data-displayname='22k']")
act=ActionChains(driver)
act.move_to_element(purity).click_and_hold(Carat).perform()
count=Carat.text
print('count of 22 K is:',count[4::])
#go to gold purity
driver.close()