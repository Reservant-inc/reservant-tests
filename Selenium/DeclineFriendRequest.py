from Classes.RandomData import RandomData
from utils.utils import *
from Selenium.UserLogin import test_user_login

ip = get_variable_value("IP_FRONTEND")
login_path = get_variable_value("LOGIN_USER")
register_path = get_variable_value("REGISTER_USER")

delay = int(get_variable_value("DELAY"))
login_url = f"http://{ip}{login_path}"
register_url = f"http://{ip}{register_path}"
home_path = get_variable_value("HOME_PATH")
home_url = f"http://{ip}{home_path}"


def test_decline_friend_invite(driver):
    info("TEST SENDING AND DECLINING A FRIEND INVITE")
    try:
        driver.get(home_url)
        wait_for_url_to_be(driver, home_url)

        # Sprawdzenie tytułu strony
        check_page_title(driver, "React App")

        wait_for_element(driver, By.ID, "root")

        # Otwieranie wyszukiwania znajomych i wyszukanie Ewa Przykładowska
        enter_text(driver, By.CSS_SELECTOR, "input.clean-input.h-8.w-\\[250px\\].p-2.placeholder\\:text-grey-2.dark\\:text-grey-1", "Ewa Przykładowska")
        wait_for(delay)

        # Wysyłanie zaproszenia do znajomych do pierwszego wyszukanego znajomego (w tym przypadku Ewa Przykładowska)
        click_button(driver, By.XPATH, "(//button[contains(text(), 'Send request') or contains(text(), 'Undo request')])[1]")
        wait_for(delay)

        # Sprawdzam czy poprawnie wysłano zaproszenie - tekst zmienia się na "Undo request"
        # Jeżeli zaproszenie było już wcześniej wysłane to wyrzuca błąd i kończy test
        find_text_in_elements(driver, By.XPATH, "(//button[contains(text(), 'Send request') or contains(text(), 'Undo request')])[1]", "Undo request", critical=True)

        # Odrzucanie zaproszenia z poziomu inputu do wyszukiwania osób

        # Wylogowywanie
        click_button(driver, By.ID, "ToolsButton")
        click_button(driver, By.ID, "logoutDropdownItem")

        # Logowanie na Ewę Przykładowską
        click_button(driver, By.ID, "serverLink")
        enter_text(driver, By.ID, "login", "customer2")
        enter_text(driver, By.ID, "password", "Pa$$w0rd")
        wait_for(delay)

        universal_wait_for(driver, EC.element_to_be_clickable, By.ID, "LoginLoginButton")
        click_button(driver, By.ID, "LoginLoginButton")

        # Zmiana strony
        wait_for_url_to_be(driver, home_url)

        # Wyszukanie John Doe żeby jego odrzucić zaproszenie z poziomu wyszukiwania
        enter_text(driver, By.CSS_SELECTOR,
                   "input.clean-input.h-8.w-\\[250px\\].p-2.placeholder\\:text-grey-2.dark\\:text-grey-1", "John Doe")
        wait_for(delay)

        # Odrzucenie zaproszenia
        click_button(driver, By.CSS_SELECTOR, "svg.MuiSvgIcon-root.MuiSvgIcon-fontSizeMedium.h-5.w-5.css-vubbuv")


        # Test się powiódł
        return True

    except Exception as e:
        result(str(e), False)
        info("Friend invite decline test failed")
        info(f"Current URL: {driver.current_url}")
        info(f"Page title: {driver.title}")
        return False  # Test nieudany

    finally:
        wait_for(delay)


if __name__ == "__main__":
    driver = webdriver.Edge()
    driver.maximize_window()
    test_user_login(driver, False)
    test_decline_friend_invite(driver)
    driver.quit()
