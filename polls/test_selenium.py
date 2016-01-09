import unittest
from selenium import webdriver

#Following are optional required
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException


baseurl = "http://quote-dev.moveeasy.com/accounts/company_login/"
username = "quotetest@gmail.com"
password = "admin123"

xpaths = { 'usernameTxtBox' : "//input[@name='email']",
           'passwordTxtBox' : "//input[@name='password']",
           'submitButton' :   "//input[@value='Login']",
           'div':"//div[@class='details-title']"
         }
mydriver = webdriver.Firefox()
mydriver.get(baseurl)
mydriver.find_element_by_xpath(xpaths['usernameTxtBox']).clear()
mydriver.find_element_by_xpath(xpaths['usernameTxtBox']).send_keys(username)
mydriver.find_element_by_xpath(xpaths['passwordTxtBox']).send_keys(password)
mydriver.find_element_by_xpath(xpaths['submitButton']).click()
quote = mydriver.find_element_by_xpath(xpaths['div'])
mydriver.execute_script("alert('tomjoy is a very good boy')")
print str(quote.text)





