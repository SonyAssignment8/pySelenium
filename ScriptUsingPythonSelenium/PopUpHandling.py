from selenium import webdriver
driver=webdriver.Chrome()
driver.implicitly_wait(20)
driver.get("https://javascript.info/alert-prompt-confirm")
driver.find_element_by_xpath("//a[text()='Run the demo']").click()
import time
time.sleep(5)
alt=driver.switch_to_alert()
alt.send_keys("krishna")
print(alt.text)
alt.accept()
alt.accept()

