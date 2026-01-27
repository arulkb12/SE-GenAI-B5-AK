from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/")

#driver.back()
#driver.forward()
#driver.refresh()

#finding element

element = driver.find_element(By.ID,"content")
element = driver.find_element(By.XPATH, '//*[@id="content"]/ul/li[1]/a')

#wait 
wait = WebDriverWait(driver, 10)
element = wait.until(EC.presence_of_element_located(By.id, "content"))

#Interaction
element.click()
element.send_keys('projects')
element.clear()

#Screenshots
driver.save_screenshot('demo.png')