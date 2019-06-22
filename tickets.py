from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options 
from twilio.rest import Client
import time
import logging

logging.basicConfig(level=logging.INFO, format = '%(asctime)s - %(levelname)s - %(message)s')

chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(executable_path=r'C:\Python\selenium\webdriver\chrome\chromedriver.exe', options=chrome_options)

page = r'https://www.odeon.co.uk/films/avengers_endgame/18306/'
xpath = r'//*[@id="filmFunctions"]/a'

client = Client("ACc9dbfaf5f2e33986a1c23f9461279665","bd2b7ba125af23f7fa1e28b5a56ffba2")

logging.info('Program started')
logging.info('Getting page...')

isOnSale = False

while isOnSale == False:
	driver.get(page)
	logging.info('Page opened')
	try:
		driver.find_element_by_xpath(xpath)
		logging.info('Tickets on sale')
		isOnSale == True
		client.messages.create(to="", from_="+447481344819", body="Avengers Endgame tickets are now on sale!")
		driver.quit()
		break
	except NoSuchElementException:
		logging.info("Tickets still not on sale :(")
		logging.info("Checking again in 60 seconds...")
		time.sleep(60)
		logging.info("Getting page again...")
