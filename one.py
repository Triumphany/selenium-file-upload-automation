from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

serv_obj = Service("C:\\drivers\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://the-internet.herokuapp.com/upload")

upload = driver.find_element(By.XPATH, "//input[@id='file-upload']")
upload.send_keys("file_pathway_from_the_system")

submit = driver.find_element(By.ID, "file-submit")
submit.click()

driver.quit()