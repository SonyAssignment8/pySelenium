# all are windows commands

from selenium import webdriver
driver = webdriver.Chrome(executable_path="D:\Python\chromedriver.exe")
driver.get("https://www.linkedin.com/")
driver.maximize_window()
driver.implicitly_wait(8000)
driver.refresh()
driver.implicitly_wait(9000)
driver.minimize_window()
driver.implicitly_wait(9000)
# driver.back()
driver.implicitly_wait(9000)
driver.forward()
driver.implicitly_wait(9000)
driver.title
driver.implicitly_wait(900)
driver.current_url
driver.implicitly_wait(200)
driver.get("https://www.linkedin.com/")
driver.implicitly_wait(200)
# driver.set_window_rect()
driver.implicitly_wait(200)
# driver.set_window_size()
driver.implicitly_wait(200)
driver.close()
# driver.quit()
