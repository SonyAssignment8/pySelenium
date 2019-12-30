from selenium import webdriver

driver=webdriver.Chrome()
driver.get("https://www.google.com/")
driver.execute_script('window.open("https://www.amazon.com/","tab1")')
driver.switch_to_window("tab1")
driver.execute_script("window.scrollTo(500,document.body.scrollHeight)")