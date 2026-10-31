import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "https://icarro-v1.netlify.app/login"
EXPECTED_URL = "https://icarro-v1.netlify.app"

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get(URL)

    yield driver

    driver.quit()


def test_login(driver):
    element = driver.find_element(By.CSS_SELECTOR, "input[name='username']")
    element2 = driver.find_element(By.CSS_SELECTOR, "input[name='password']")

    assert element.is_displayed()
    assert element2.is_displayed()


def test_lig_in_button_is_displayed(driver):
    button = driver.find_element(By.XPATH, "//button[contains(text(),'Y’alla!')]")
    assert button.is_displayed()

def test_login_success(driver):
    driver.find_element(By.CSS_SELECTOR, "input[name='username']").send_keys("lgspread197@gmail.com")
    driver.find_element(By.CSS_SELECTOR, "input[name='password']").send_keys("lgspread197")

    driver.find_element(By.XPATH,"//button[contains(text(),'Y’alla!')]").click()

    assert driver.current_url == EXPECTED_URL