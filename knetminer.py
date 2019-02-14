#!/usr/bin/python

import json, requests, os, selenium, pandas as pd, bs4
from selenium import webdriver
from bs4 import BeautifulSoup

#use selenium to automatically access the browser.
def seleneknet():
    #access browser driver if 1) browser has a driver downloaded. 2) a driver is added to selenium.
    driver = webdriver.Firefox()
    driver.get(url)
    python_button.click()
    
    



'''
def knetscrap():
    url = "http://babvs67.rothamsted.ac.uk:8081/ws/rice/genome"
    phenotypes = {"pheno1":"mesocotyl length", "pheno2":"coleoptile length", "pheno3":"root length"}
    r = requests.get(url, params=phenotypes)
    print(r.url)
    r.json()
    return
'''
if __name__=="__main__":
    #knetscrap()