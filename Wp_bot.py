from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
chats=['bot1','Paapa','Ma','bot2']

driver = webdriver.Chrome(executable_path="/usr/local/lib/node_modules/chromedriver/bin/chromedriver",)
driver.get("https://web.whatsapp.com/")
driver.maximize_window()
print("Scan QR code ")
time.sleep(10)
for chat in chats :
    driver.find_element_by_xpath("//*[contains(@class,'_3FRCZ copyable-text selectable-text')]").send_keys(f"{chat}")
    driver.find_element_by_xpath("//*[contains(@class,'_3FRCZ copyable-text selectable-text')]").send_keys(Keys.ENTER)
    time.sleep(4)
    driver.find_element_by_xpath("//*[contains(@class,'_2FVVk _2UL8j')]").send_keys(" Helowwwww :D ")
    driver.find_element_by_xpath("//*[contains(@class,'_2FVVk _2UL8j')]").send_keys(Keys.ENTER)
    driver.find_element_by_xpath("//*[contains(@class,'_2FVVk _2UL8j')]").send_keys(Keys.ENTER)
    time.sleep(4)
    driver.find_element_by_xpath("//*[contains(@class,'_2FVVk _2UL8j')]").send_keys(" wtsuoppp :D ")
    driver.find_element_by_xpath("//*[contains(@class,'_2FVVk _2UL8j')]").send_keys(Keys.ENTER)
    driver.find_element_by_xpath("//*[contains(@class,'_2FVVk _2UL8j')]").send_keys(Keys.ENTER)
