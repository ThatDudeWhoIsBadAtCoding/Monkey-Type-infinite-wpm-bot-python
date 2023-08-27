from selenium import webdriver
from pyautogui import write
from time import sleep
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from io import StringIO

URL = "https://monkeytype.com"
print("RUNNING")
getter = webdriver.Chrome()
print("SETUPP")
getter.maximize_window()
getter.get(URL)
print("GOT")

cookie_accept_btn = getter.find_element(By.CLASS_NAME, "acceptAll")
cookie_accept_btn.click()
element = getter.find_element(By.XPATH, "//*[@mode='words']")
element.click()
getter.implicitly_wait(1)
sleep(1)

getter.get(URL)
getter.implicitly_wait(5)
sleep(5)

res = getter.page_source
soup = BeautifulSoup(res, 'html.parser')
text = soup.find("div", {"id": "words"})

txt = StringIO()
for child in text.findChildren():
    if len(child.text) > 1:
        txt.write(" ")
        continue
    txt.write(child.text)
txt = txt.getvalue()[1:]
txt.replace("aa", "")
write(txt)   
sleep(10)
getter.close()