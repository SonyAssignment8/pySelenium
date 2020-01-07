from selenium import webdriver
import time
#1 Open browser
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
#2 Enter URL(bluestone)
driver.get("https://www.bluestone.com/")
driver.maximize_window()
act = ActionChains(driver)
wb_jewllery = driver.find_element_by_xpath("//a[@title='Jewellery']")
#3 select Kadas and click on it
wb_kadas = driver.find_element_by_xpath("//a[@title='Kadas']")
act.move_to_element(wb_jewllery).click(wb_kadas).perform()
#4 select any kada
driver.find_element_by_xpath("//a[@id='pid_8994']").click()
driver.switch_to.window(driver.window_handles[1])
time.sleep(1)
#5 Select Bangle size
select = Select(driver.find_element_by_xpath("//input[@id='ringselect']"))
select.select_by_visible_text('2-2(2 2/16")')


