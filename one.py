from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

serv_obj = Service("Chrome_driver_location")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://the-internet.herokuapp.com/upload")

upload = driver.find_element(By.XPATH, "//input[@id='file-upload']")
upload.send_keys("file_pathway_from_the_system")

submit = driver.find_element(By.ID, "file-submit")
submit.click()

driver.quit()
