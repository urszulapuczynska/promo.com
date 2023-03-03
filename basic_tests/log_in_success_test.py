import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
def test_log_in():
    PATH = 'Macintosh HD/Users/Urszula/Downloads/chromedriver_mac64 (1)'
    driver = webdriver.Chrome(PATH)

    email = 'please provide your credentials'
    password = 'please provide your credentials'

    driver.get("https://promo.com")
    assert 'Video Maker' in driver.title
    assert 'Power your business' in driver.page_source
    driver.maximize_window()
    driver.find_element(By.CSS_SELECTOR, '.signin.login.new-auth').click()

    driver.find_element(By.CSS_SELECTOR, "#email").send_keys(email)
    driver.find_element(By.CSS_SELECTOR, "#password").send_keys(password)
    driver.find_element(By.CSS_SELECTOR, "#password").send_keys(Keys.ENTER)
    time.sleep(3)
    assert 'My Workspace' in driver.page_source