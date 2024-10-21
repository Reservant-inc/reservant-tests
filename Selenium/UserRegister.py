from Classes.RandomData import RandomData
from utils.utils import *

ip = get_variable_value("IP_FRONTEND")
register_path = get_variable_value("REGISTER_USER")
login_path = get_variable_value("LOGIN_USER")
delay = int(get_variable_value("DELAY"))
register_url = f"http://{ip}{register_path}"
login_url = f"http://{ip}{login_path}"


def test_user_register(driver):
    info("USER REGISTER TEST")
    driver.get(register_url)
    try:
        # Sprawdzenie tytułu
        check_page_title(driver, "React App")

        # Sprawdzenie czy istnieje elemenet o id root, w naszym przypadku div
        wait_for_element(driver, By.ID, "root")

        #LOGIN
        # Znalezienie i kliknięcie przycisku
        click_text_field(driver, By.ID, "login")

        press_tab_key(driver)

        # Sprawdzenie czy pojawia się nowa zawartość
        wait_for_element(driver, By.ID, "login-helper-text")

        # EMAIL
        click_text_field(driver, By.ID, "email")

        press_tab_key(driver)

        wait_for_element(driver, By.ID, "email-helper-text")

        # PASSWORD
        click_text_field(driver, By.ID, "password")

        press_tab_key(driver)

        wait_for_element(driver, By.ID, "password-helper-text")

        # CONFIRM PASSWORD
        click_text_field(driver, By.ID, "confirmPassword")

        press_tab_key(driver)

        wait_for_element(driver, By.ID, "confirmPassword-helper-text")

        wait_for(delay)

        # Znaleznienie pola i wypełnienie go danymi

        enter_text(driver, By.ID, "login", RandomData.generate_login())

        enter_text(driver, By.ID, "email", RandomData.generate_email())

        password = RandomData.generate_password()

        enter_text(driver, By.ID, "password", password)

        enter_text(driver, By.ID, "confirmPassword", password)
        result("Form filled correctly")

        wait_for(delay)

        # Czekamy na pojawienie się przycisku
        universal_wait_for(driver, EC.element_to_be_clickable, By.CSS_SELECTOR, "button")

        click_button(driver, By.CSS_SELECTOR, "button")

        universal_wait_for(driver, EC.element_to_be_clickable, By.ID, "firstName")

        # FIRST NAME
        click_text_field(driver, By.ID, "firstName")

        press_tab_key(driver)

        wait_for_element(driver, By.ID, "firstName-helper-text")

        # LAST NAME
        click_text_field(driver, By.ID, "lastName")

        press_tab_key(driver)

        wait_for_element(driver, By.ID, "lastName-helper-text")

        # PHONE
        click_text_field(driver, By.ID, "userRegister-phoneNumber-field")

        press_tab_key(driver)

        wait_for_element(driver, By.ID, "userRegister-phoneNumber-field")

        # DATE
        click_text_field(driver, By.ID, "birthDate")

        press_tab_key(driver)

        wait_for_element(driver, By.ID, "userRegister-phoneNumber-field")

        enter_text(driver, By.ID, "firstName", RandomData.generate_first_name())

        enter_text(driver, By.ID, "lastName", RandomData.generate_last_name())

        enter_text(driver, By.ID, "userRegister-phoneNumber-field", RandomData.generate_phone())

        enter_text(driver, By.ID, "birthDate", RandomData.generate_birth_date())

        # Czekamy na pojawienie się przycisku
        #TODO id
        universal_wait_for(driver, EC.element_to_be_clickable, By.CSS_SELECTOR, "button.pointer:nth-child(2)")

        click_button(driver, By.CSS_SELECTOR, "button.pointer:nth-child(2)")

        # Czekamy na zmianę strony
        universal_wait_for(driver, EC.url_changes, different_value=register_url)

        # Sprawdzenie czy strona zmieniła się na taką jaką chcemy w naszym przypadku login
        wait_for_url_to_be(driver, login_url)

        return True  # Test przeszedł

    except Exception as e:
        result(str(e), False)
        info("User register test failed")
        info(f"Current URL: {driver.current_url}")
        info(f"Page title: {driver.title}")
        return False  # Test nieudany


    finally:
        wait_for(delay)


if __name__ == "__main__":
    driver = webdriver.Edge()
    test_user_register(driver)
    driver.quit()