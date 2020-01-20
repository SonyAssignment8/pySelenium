from selenium import webdriver
import csv
browser = webdriver.Chrome()




from selenium import webdriver
import csv
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

browser.get('https://www.ebay.co.uk/itm/Wooden-Box-Coins-Coin-Capsules-Display-Storage-Case-for-Collectible-50-100-New/392274824564')
from selenium.webdriver.support.select import Select

sel = Select(browser.find_element_by_xpath("//select[@id='msku-sel-1']"))

for index in range(1, len(sel.options)):
    # skipping index 0 because it is not valid option
    sel.select_by_index(index)
    print("{}: {}".format(sel.first_selected_option.text, browser.find_element_by_xpath("//span[@id='prcIsum']").text))
