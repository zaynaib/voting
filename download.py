from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager

executable_path = {'executable_path':ChromeDriverManager().install()}
import selenium

browser = Browser('chrome', **executable_path)