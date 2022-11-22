import sys
import os
from time import sleep
import OpenBrowser as openb
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service

def componi_url(argomento_ingresso):
    url_base = 'https://www.treccani.it/vocabolario/'
    url_plus = argomento_ingresso
    url_finale = url_base + url_plus
    return url_finale


if __name__ == "__main__":
    word_to_search = sys.argv[1]
    url_finale = componi_url(word_to_search)
    browser = openb.start_browser("chromehidden")
    browser.get(url_finale)
    clear = lambda: os.system('clear')
    clear()

    try:
        CookieAccept = WebDriverWait(browser, 3).until(EC.element_to_be_clickable((By.XPATH,\
            '//*[@id="qc-cmp2-ui"]/div[3]/div/button[3]')))
        CookieAccept.click()
    except:
        print("No cookies")

    try:
        TextPresent = WebDriverWait(browser, 2).until(EC.element_to_be_clickable((By.XPATH,\
        '/html/body/div[2]/div[2]/div/div[1]/div/div[4]/div/p[3]')))
        print("\n")
        print("*************************")
        print(f"**** {word_to_search} ****")
        print("*************************")
        print(TextPresent.text)
        print("*************************")
        print("\n")
    except:
        print(f"Parola {word_to_search} non trovata")
    finally:
        browser.close()

