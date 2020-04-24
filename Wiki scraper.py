# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 16:50:46 2020

@author: NNicholson
"""
from bs4 import BeautifulSoup
import lxml
import requests
import csv

def grab_year_pages(years):
    for year in years:
        page = requests.get('https://wikipedia.org/wiki/'+year)
        if not page:
            print('Failed to fetch page for',year)
            continue
        else:
            print('Successfully fetched page for',year)
            with open('First page fetches/'+year+'.txt',mode = 'w', encoding = 'utf8') as file:
                file.write(page.text)
    print('Finished fetching pages')
    

def soupify(year):
    with open('First page fetches/'+str(year)+'.txt', mode = 'r', encoding = 'utf8') as file:
        return BeautifulSoup(file,'lxml')
            
def check_for_span(years,name):
    missing = []
    for year in years:
        page = soupify(year)
        if page.find_all('span',id = name) == []:
            missing.append(str(year))
    return missing

def write_csv(filepath, events):
    with open(filepath,'w',encoding = 'utf8') as file:
        writer = csv.writer(file)
        for event in events:
            writer.writerow([event])
            
myfolder = 'First CSVs'
