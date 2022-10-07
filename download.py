from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
#https://www.tutorialspoint.com/downloading-a-file-at-a-specified-location-through-python-and-selenium-using-chrome-driver

import selenium

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#object of ChromeOptions class
op = webdriver.ChromeOptions()
#browser preferences
p = {'download.default_directory':'C:\Users\ghs6kor\Downloads\Test'}
#add options to browser
op.add_experimental_option('prefs', p)


executable_path = {'executable_path':ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path,headless=False,options=op)

#vist website
url=  'https://www.elections.il.gov/shape/'
browser.visit(url)

#search for prefix 2020_

links_found = browser.links.find_by_partial_text('2020_')
print(links_found)

print(links_found[0].text)

'''
#loop through 2020_ map files and click each one
for i in range(len(links_found)):
    links_found[i].click()

    #next skip the first link that goes to the parent directory and only click on the actual shape flies
    shapefile_links = browser.find_by_css('a')[1:]
    for e in range(len(shapefile_links)):
        shapefile_links[e].click()

    #go back to the parent directory and click on the next goverment 2020 shape files
    browser.back()


browser.quit()
'''

#loop through and all the 2020_ links
#click for each a element on the page
# and download into a folder

links_found[0].click()
shapefile_links = browser.find_by_css('a')[1:]


#for e in range(len(shapefile_links)):
#    shapefile_links[e].click()
#print(browser.find_by_css('a'))
#print(shapefile_links)
#loop through [1:]



#then go back

