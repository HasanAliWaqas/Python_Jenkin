import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


@pytest.fixture(scope="module")
def driver():
    # Optional: Set up Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")  # Start maximized

    # Set up the Chrome driver
    driver=webdriver.Chrome()

    yield driver

    # Clean up
    driver.quit()


def test_login(driver):
    driver.get("https://hrm.manxel.com/")

    # Wait for the page title to be loaded
    WebDriverWait(driver, 10).until(EC.title_contains("Manxel"))
    title = driver.title
    print("Page title is:", title)

    username = "hassan.ali@therocketdigital.com"
    password = "Hasan123@"

    # Wait for the login fields to be present
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "email")))
    username_field = driver.find_element(By.ID, "email")
    password_field = driver.find_element(By.ID, "password")

    # Enter login credentials
    username_field.send_keys(username)
    password_field.send_keys(password)

    # Locate and click the login button
    # Update the XPath to the correct value
    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")  # Update XPath if necessary

    # Wait for login button to be clickable and then click it
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
    assert not login_button.get_attribute("disabled")
    login_button.click()

    # Wait for successful login and check success message
    success_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div.page-title-box h3")))
    # assert success_element.text == "Manxel"
    print("Login successful. Page title is:", success_element.text)
