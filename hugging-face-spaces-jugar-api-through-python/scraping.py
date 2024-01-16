import traceback
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC





    


if __name__ == '__main__':
    url = 'https://huggingface.co/spaces/HumanAIGC/OutfitAnyone'
    s = Service(r'C:\Users\pseudo\firefoxdriver.exe')
    driver = webdriver.Firefox(service=s)

    driver.get(url)
    driver.maximize_window()
    sleep(5)

    driver.quit()
