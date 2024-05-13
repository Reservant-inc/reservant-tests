from Classes.LoginData import LoginData
from utils.utils import *

ip = get_variable_value("IP_FRONTEND")
register_path = get_variable_value("REGISTER_USER")
login_path = get_variable_value("LOGIN_USER")
delay = int(get_variable_value("DELAY"))
until = 10
register_url = f"http://{ip}{register_path}"
login_url = f"http://{ip}{login_path}"
sample_login = LoginData.generate_login_data()


def test_user_register(driver):
    driver.get(register_url)
    try:
        # Sprawdzenie tytułu
        assert "React App" in driver.title, f"Oczekiwano tytułu zawierającego 'React App', otrzymano: {driver.title}"

        result("Title is correct.")

        # Sprawdzenie czy istnieje elemenet o id root, w naszym przypadku div
        wait_for_element(driver, By.ID, "root")
        result("Main div is present.")

        # Znalezienie i kliknięcie przycisku
        click_button(driver, By.CSS_SELECTOR, "button")
        result("Successfully clicked the button")

        # Sprawdzenie czy pojawia się nowa zawartość
        wait_for_element(driver, By.CLASS_NAME, "text-pink")
        result("New content is displayed.")

        wait_for(delay)

        # Znaleznienie pola i wypełnienie go danymi
        enter_text(driver, By.ID, "firstName", sample_login.first_name)

        enter_text(driver, By.ID, "lastName", sample_login.last_name)

        enter_text(driver, By.ID, "login", sample_login.login)

        enter_text(driver, By.ID, "email", sample_login.email)

        enter_text(driver, By.CLASS_NAME, "PhoneInputInput", sample_login.phone_number)  # TODO id

        enter_text(driver, By.ID, "birthDate", sample_login.birth_day)

        enter_text(driver, By.ID, "password", sample_login.password)

        enter_text(driver, By.ID, "confirmPassword", sample_login.password)
        result("Form filled correctly")

        wait_for(delay)

        # Czekamy na pojawienie się przycisku
        universal_wait_for(driver, EC.element_to_be_clickable, By.CSS_SELECTOR, "button")
        result("Register button is clickable.")

        click_button(driver, By.CSS_SELECTOR, "button")
        result("Successfully clicked register button")

        # Czekamy na zmianę strony
        universal_wait_for(driver, EC.url_changes, different_value=register_url)
        result("URL has changed successfully")

        # Sprawdzenie czy strona zmieniła się na taką jaką chcemy w naszym przypadku login
        assert driver.current_url == login_url, f"URL did not change to expected. Current URL: {driver.current_url}"
        result("Form submitted successfully and result is correct.")

        return True  # Test przeszedł

    except Exception as e:
        result(str(e), False)
        info(f"Current URL: {driver.current_url}")
        info(f"Page title: {driver.title}")
        print("-----------------------")
        info("Errors displayed on the website:")
        info(get_text_from_elements_by_class(driver, By.CLASS_NAME, "text-pink"))
        print("-----------------------")
        info("Problem with following login data:")
        info(sample_login)
        return False  # Test nieudany


    finally:
        wait_for(delay)
