import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# defining executable path
service = Service(executable_path="C:/Program Files (x86)/chromedriver.exe")

driver = webdriver.Chrome(service=service)


driver.maximize_window()
driver.get("https://trytestingthis.netlify.app/")

#firstname & lastname input
frstname = driver.find_element(By.ID, "fname")
frstname.send_keys("Roronoa")
time.sleep(3)
lstname = driver.find_element(By.ID, "fname")
lstname.send_keys("Zoro")
time.sleep(3)

#radio button
gender = driver.find_element(By.ID, "male")
gender.click()






driver.close()