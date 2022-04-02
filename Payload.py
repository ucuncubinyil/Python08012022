from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from datetime import datetime
from Veritabani import Veritabani

#
# driver_path = "C:\\DovizTakip\\chromedriver.exe"
# opsiyonlar = Options()
# opsiyonlar.add_argument("--headless")
#
# browser = webdriver.Chrome(executable_path=driver_path, options=opsiyonlar)
# browser.get("https://www.haberturk.com/")
#
# altin = browser.find_element_by_css_selector("a#gram-altin span:nth-child(2)").text
# dolar = browser.find_element_by_css_selector("a#dolar span:nth-child(2)").text
# euro = browser.find_element_by_css_selector("a#euro span:nth-child(2)").text
#
# print(altin)
# print(dolar)
# print(euro)

print(datetime.now())
zaman = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
print(zaman)