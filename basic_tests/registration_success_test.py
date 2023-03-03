import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
from faker import Faker
fake = Faker()

def test_log_in():
    PATH = 'Macintosh HD/Users/Urszula/Downloads/chromedriver_mac64 (1)'
    driver = webdriver.Chrome(PATH)

    email = fake.email()
    full_name = 'Orszulkaa czyńska'
    password = 'aaromo12@test.com'

    driver.get("https://promo.com")
    assert 'Video Maker' in driver.title
    assert 'Power your business' in driver.page_source
    driver.maximize_window()
    wait = WebDriverWait(driver, 10, 0.5)
    driver.find_element(By.CSS_SELECTOR, '.signin.login.new-auth').click()
    assert driver.find_element(By.XPATH, "//button[normalize-space()='Continue with Google']").is_displayed()
    assert driver.find_element(By.XPATH, "//button[normalize-space()='Continue with Facebook']").is_displayed()
    driver.find_element(By.XPATH, "//button[normalize-space()='Sign up']").click()
    assert 'Get started for free' in driver.page_source

    driver.find_element(By.XPATH, "//input[@id='signup-email']").send_keys(email)
    driver.find_element(By.XPATH, "//input[@id='signup-fullName']").send_keys(full_name)
    driver.find_element(By.XPATH, "//input[@id='signup-password']").send_keys(password)

    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    time.sleep(3)
    assert 'Create Page' in driver.title
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, '.onBoarding-header__close-button--text').click()
    time.sleep(5)
    assert full_name in driver.page_source