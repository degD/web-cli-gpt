#!/bin/python3

import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Creating WebDriver
options = webdriver.ChromeOptions()
options.add_experimental_option("debuggerAddress", "localhost:9222")
driver = webdriver.Chrome(options=options)

# Sending text to ChatGPT
text = sys.argv[1]
text_box = driver.find_element(By.ID, "prompt-textarea")
text_box.send_keys(text + Keys.RETURN)

# Wait until ChatGPT finishes writing
while driver.find_elements(By.CSS_SELECTOR, ".text-2xl") != []: pass

# Return ChatGPT's response
chatgpt_reply_element = driver.find_elements(By.CSS_SELECTOR, "div[data-testid] p")[-1]
print(chatgpt_reply_element.text)