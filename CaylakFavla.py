"""

*** This automation software makes writers crazy. ***

"""
from selenium.common.exceptions import NoSuchElementException      
from selenium import webdriver
from contextlib import contextmanager
import time
browser = webdriver.Firefox()
browser.get("https://eksisozluk.com/giris")
time.sleep(4)
emailgiris = browser.find_element_by_xpath("//*[@id='username']")
passwordgiris = browser.find_element_by_xpath("//*[@id='password']")
emailgiris.send_keys("email@gmail.com")
passwordgiris.send_keys("PassWord1")
giris_yap = browser.find_element_by_xpath("//*[@id='login-form-container']/form/fieldset/div[4]/button")
giris_yap.click()
time.sleep(5)

browser.get("https://eksisozluk.com/basliklar/caylaklar")
time.sleep(3)
      
def check_exists_by_xpath(xpath):
    try:
        browser.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True

def favla():
	while check_exists_by_xpath("//*[@title='favorilere ekle']"):
		try:
			fav = browser.find_element_by_xpath("//*[@title='favorilere ekle']")
			fav.click() 
			time.sleep(1) 
		except:
			time.sleep(1)
	
b = 1
while b < 101:
	baslik = browser.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/section/ul/li["+str(b)+"]/a")
	baslik.click()
	time.sleep(2)	
	favla()	
	time.sleep(2)
	browser.execute_script("window.history.go(-1)")	
	time.sleep(3)
	b = b+1
	
#		Chrome(executable_path='C:/Users/chromedriver.exe')
#		browser.execute_script("window.scrollTo(0,800);")	
#		browser.close()
#//*[@id='track-topic-link']
#/html/body/div[3]/div[2]/div[2]/section/div[1]/div[1]/div/div[2]