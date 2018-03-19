from selenium import webdriver

driver = webdriver.Firefox()
driver.implicitly_wait(3)

driver.get('https://google.com')
