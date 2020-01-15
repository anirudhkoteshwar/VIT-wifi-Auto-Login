import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

a = input("Enter your regno.::")
b = input("Enter your Password::")

driver = webdriver.Chrome()
driver.get("http://phc.prontonetworks.com/cgi-bin/authlogin?URI=http://www.msftconnecttest.com/redirect")

username = driver.find_element_by_name("userId")
password = driver.find_element_by_name("password")
username.send_keys(a)
password.send_keys(b)
btn = driver.find_element_by_name("Submit22")
btn.click()

time.sleep(3)
time.close()