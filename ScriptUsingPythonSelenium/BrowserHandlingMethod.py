from ScriptUsingPythonSelenium.BaseClass import*
driver.get("http://localhost:8888/")
a=driver.current_url  #to get the current URL
print(a)
# b=driver.page_source #to get the current page source
# print(b)
driver.maximize_window() #to maximize the window
time.sleep(3)
driver.minimize_window() #To minimize the window
time.sleep(3)
#driver.fullscreen_window() #T open browser in full screen mode
driver.maximize_window()
time.sleep(3)
driver.refresh()
c=driver.title
print(c)
driver.back()
driver.forward()
driver.current_window_handle  #to get the sessin id of current window
#e=driver.window_handles
#print(e)
print(d)
import pickle

cookie={"name":"kk","value":"ab"}
driver.add_cookie(cookie)
ck=driver.get_cookie("kk")
print(ck)
