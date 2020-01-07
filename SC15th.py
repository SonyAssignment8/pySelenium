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

#4 Select 2 Gm
wb_one_gram = driver.find_element_by_xpath("//span[contains(text(),'2 gram')]")
act.move_to_element(wb_coins).click(wb_one_gram).perform()

#5 Verify 1Gm Coin is displaying or not
exp_gold_coin = "2 gram"
wb = driver.find_element_by_xpath("//h1[text()='2 gram 24 KT Gold Coin']")
act_check_gold_coin = wb.text
print(act_check_gold_coin)
if act_check_gold_coin.__contains__(exp_gold_coin):
    print("Verified",act_check_gold_coin,"is being displayed")
else:
    print("Not Verified")
#close Browser
driver.close()