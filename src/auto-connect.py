from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
import json
import time
chrome_options = Options()
#chrome_options.add_argument("--disable-extensions")
#chrome_options.add_argument("--disable-gpu")
#chrome_options.add_argument("--no-sandbox") # linux only
chrome_options.add_argument("--headless")

def login(driver, config_path):
    driver.get('https://go.ruc.edu.cn/')
    wait = WebDriverWait(driver, 10)
    print("driver get ok")
    print(driver.current_url)
    if "srun" not in driver.current_url:
        config = json.load(open(config_path))
        print("config load ok")
        print(driver.page_source)
        username = driver.find_element_by_id('username')
        action = ActionChains(driver)
        action.move_to_element(username)
        action.click(username)
        action.send_keys(config["account"])
        action.perform() #这个一定要的
        print(driver.page_source)
        password = driver.find_element_by_id('password')
        action = ActionChains(driver)
        action.move_to_element(password)
        action.click(password)
        action.send_keys(config["password"])
        action.perform() #这个一定要的
        print(driver.page_source)
        bttn = driver.find_element_by_id('login-account')
        action = ActionChains(driver)
        action.move_to_element(bttn)
        action.click(bttn)
        action.perform() #这个一定要的
        wait = WebDriverWait(driver, 10)
        print(driver.current_url)
        driver.close()
# 使用 Chromium 的 WebDriver
print("import ok")
driver = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver', chrome_options=chrome_options)

print("driver initial ok")
# 開啟 Google 首頁

config_path = "../config/login.json"
login(driver,config_path)
while(True):
    time.sleep(3600)
    #wait = WebDriverWait(driver, 3600)
    config_path = "../config/login.json"
    login(driver,config_path)

driver.quit()
print("driver close ok")
