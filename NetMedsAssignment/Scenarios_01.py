from selenium import webdriver
from NetMedsAssignment.GeniricLib import GetConfigdata
import time
driver = webdriver.Chrome()
g = GetConfigdata()
us = g.data("Login","username")
pw = g.data("Login", "password")
uname = g.data("Xpath","uname")
pwrd = g.data("Xpath","pwd")
driver.implicitly_wait(20)
driver.get(g.data("config", "url"))
driver.maximize_window()
print(g.data("Xpath","creden"))
driver.find_element_by_xpath(g.data("Xpath", "familyc")).click()
driver.implicitly_wait(10)
driver.find_element_by_xpath(g.data("Xpath","addtocart")).click()
driver.implicitly_wait(10)
driver.find_element_by_xpath(g.data("Xpath","producttoadd")).click()
driver.implicitly_wait(10)
driver.find_element_by_xpath(g.data("Xpath","productcount")).click()






