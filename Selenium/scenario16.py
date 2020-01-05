from selenium import webdriver
import time
from selenium.webdriver import ActionChains

driver=webdriver.Chrome(executable_path='C:\\Users\\kodiak\\Downloads\\chromedriver.exe')
driver.get("https://www.bluestone.com/")
driver.maximize_window()
mousehover=driver.find_element_by_xpath("//a[text()='Coins ']")
a=ActionChains(driver)
a.move_to_element(mousehover).perform()
time.sleep(3)
driver.find_elements_by_xpath("//span[@data-p='all-jewellery-goldcoins-plain-gold,m']/../..//span[contains(text(),'gram')]")
#Method1
acl_url=driver.current_url
exp_url=("https://www.bluestone.com/gold+coins/1-gram-24-kt-gold-coin~5920.html")
assert acl_url==exp_url,print("fail")
print("pass")

#Method2
# for i in lst_coins:
#     data=i.text
#     actuallst.append(data)
# print(actuallst)
# assert "1 gram" in actuallst,"Coin is not in the list"
# print("1 gram coin present in the list")
driver.close()

