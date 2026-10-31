import pytest
import uuid
from selenium import webdriver
from selenium.webdriver.common.by import By

REGISTER_URL = "https://demowebshop.tricentis.com/register"
LOGIN_URL = "https://demowebshop.tricentis.com/login"
EXPECTED_URL = "https://demowebshop.tricentis.com/"

EMAIL = f"vladimir_{uuid.uuid4().hex[:8]}@example.com"   #Генерация уникального идентификатора
PASSWORD = "TestPassword123!"

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get(REGISTER_URL)

    yield driver

    driver.quit()


def test_registration_and_login(driver):

    # Registration
    driver.find_element(By.CSS_SELECTOR, "#gender-male").click()
    driver.find_element(By.ID, "FirstName").send_keys("Vladimir")
    driver.find_element(By.ID, "LastName").send_keys("Vladimir")
    driver.find_element(By.ID, "Email").send_keys(EMAIL)
    driver.find_element(By.ID, "Password").send_keys(PASSWORD)
    driver.find_element(By.ID, "ConfirmPassword").send_keys(PASSWORD)

    driver.find_element(By.ID, "register-button").click()

    message = driver.find_element(By.CLASS_NAME, "result")
    # предполагается, что после регистрации появляется сообщение .result
    assert "Your registration completed" in message.text
    # Проверить сообщение об успешной регистрации (message.text	- Получение текста со страницы)

    # выход после регистрации (после выхода доступна ссылка a.ico-logout)
    driver.find_element(By.CSS_SELECTOR, "a.ico-logout").click()

    # Login
    driver.get(LOGIN_URL)

    driver.find_element(By.ID, "Email").send_keys(EMAIL)
    driver.find_element(By.ID, "Password").send_keys(PASSWORD)
    driver.find_element(By.XPATH, "//input[@id='RememberMe']").click()

    driver.find_element(By.XPATH, "//input[@value='Log in']").click()

    assert driver.current_url == EXPECTED_URL