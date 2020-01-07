from selenium import webdriver
import time
#1 Open browser
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
#2 Enter URL(bluestone)
driver.get("https://www.bluestone.com/")
driver.maximize_window()
driver.implicitly_wait(12)
#3 move to Gold coins
act = ActionChains(driver)
wb_coins = driver.find_element_by_xpath("//a[@title='Coins']")

#4 Select 5 Gm
wb_one_gram = driver.find_element_by_xpath("//span[text()='Lakshmi Gold Coins']/../..//ul/li/span[text()='5 gram']")
act.move_to_element(wb_coins).click(wb_one_gram).perform()

#5 Verify 5Gm Coin is displaying or not
exp_gold_coin = "5 gram"
wb = driver.find_element_by_xpath("//h1[text()='5 gram 24 KT Lakshmi Gold Coin']")
act_check_gold_coin = wb.text
print(act_check_gold_coin)
if act_check_gold_coin.__contains__(exp_gold_coin):
    print("Verified",act_check_gold_coin,"is being displayed")
else:
    print("Not Verified")
#close Browser
driver.close()