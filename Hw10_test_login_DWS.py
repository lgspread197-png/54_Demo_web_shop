import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "https://demowebshop.tricentis.com/login"
EXPECTED_URL = "https://demowebshop.tricentis.com/"

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get(URL)

    yield driver

    driver.quit()


def test_log_in_and_checkbox(driver):

        element = driver.find_element(By.XPATH, "//input[@id='Email']")
        element2 = driver.find_element(By.XPATH, "//input[@id='Password']")
        checkbox = driver.find_element(By.XPATH,"//input[@id='RememberMe']")
        assert element.is_displayed()
        assert element2.is_displayed()
        assert checkbox.is_displayed()
        assert not checkbox.is_selected()

def test_lig_in_button_is_displayed(driver):

        button = driver.find_element(By.XPATH,"//input[@value='Log in']")
        button2 = driver.find_element(By.XPATH,"//input[@class='button-1 login-button']")
        assert button.is_displayed()
        assert button2.is_displayed()

def test_login_success(driver):
    driver.find_element(By.XPATH, "//input[@id='Email']").send_keys("lgspread197@gmail.com")
    driver.find_element(By.XPATH, "//input[@id='Password']").send_keys("lamgam")
    driver.find_element(By.XPATH, "//input[@id='RememberMe']").click()

    driver.find_element(By.XPATH,"//input[@value='Log in']").click()

    assert driver.current_url == EXPECTED_URL