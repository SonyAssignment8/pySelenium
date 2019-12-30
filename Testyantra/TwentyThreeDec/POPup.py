from selenium import webdriver
import time
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(r"D:\Python\chromedriver.exe")
driver.get("https://javascript.info/alert-prompt-confirm")
driver.implicitly_wait(12)
driver.maximize_window()
driver.find_element_by_xpath("//a[text()='Run the demo']").click()
driver.switch_to_alert().send_keys("atul")
time.sleep(20)
driver.switch_to_alert().accept()
print(driver.switch_to_alert().text)
driver.switch_to_alert().dismiss()
driver.close()

