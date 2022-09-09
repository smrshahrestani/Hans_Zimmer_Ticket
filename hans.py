
from hashlib import new
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from pynput import keyboard
from pynput.keyboard import Key, Controller
import os


rest = 10

website1 = "https://shop.axs.co.uk/Lw%2fYCwAAAACXOTP%2fAAAAAACf%2fv%2f%2f%2fwD%2f%2f%2f%2f%2fBmFtZXh1awD%2f%2f%2f%2f%2f%2f%2f%2f%2f%2fw%3d%3d/shop/search?skin=&tags=&cpch=&cpdate=&cpcn=&cpsrc=&intoff=&cid=&uk_et_cid=&utm_source=&utm_medium=&utm_campaign=&utm_term=&utm_content=&aff="

website2= "https://shop.axs.co.uk/Lw%2fYCwAAAABDaUH%2fAAAAAAB%2b%2fv%2f%2f%2fwD%2f%2f%2f%2f%2fBmFtZXh1awD%2f%2f%2f%2f%2f%2f%2f%2f%2f%2fw%3d%3d/shop/search?skin=&tags=&cpch=&cpdate=&cpcn=&cpsrc=&intoff=&cid=&uk_et_cid=&utm_source=&utm_medium=&utm_campaign=&utm_term=&utm_content=&aff="

path ='/html/body/div[4]/div[2]/div/div/div[1]/h4'
path = '//*[@id="TICKET_SOLD_OUT"]/div/div/div[1]/h4'
# path = "modal-title"

compare_text = "There are currently no tickets available"



class TestPage():

    def setUp(self):
        self.options = Options()
        self.options.headless = False
        self.browser = webdriver.Chrome(chrome_options=self.options)
        self.count = 0


    def tearDown(self):
        self.browser.close()


    def available_ticket(self, url):
        self.browser.get(url)
        self.browser.implicitly_wait(100)
        # a = self.browser.find_elements_by_class_name(path)
        e = self.browser.find_element(By.XPATH, path)
        return e.text




def sendMessage(message):
    os.system("open -a Messages")

    time.sleep(5)

    keyboard = Controller()
    keyboard.type(message)
    time.sleep(1)
    keyboard.press(Key.enter)



def check_forever():

    loop = True
    new_hans = TestPage()
    new_hans.setUp()

    while loop:
        print("Now Searching...")
        a = new_hans.available_ticket(website1)
        b = new_hans.available_ticket(website2)
        if a != compare_text or b != compare_text: 
            loop = False
            sendMessage("tickets available....")
        else:
            print("No tickets found 😢")
            time.sleep(rest)

    new_hans.tearDown()



check_forever()
