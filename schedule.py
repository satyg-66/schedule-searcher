#!/bin/env python3

# AUTHOR: Jonas Ingemarsson
# DESC: A script to auto-search for schedules at the University of Skövde
# DEPENDENCIES: proper webbrowser driver compatible with Selenium (https://pypi.org/project/selenium/)
# NOTE: Program is in both Swedish and English, but the site selected is in English only.
#       To change the site to swedish, please edit URL by removing 'eng' in 'schemaeng' and change 'result' in searchType to 
#       its swedish counterpart.

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

def welcome():
    print('##### WELCOME TO HiS SCHEDULE SEARCHER / VÄLKOMMEN TILL HiS SCHEMASÖKARE #####\n')

def searchType():
    question = '''Select a search option / Välj ett alternativ
    1. Course / Kurs
    2. Programme / Programtillfälle
    3. Course occation / Kurstillfälle
    4. Signature / Signatur
    5. Room / Lokal
    '''
    while True:
        answer = input(question)
        if answer == "1":
            result = "Course"
            break
        elif answer == "2":
            result = "Programme"
            break
        elif answer == "3":
            result = "Course occation"
            break
        elif answer == "4":
            result = "Signature"
            break
        elif answer == "5":
            result = "Room"
            break

    return result

def searchValue(TYPE):
    if TYPE == "Course":
        result = input("What Course / Vilken Kurs: ")
    elif TYPE == "Programme":
        result = input("Which Programme / Vilket Program: ")
    elif TYPE == "Course occation":
        result = input("Course occation / Kurstillfälle: ")
    elif TYPE == "Signature":
        result = input("What Signature / Vilken Signatur: ")
    elif TYPE == "Room":
        result = input("What Room / Vilken Lokal: ")

    return result

def scrape(TYPE, VALUE):
    URL = 'https://cloud.timeedit.net/his/web/schemaeng/ri1Q7.html'

    browser = webdriver.Firefox()
    browser.get(URL)

    browser.find_element(By.XPATH, '//*[@id="fancytypeselector"]').click()
    dropDown = Select(browser.find_element(By.XPATH, '//*[@id="fancytypeselector"]'))
    dropDown.select_by_visible_text(TYPE)

    browser.find_element(By.XPATH, '//*[@id="ffsearchname"]').send_keys(VALUE)
    browser.find_element(By.XPATH, '/html/body/div[9]/div[1]/div[2]/div[1]/div/div/input[2]').click()

    browser.find_element(By.XPATH, '/html/body/div[9]/div[1]/div[2]/div[2]/div/div/div/div[2]/a').click()
    browser.find_element(By.XPATH, '//*[@id="objectbasketgo"]').click()

def main():
    welcome()  
    TYPE = searchType()
    VALUE = searchValue(TYPE)
    scrape(TYPE, VALUE)

if __name__ == "__main__":
    main()


