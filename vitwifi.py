import os
import sys
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

regnum = 'XXXXXXX' #Enter your registration number here
pwsd = 'XXXXXX' #Enter your password here
routername = "VIT5G"



# The following 2 lines are written for linux to autoconnect to the wifi.
os.system(f"nmcli dev wifi connect {routername}")
# For windows uncomment the line below (not tested)
#os.system(f'''cmd /c "netsh wlan connect name={routername}"''')
time.sleep(3)

options = Options()
options.binary_location = "/usr/bin/brave" # Modify this string with the path to your chrome executable. 
options.add_argument("headless")
driver = webdriver.Chrome(options=options)

driver.get("http://phc.prontonetworks.com/cgi-bin/authlogin?URI=http://www.msftconnecttest.com/redirect")
driver.implicitly_wait(3)

username = driver.find_element(By.NAME, "userId")
password = driver.find_element(By.NAME, "password")
username.send_keys(regnum)
driver.implicitly_wait(1)
password.send_keys(pwsd)
driver.implicitly_wait(1)
btn = driver.find_element(By.NAME, "Submit22")
btn.click()

driver.implicitly_wait(3)
