from utils.utils import *
import random

ip = get_variable_value("IP_FRONTEND")
login_path = get_variable_value("LOGIN_USER")
delay = int(get_variable_value("DELAY"))
until = 10
login_url = f"http://{ip}{login_path}"


def test_user_login(driver):
    driver.get(login_url)
    try:
        # Sprawdzenie tytułu
        assert "React App" in driver.title, f"Oczekiwano tytułu zawierającego 'React App', otrzymano: {driver.title}"
        result("Title is correct.")

        wait_for_element(driver, By.ID, "root")
        result("Main div is present. ")

        wait_for(delay)
        click_button(driver, By.CSS_SELECTOR, "button")

        wait_for(delay)
        new_content = wait_for_element(driver, By.ID, "root")
        assert new_content.is_displayed()
        result("New content is displayed after clicking the button.")

        # Wybór losowego adresu email
        email = wybierz_email()
        enter_text(driver, By.ID, "login", email)

        enter_text(driver, By.ID, "password", "Pa$$w0rd")

        driver.find_element(By.ID, "password").send_keys(Keys.TAB)  # TODO: entering tab via enter_text

        universal_wait_for(driver, EC.element_to_be_clickable, By.CSS_SELECTOR, "button")
        result("Login button is clickable.")

        click_button(driver, By.CSS_SELECTOR, "button")

        # Zmiana strony
        universal_wait_for(driver, EC.url_changes, different_value=login_url)
        result("URL has changed successfully - user has logged in!")

        # ================

    except Exception as e:
        result(str(e), False)
        info(f"Current URL: {driver.current_url}")
        info(f"Page title: {driver.title}")
        print("-----------------------")
        info("Errors displayed on the website:")
        print("to be implemented!") # TODO: no "Invalid credentials" error
        #info(get_text_from_elements_by_class(driver, By.CLASS_NAME, "text-pink"))
        print("-----------------------")
        info("Problem with following login data:")
        info(f"Login: {email}, password: Pa$$w0rd")
        return False  # Test nieudany

    finally:
        wait_for(delay)


def wybierz_email():  #Funkcja wybierająca ranomowy login z podanych
    adresy_email = ["JD", "customer", "support@mail.com", "manager@mail.com", "JD+hall", "JD+backdoors", "JD+employee"]
    wybrany_email = random.choice(adresy_email)
    return wybrany_email


if __name__ == "__main__":
    driver = webdriver.Edge()
    test_user_login(driver)
    driver.quit()
