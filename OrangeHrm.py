from selenium import webdriver
driver = webdriver.Chrome(executable_path="D:\Python\chromedriver.exe")
driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
driver.maximize_window()
driver.find_element_by_id("txtUsername")
driver.find_element_by_id("txtUsername").send_keys("Admin")
driver.find_element_by_name("txtPassword").send_keys("admin123")
driver.find_element_by_id("btnLogin").click()
# driver.find_element_by_id("menu_admin_viewAdminModule")
# driver.find_element_by_id("menu_admin_viewAdminModule").click()
driver.find_element_by_xpath("//a[@id='welcome']").click()
driver.find_element_by_xpath("//a[text()='Logout']").click()


