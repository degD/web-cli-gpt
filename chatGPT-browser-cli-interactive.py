"""
Made by: DegD
Date: 20.09.2023
Purpose: Library to access OpenAI's ChatGPT trough the default web browser
Inspired by https://github.com/alnwlsn/scratchpad/blob/main/chatgpt.py
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


# Start chromium with
# chromium --remote-debugging-port=9222
# Then login at chat.openai.com

options = webdriver.ChromeOptions()
options.add_experimental_option("debuggerAddress", "localhost:9222")

driver = webdriver.Chrome(options=options)

# driver.get("https://chat.openai.com/")
# text_box = driver.find_element(By.ID, "prompt-textarea")
# text_box.send_keys("Hello, ChatGPT! I love you!" + Keys.RETURN)
# Would be better if clicks on SEND
# And wait a little

# Get conversation data
conversation_data = []
for conversation_element in driver.find_elements(By.CSS_SELECTOR, "div[data-testid]"):
    conversation_data.append(conversation_element.text)

# Print the conversation
print("ChatGPT browser version terminal control:\n")
for i, conversation in enumerate(conversation_data):
    # print(f'{i+1}. ', end='')
    if i % 2 == 0: print("USER:")
    else: print("ChatGPT:")
    print(conversation + '\n')

# Would be better if clicks on SEND
# And wait a little
# conversation_counter = i + 2 + 1 # To access the last reply of ChatGPT easily 
text_box = driver.find_element(By.ID, "prompt-textarea")
while True:
    user_prompt = input('USER:\n')
    text_box.send_keys(user_prompt + Keys.RETURN)
    
    # Wait until ChatGPT is ready (finished waiting)
    while driver.find_elements(By.CSS_SELECTOR, ".text-2xl") != []: pass
    # not bool(chatgpt_state_element_list)
    # is_chatgpt_done_writing = lambda d: not bool(chatgpt_state_element_list)
    # class=text-2xl
    
    print("\nChatGPT:") # Fine-tune selectors...
    chatgpt_reply_element = driver.find_elements(By.CSS_SELECTOR, "div[data-testid]")[-1]
    print(chatgpt_reply_element.text + '\n')
    
    # Add further error check

# conversation_turn_9 = driver.find_elements(
#     By.CSS_SELECTOR, 
#     "div[data-testid] p")
# for x in conversation_turn_9:
#     print(x.text)

# driver.close()

