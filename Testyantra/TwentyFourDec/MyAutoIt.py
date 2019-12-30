from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome(executable_path="D:\Python\chromedriver.exe")
driver.get("https://blueimp.github.io/jQuery-File-Upload/")
driver.maximize_window()
driver.find_element_by_xpath("//input[@name='files[]']").click()
driver.find_element_by_xpath("//span[text()='Start upload']").click()
# import autoit
# Upload
# autoit.win_wait_active("[CLASS:#32770],3")
# autoit.control_send("[CLASS:#32770]", "Edit1", "oopss concept.docx")
# autoit.control_click("[CLASS:#32770]","Button1")