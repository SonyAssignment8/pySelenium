from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome("./chromedriver.exe")
driver.get("https://www.bluestone.com/")
# driver.maximize_window()
driver.execute_script("window.open('https://google.com','tab');")
driver.switch_to_window('tab')
driver.find_element_by_name("q").send_keys("Python")
driver.find_element_by_name("q").send_keys(Keys.ENTER)
# driver.execute_script("window.scrollTo(document.body.scrollWidth,2000)")
# driver.execute_script("window.scrollTo(0, 1000)")
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

last_height = driver.execute_script("return document.body.scrollWidth")
driver.execute_script("window.scrollTo(0,document.body.scrollTop)")
print(last_height)
driver.save_screenshot('sample.png')
driver.close()