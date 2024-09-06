from Classes.LoginData import LoginData
from utils.utils import *

ip = get_variable_value("IP_FRONTEND")
register_path = get_variable_value("REGISTER_USER")
login_path = get_variable_value("LOGIN_USER")
delay = int(get_variable_value("DELAY"))
register_url = f"http://{ip}{register_path}"
login_url = f"http://{ip}{login_path}"
sample_login = LoginData.generate_login_data()


def test_user_register(driver):
    info("USER REGISTER TEST")
    driver.get(register_url)
    try:
        # Sprawdzenie tytułu
        assert "React App" in driver.title, f"Oczekiwano tytułu zawierającego 'React App', otrzymano: {driver.title}"

        result("Title is correct.")

        # Sprawdzenie czy istnieje elemenet o id root, w naszym przypadku div
        wait_for_element(driver, By.ID, "root")
        result("Main div is present.")

        #LOGIN
        # Znalezienie i kliknięcie przycisku
        click_text_field(driver, By.ID, "login")
        result("Successfully clicked the login text field")

        press_tab_key(driver)

        # Sprawdzenie czy pojawia się nowa zawartość
        wait_for_element(driver, By.ID, "login-helper-text")
        result("Login error is displayed.")

        # EMAIL
        click_text_field(driver, By.ID, "email")
        result("Successfully clicked the email text field")

        press_tab_key(driver)

        wait_for_element(driver, By.ID, "email-helper-text")
        result("Email error is displayed.")

        # PASSWORD
        click_text_field(driver, By.ID, "password")
        result("Successfully clicked the password text field")

        press_tab_key(driver)

        wait_for_element(driver, By.ID, "password-helper-text")
        result("Password error is displayed.")

        # CONFIRM PASSWORD
        click_text_field(driver, By.ID, "confirmPassword")
        result("Successfully clicked the confirm password text field")

        press_tab_key(driver)

        wait_for_element(driver, By.ID, "confirmPassword-helper-text")
        result("Confirm password error is displayed.")

        wait_for(delay)

        # Znaleznienie pola i wypełnienie go danymi

        enter_text(driver, By.ID, "login", sample_login.login)

        enter_text(driver, By.ID, "email", sample_login.email)

        enter_text(driver, By.ID, "password", sample_login.password)

        enter_text(driver, By.ID, "confirmPassword", sample_login.password)
        result("Form filled correctly")

        wait_for(delay)

        # Czekamy na pojawienie się przycisku
        universal_wait_for(driver, EC.element_to_be_clickable, By.CSS_SELECTOR, "button")
        result("NEXT button is clickable.")

        click_button(driver, By.CSS_SELECTOR, "button")
        result("Successfully clicked NEXT button")

        universal_wait_for(driver, EC.element_to_be_clickable, By.ID, "firstName")

        # FIRST NAME
        click_text_field(driver, By.ID, "firstName")
        result("Successfully clicked the first name text field")

        press_tab_key(driver)

        wait_for_element(driver, By.ID, "firstName-helper-text")
        result("First name error is displayed.")

        # LAST NAME
        click_text_field(driver, By.ID, "lastName")
        result("Successfully clicked the last name text field")

        press_tab_key(driver)

        wait_for_element(driver, By.ID, "lastName-helper-text")
        result("Last name error is displayed.")

        # PHONE
        click_text_field(driver, By.ID, "userRegister-phoneNumber-field")
        result("Successfully clicked the phone text field")

        press_tab_key(driver)

        wait_for_element(driver, By.ID, "userRegister-phoneNumber-field")
        result("Phone error is displayed.")

        # DATE
        click_text_field(driver, By.ID, "birthDate")
        result("Successfully clicked the birth date text field")

        press_tab_key(driver)

        wait_for_element(driver, By.ID, "userRegister-phoneNumber-field")
        result("Birth date error is displayed.")

        enter_text(driver, By.ID, "firstName", sample_login.first_name)

        enter_text(driver, By.ID, "lastName", sample_login.last_name)

        enter_text(driver, By.ID, "userRegister-phoneNumber-field", sample_login.phone_number)

        enter_text(driver, By.ID, "birthDate", sample_login.birth_day)

        # Czekamy na pojawienie się przycisku
        #TODO id
        universal_wait_for(driver, EC.element_to_be_clickable, By.CSS_SELECTOR, "button.pointer:nth-child(2)")
        result("SUBMIT button is clickable.")

        click_button(driver, By.CSS_SELECTOR, "button.pointer:nth-child(2)")
        result("Successfully clicked SUBMIT button")

        # Czekamy na zmianę strony
        universal_wait_for(driver, EC.url_changes, different_value=register_url)
        result("URL has changed successfully")

        # Sprawdzenie czy strona zmieniła się na taką jaką chcemy w naszym przypadku login
        assert driver.current_url == login_url, f"URL did not change to expected. Current URL: {driver.current_url}"
        result("Form submitted successfully and result is correct.")

        return True  # Test przeszedł

    except Exception as e:
        result(str(e), False)
        info("User register test failed")
        info(f"Current URL: {driver.current_url}")
        info(f"Page title: {driver.title}")
        print("-----------------------")
        info("Problem with following login data:")
        info(sample_login)
        return False  # Test nieudany


    finally:
        wait_for(delay)


if __name__ == "__main__":
    driver = webdriver.Edge()
    test_user_register(driver)
    driver.quit()