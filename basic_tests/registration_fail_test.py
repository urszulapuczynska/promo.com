import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

def test_log_in():
    PATH = 'Macintosh HD/Users/Urszula/Downloads/chromedriver_mac64 (1)'
    driver = webdriver.Chrome(PATH)

    email = 'jankowalski'
    full_name = 'Orszulkaa czyńska'
    password = 'aaromo12@test.com'

    driver.get("https://promo.com")
    assert 'Video Maker' in driver.title
    assert 'Power your business' in driver.page_source
    driver.maximize_window()
    wait = WebDriverWait(driver, 10, 0.5)
    driver.find_element(By.CSS_SELECTOR, '.signin.login.new-auth').click()
    if driver.find_element(By.XPATH, "//button[normalize-space()='Sign up']").is_displayed():
        driver.find_element(By.XPATH, "//button[normalize-space()='Sign up']").click()
    else:
        print("Couldn\'t reach button")

    driver.find_element(By.XPATH, "//input[@id='signup-email']").send_keys(email)
    driver.find_element(By.XPATH, "//input[@id='signup-fullName']").send_keys(full_name)
    driver.find_element(By.XPATH, "//input[@id='signup-password']").send_keys(password)
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    error_message = driver.find_element(By.XPATH, "//span[@class='promo__input-message']")

    if "This is not an email address" in driver.page_source:
        print(driver.find_element(By.XPATH, "//span[@class='promo__input-message']").text)
    else:
        print("You have registered using invalid email address.")
