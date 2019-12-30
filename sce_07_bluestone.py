'''
Scenario 7
1. open Browser
2. Pass Url (bluestone)
3. Move the cursor  All Jewellery
4. select Kadas and click on it
5. select any kada.
6. click on buy now
7. Capture whether error message is displayed or not(Not Displayed fail test case)
8. close browser
'''
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(15)
driver.get("https://www.bluestone.com/")
import time
ring_we=driver.find_element_by_xpath("//a[contains(text(),'All Jewellery')]")
act=ActionChains(driver)
act.click_and_hold(ring_we).perform()
driver.find_element_by_xpath("//span[@data-p='mens-jewellery-kadas,m']").click()
driver.find_element_by_xpath("//img[@alt='The Udith Kada For Him']").click()
parent_window=driver.window_handles[0]
child_window=driver.window_handles[1]
driver.switch_to.window(child_window)
time.sleep(5)
driver.find_element_by_xpath("//input[@class='exclusive btn style2 btn-block addToCart']").click()
err_mesg=driver.find_element_by_xpath("//div[@class='formErrorContent']").text
print(err_mesg)
assert err_mesg,"Error mesg does not dislayed"
print("Error mesg must be displayed")
driver.close()