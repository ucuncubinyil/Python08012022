from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from datetime import datetime
from Veritabani import Veritabani


class Kur:
    @staticmethod
    def getir(kurTipi):
        driver_path = "C:\\DovizTakip\\chromedriver.exe"
        opsiyonlar = Options()
        opsiyonlar.add_argument("--headless")

        browser = webdriver.Chrome(executable_path=driver_path, options=opsiyonlar)
        browser.get("https://www.haberturk.com/")

        if (kurTipi == "altin"):
            icerik = browser.find_element_by_css_selector("a#gram-altin span:nth-child(2)").text
        elif (kurTipi == "dolar"):
            icerik = browser.find_element_by_css_selector("a#dolar span:nth-child(2)").text
        elif (kurTipi == "euro"):
            icerik = browser.find_element_by_css_selector("a#euro span:nth-child(2)").text
        else:
            print("Hatalı kur tipi girdiniz !!")

        deger = float(icerik.replace(",","."))

        tablo=  "tb_"+kurTipi
        zaman =  datetime.now().strftime("%d.%m.%Y %H:%M:%S")
        print(zaman)
        komut =  f"INSERT INTO {tablo} (zaman, kur) VALUES ('{zaman}', '{deger}' )"
        Veritabani.kaydet(komut)