from selenium import webdriver
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
#chrome_options.add_argument("--disable-extensions")
#chrome_options.add_argument("--disable-gpu")
#chrome_options.add_argument("--no-sandbox") # linux only
chrome_options.add_argument("--headless")

# 使用 Chromium 的 WebDriver
print("import ok")
driver = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver', chrome_options=chrome_options)

print("driver initial ok")
# 開啟 Google 首頁
driver.get('https://www.baidu.com/')
print("driver get ok")
driver.close()
print("driver close ok")
