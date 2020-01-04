from selenium import webdriver
from selenium.webdriver.chrome import options

import time
co= webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
co.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(chrome_options=co)
driver.get("https://www.yatra.com/")
driver.maximize_window()
time.sleep(10)
driver.close()

