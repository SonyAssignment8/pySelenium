from ScriptUsingPythonSelenium.BaseClass import*
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.find_element_by_id("txtUsername").send_keys("Admin")
driver.find_element_by_name("txtPassword").send_keys("admin123")
driver.find_element_by_name("Submit").click()
driver.find_element_by_id("menu_admin_viewAdminModule").click()
driver.find_element_by_id("welcome").click()
time.sleep(3)
driver.find_element_by_partial_link_text("Logout").click()
