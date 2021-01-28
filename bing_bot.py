import webbrowser
import time
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--headless")
browser = webdriver.Chrome('C:\Program Files (x86)\chromedriver.exe', chrome_options=chrome_options)
# email="your_email"


browser.get('https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=13&ct=1604339855&rver=6.7.6631.0&wp=MBI_SSL&wreply=https%3a%2f%2fwww.bing.com%2fsecure%2fPassport.aspx%3frequrl%3dhttps%253a%252f%252fwww.bing.com%252f%253fwlexpsignin%253d1%26sig%3d2702E9E8B0A361ED0C81E69EB10B6095&lc=1033&id=264960&CSRFToken=3a19e94e-355a-45d0-a9e7-b4cafd4f94bb&aadredir=1')

email=browser.find_element_by_xpath('//*[@id="i0116"]')
email.send_keys("your_email")

time.sleep(2)

next=browser.find_element_by_xpath('//*[@id="idSIButton9"]')
next.click()
time.sleep(2)
password=browser.find_element_by_xpath('//*[@id="i0118"]')
password.send_keys('your_password')





time.sleep(2)


sign_in=browser.find_element_by_xpath('//*[@id="idSIButton9"]')
sign_in.click()

# yes=browser.find_element_by_xpath('//*[@id="idSIButton9"]')
# yes.click()

time.sleep(2)


words1=["a", "b", "c", "d","e", "f", "g", "h","i", "j", "k", "l","m", "n", "o", "p","q", "r", "s", "t","u", "v", "w", "x","y", "z","a", "b", "c", "d","e", "f", "g", "h","i", "j",]
words=[]
for word in words1:
    some=words1[random.randint(0,25)]+words1[random.randint(0,25)]+words1[random.randint(0,25)]
    words.append(some)


search_bar=browser.find_element_by_xpath('//*[@id="sb_form_q"]')

for word in words:
    print(word)
    search_bar=browser.find_element_by_xpath('//*[@id="sb_form_q"]')
    search_bar.send_keys(word)

    time.sleep(3)

#
# search = browser.find_element_by_xpath('//*[@id="sb_form_go"]')
    search_bar.send_keys(Keys.ENTER)