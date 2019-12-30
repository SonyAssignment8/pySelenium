
from selenium import webdriver
from time import sleep

from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://www.google.com/")
sleep(5)
driver.find_element_by_name("q").send_keys("movies")
driver.find_element_by_name("q").send_keys(Keys.ENTER)
# driver.execute_script("window.open('https://in.bookmyshow.com/bengaluru','tab2');")
# sleep(4)
# driver.switch_to_window("tab2")
# driver.execute_script("window.scrollTo(0,400)")
sleep(4)
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
sleep(4)
driver.execute_script("window.scrollTo(0,document.body.scrollTop)")
sleep(3)
height = driver.execute_script("return document.body.scrollWidth")
width = driver.execute_script("return document.body.scrollHeight")
print("Height of scroll bar:",height)
print("Width of scroll bar:",width)
driver.close()