from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

driver=webdriver.Chrome()
driver.get("http://www.quora.com/profile/kevin-rose")
element=driver.find_element_by_xpath("//a[text()='Followers ']")
wait=WebDriverWait(driver,10)
wait.until(ec.element_to_be_clickable,element)
element.click()
