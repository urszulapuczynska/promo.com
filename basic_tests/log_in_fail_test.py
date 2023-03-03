import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from faker import Faker
fake = Faker()

def test_log_in():
    PATH = 'Macintosh HD/Users/Urszula/Downloads/chromedriver_mac64 (1)'
    driver = webdriver.Chrome(PATH)

    email = fake.email()
    password = 'promo12@test.com'

    driver.get("https://promo.com")
    assert 'Video Maker' in driver.title
    assert 'Power your business' in driver.page_source
    driver.maximize_window()
    driver.find_element(By.CSS_SELECTOR, '.signin.login.new-auth').click()

    driver.find_element(By.CSS_SELECTOR, "#email").send_keys(email)
    driver.find_element(By.CSS_SELECTOR, "#password").send_keys(password)
    driver.find_element(By.CSS_SELECTOR, "#password").send_keys(Keys.ENTER)
    time.sleep(3)
    error_message = driver.find_element(By.XPATH, "//span[@class='promo__input-message']")

    if "The email or password you entered is incorrect" in driver.page_source:
        print(error_message.text)
    else:
        print("You have registered using invalid email address or password.")
