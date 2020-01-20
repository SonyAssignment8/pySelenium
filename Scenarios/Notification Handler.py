from selenium import webdriver
from selenium.webdriver.chrome.options import Options

driver = webdriver.Chrome()
driver.get('https://www.irctc.co.in')

option = Options()

option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")

# Pass the argument 1 to allow and 2 to block
option.add_experimental_option("prefs", {
    "profile.default_content_setting_values.notifications": 2
})


