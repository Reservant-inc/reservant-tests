from utils.utils import *
import random

ip = get_variable_value("IP_FRONTEND")
login_path = get_variable_value("LOGIN_USER")
register_path = get_variable_value("REGISTER_USER")
delay = int(get_variable_value("DELAY"))

login_url = f"http://{ip}{login_path}"
register_url = f"http://{ip}{register_path}"
home_path = get_variable_value("HOME_PATH")
home_url = f"http://{ip}{home_path}"


def test_user_login(driver, check_signup = True):
    """
    Dokumentacja - czyli co to robi
    """
    info("USER LOGIN TEST")
    email = "Not selected yet"

    driver.get(login_url)
    try:
        # Sprawdzenie tytułu
        check_page_title(driver, "React App")

        wait_for_element(driver, By.ID, "root")

        wait_for(delay)
        # LOGIN
        # Znalezienie i kliknięcie przycisku
        click_text_field(driver, By.ID, "login")

        press_tab_key(driver)

        # Sprawdzenie czy pojawia się nowa zawartość
        wait_for_element(driver, By.ID, "login-helper-text")

        # PASSWORD
        click_text_field(driver, By.ID, "password")

        press_tab_key(driver)

        wait_for_element(driver, By.ID, "password-helper-text")

        # Wybór losowego adresu email
        email = wybierz_email()
        enter_text(driver, By.ID, "login", email)

        enter_text(driver, By.ID, "password", "Pa$$w0rd")

        # Sprawdzenie, czy przycisk jest klikalny
        universal_wait_for(driver, EC.element_to_be_clickable, By.ID, "LoginLoginButton")

        click_button(driver, By.ID, "LoginLoginButton")

        # Zmiana strony
        wait_for_url_to_be(driver, home_url)

        # jeśli chcemy sprawdzić dodatkowo czy działa przycisk rejestracji przy logowaniu
        if(check_signup):
            # Return to the login page and click "Sign In"
            click_button(driver, By.ID, "ToolsButton")
            click_button(driver, By.ID, "logoutDropdownItem")
            click_button(driver, By.ID, "serverLink")
            wait_for(delay)
            universal_wait_for(driver, EC.url_to_be, different_value=login_url)
            wait_for_element(driver, By.ID, "root")
            click_button(driver, By.ID, "login-notRegistered-link")

            # Verify URL change
            wait_for_url_to_be(driver, register_url)

    except Exception as e:
        result(str(e), False)
        info("User login test failed")
        info(f"Current URL: {driver.current_url}")
        info(f"Page title: {driver.title}")
        print("-----------------------")
        info("Problem with following login data:")
        info(f"Login: {email}, password: Pa$$w0rd")
        return False  # Test nieudany

    finally:
        wait_for(delay)


def wybierz_email():  # Funkcja wybierająca ranomowy login z podanych
    adresy_email = ["JD"]
    wybrany_email = random.choice(adresy_email)
    return wybrany_email


if __name__ == "__main__":
    driver = webdriver.Edge()
    test_user_login(driver)
    driver.quit()
