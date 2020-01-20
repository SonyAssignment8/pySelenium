from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://www.vtiger.com")
privacyPolicies = driver.find_element(By.XPATH,"//a[text()='Privacy Policy'")
driver.execute_script("arguments[0].ScrollIntoView()",privacyPolicies)
time.sleep()
driver.close()

