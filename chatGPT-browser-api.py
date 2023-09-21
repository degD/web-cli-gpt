"""
Made by: DegD
Date: 20.09.2023
Purpose: Library to access OpenAI's ChatGPT trough the default web browser
Inspired by https://github.com/alnwlsn/scratchpad/blob/main/chatgpt.py
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


# Start chromium with
# chromium --remote-debugging-port=9222

options = webdriver.ChromeOptions()
options.add_experimental_option("debuggerAddress", "localhost:9222")

driver = webdriver.Chrome(options=options)

# driver.get("https://chat.openai.com/")
text_box = driver.find_element(By.ID, "prompt-textarea")
text_box.send_keys("Hello, ChatGPT! I hate you!" + Keys.RETURN)
# Would be better if clicks on SEND
# And wait a little

conversation_turn_9 = driver.find_element(
    By.CSS_SELECTOR, 
    "div[data-testid='conversation-turn-9'] p")
print(conversation_turn_9.text)

# driver.close()