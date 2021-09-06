import selenium
from selenium import webdriver
driver=webdriver.Chrome()
driver.get('https://primevideo.com')
driver.maximize_window()
driver.find_element_by_class_name('_1NNx6V').click()
driver.find_element_by_xpath('//*[@id="ap_email"]').send_keys('Enter your email id here')
driver.find_element_by_xpath('//*[@id="ap_password"]').send_keys('Enter your password here')
driver.find_element_by_class_name('a-button-input').click()
driver.find_element_by_xpath('//*[@id="aiv-cl-main-middle"]/div/div[3]/div/div[3]/div/div[2]/div/div/ul/li[3]/div/a/div').click()
driver.find_element_by_xpath('//*[@id="aiv-cl-main-middle"]/div/div[3]/div/div[1]/div/div[1]/div[1]/div/a').click()
