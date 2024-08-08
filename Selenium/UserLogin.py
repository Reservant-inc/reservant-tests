from utils.utils import *
import random

ip = get_variable_value("IP_FRONTEND")
login_path = get_variable_value("LOGIN_USER")
register_path = get_variable_value("REGISTER_USER")
delay = int(get_variable_value("DELAY"))
login_url = f"http://{ip}{login_path}"
register_url = f"http://{ip}{register_path}"


def test_user_login(driver):
    info("USER LOGIN TEST")
    email = "Not selected yet"
    driver.get(login_url)
    try:
        # Sprawdzenie tytułu
        assert "React App" in driver.title, f"Oczekiwano tytułu zawierającego 'React App', otrzymano: {driver.title}"
        result("Title is correct.")

        wait_for_element(driver, By.ID, "root")
        result("Main div is present. ")

        wait_for(delay)
        # LOGIN
        # Znalezienie i kliknięcie przycisku
        click_text_field(driver, By.ID, "login")
        result("Successfully clicked the login text field")

        press_tab_key(driver)

        # Sprawdzenie czy pojawia się nowa zawartość
        wait_for_element(driver, By.ID, "login-helper-text")
        result("Login error is displayed.")

        # PASSWORD
        click_text_field(driver, By.ID, "password")
        result("Successfully clicked the password text field")

        press_tab_key(driver)

        wait_for_element(driver, By.ID, "password-helper-text")
        result("Password error is displayed.")

        # Wybór losowego adresu email
        email = wybierz_email()
        enter_text(driver, By.ID, "login", email)

        enter_text(driver, By.ID, "password", "Pa$$w0rd")

        universal_wait_for(driver, EC.element_to_be_clickable, By.ID, "LoginLoginButton")
        result("Login button is clickable.")

        click_button(driver, By.ID, "LoginLoginButton")

        # Zmiana strony
        universal_wait_for(driver, EC.url_changes, different_value=login_url)
        result("URL has changed successfully - user has logged in!")

        # ==========================
        # Return to the login page and click "Sign In"
        click_button(driver, By.ID, "ToolsButton")
        click_button(driver, By.ID, "logoutDropdownItem")
        click_button(driver, By.ID, "serverLink")
        result("Successfully logged out and returned to login site.")
        wait_for(delay)
        universal_wait_for(driver, EC.url_to_be, different_value=login_url)
        result("URL has changed successfully to the login page!")
        wait_for_element(driver, By.ID, "root")
        click_button(driver, By.ID, "login-notRegistered-link")
        result("Successfully clicked register button")

        # Verify URL change
        universal_wait_for(driver, EC.url_to_be, different_value=register_url)
        result("URL has changed successfully to the register page!")

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
    adresy_email = ["JD", "customer", "support@mail.com", "manager@mail.com", "JD+hall", "JD+backdoors", "JD+employee"]
    wybrany_email = random.choice(adresy_email)
    return wybrany_email


if __name__ == "__main__":
    driver = webdriver.Edge()
    test_user_login(driver)
    driver.quit()
