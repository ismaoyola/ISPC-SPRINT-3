import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 

options= webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome (executable_path= 'C:/Users/ioyola_ext/Documents/chromedriver.exe')
driver.get("https://deliverind.com.ar/")



searchdeliverind = driver.find_element(By.XPATH,"/html/body/header/nav/div[4]/div[1]/ul/li[1]").click()
time.sleep(5)





searchdeliverind=driver.find_element(By.XPATH,"/html/body/header/nav/div[4]/div[1]/ul/li[2]").click()
time.sleep(5)




searchdeliverind=driver.find_element(By.XPATH,"/html/body/header/nav/div[4]/div[1]/ul/li[3]").click()
time.sleep(5)


