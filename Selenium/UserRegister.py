import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Edge()

driver.get("http://172.21.40.127:800/user/register")


def wait_for(seconds):
    time.sleep(seconds)


try:
    # Sprawdzenie tytułu
    assert "React App" in driver.title
    print("Test Passed: Title is correct.")

    # Sprawdzenie czy istnieje elemenet o id root, w naszym przypadku div
    main_div = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "root"))
    )
    print("Test Passed: Main div is present.")

    # Znalezienie i kliknięcie przycisku
    wait_for(2)  # Lepiej używać WebDriverWait
    button = driver.find_element(By.CSS_SELECTOR, "button")  # TODO id
    button.click()

    # Sprawdzenie czy pojawia się nowa zawartość
    wait_for(2)
    new_content = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "text-pink"))
    )
    assert new_content.is_displayed()
    print("Test Passed: New content is displayed after clicking the button.")

    # Znaleznienie pola i wypełnienie go danymi
    input_field = driver.find_element(By.ID, "firstName")
    input_field.send_keys("Ktos")

    input_field = driver.find_element(By.ID, "lastName")
    input_field.send_keys("Nowak")

    input_field = driver.find_element(By.ID, "login")
    input_field.send_keys("login10")

    input_field = driver.find_element(By.ID, "email")
    input_field.send_keys("cos@cos.pl")

    input_field = driver.find_element(By.CLASS_NAME, "PhoneInputInput")  # TODO id
    input_field.send_keys("123456789")

    input_field = driver.find_element(By.ID, "birthDate")
    input_field.send_keys("01.01.1999")

    input_field = driver.find_element(By.ID, "password")
    input_field.send_keys("Test1234@")

    input_field = driver.find_element(By.ID, "confirmPassword")
    input_field.send_keys("Test1234@")
    # "Odklikujemy pole"
    input_field.send_keys(Keys.TAB)

    # Czekamy do 10 sekund na zmianę strony
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "button"))
    )

    button = driver.find_element(By.CSS_SELECTOR, "button")
    button.click()

    # Czekamy do 10 sekund na zmianę strony
    WebDriverWait(driver, 10).until(
        EC.url_changes("http://172.21.40.127:800/user/register")
    )

    # Sprawdzenie czy strona zmieniła się na taką jaką chcemy w naszym przypadku login
    expected_url = "http://172.21.40.127:800/user/login"
    current_url = driver.current_url
    assert current_url == expected_url, f"URL did not change to expected. Current URL: {current_url}"
    print("Test Passed: Form submitted successfully and result is correct.")

# Przykład zmiany strony
# driver.get("http://172.21.40.127:800/another-page")
# wait_for(2)
# assert "another-page" in driver.current_url
# print("Test Passed: Navigation to another page is successful.")

except Exception as e:
    print("Test Failed:", str(e))

finally:
    wait_for(5)
    driver.quit()
