from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://hrm.manxel.com/")

driver.maximize_window()

title = driver.title
print(title)


username = "hassan.ali@therocketdigital.com"
password = "Hasan123@"
login_url = "https://hrm.manxel.com/"
driver.get(login_url)

username_field = driver.find_element(By.ID, "email")
password_field = driver.find_element(By.ID, "password")

username_field.send_keys(username)
password_field.send_keys(password)

login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
assert not login_button.get_attribute("disabled")
login_button.click()

success_element = driver.find_element(By.CSS_SELECTOR, "div[class='page-title-box'] h3")
assert success_element.text == "Manxel"
