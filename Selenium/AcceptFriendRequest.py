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

# Jako że na ten moment nie ma opcji usuwania znajomych to ten test można odpalić tylko raz na konkretnego usera...


def test_accept_friend_invite(driver):
    info("TEST SENDING AND ACCEPTING A FRIEND INVITE")
    try:
        driver.get(home_url)
        wait_for_url_to_be(driver, home_url)

        # Sprawdzenie tytułu strony
        check_page_title(driver, "React App")

        wait_for_element(driver, By.ID, "root")

        # Otwieranie wyszukiwania znajomych i wyszukanie ...
        enter_text(driver, By.CSS_SELECTOR, "input.clean-input.h-8.w-\\[250px\\].p-2.placeholder\\:text-grey-2.dark\\:text-grey-1", "Paul Atreides")
        wait_for(delay)

        # Wysyłanie zaproszenia do znajomych do pierwszego wyszukanego znajomego (w tym przypadku PA)
        click_button(driver, By.XPATH, "(//button[contains(text(), 'Send request') or contains(text(), 'Undo request')])[1]")
        wait_for(delay)

        # Sprawdzam czy poprawnie wysłano zaproszenie - tekst w przycisku zmienia się na "Undo request"
        # Jeżeli zaproszenie było już wcześniej wysłane to wyrzuca błąd i kończy test
        find_text_in_elements(driver, By.XPATH, "(//button[contains(text(), 'Send request') or contains(text(), 'Undo request')])[1]", "Undo request", critical=True)

        # Akceptacja zaproszenia z poziomu powiadomień

        # Wylogowywanie
        # todo podmienić jak pojawi się mój pull request z fixem na serwerze
        click_button(driver, By.ID, "ToolsButton")
        # click_button(driver, By.ID, "logoutDropdownItem")
        click_button(driver, By.XPATH, "//span[contains(text(), 'Wylogowanie') or contains(text(), 'Sign out')]", "Wylogowanie lub Sign out")


        # Logowanie na PA
        # TODO quick fix na teraz, trzeba dorobić id nowym przyciskom logowania
        click_button(driver, By.XPATH, "//button[contains(text(), 'LOGIN')]")
        enter_text(driver, By.ID, "login", "PA")
        enter_text(driver, By.ID, "password", "Pa$$w0rd")

        universal_wait_for(driver, EC.element_to_be_clickable, By.ID, "LoginLoginButton")
        click_button(driver, By.ID, "LoginLoginButton")
        wait_for(delay)

        # Kliakamy guzik powiadomień
        wait_for_element(driver, By.ID, "navbarNotificationsButton").click()
        wait_for(delay)

        # Klikamy guzik "Wyświetl więcej"
        click_button(driver, By.ID, "showMoreNotificationsButton")
        wait_for(delay)

        # Klikamy zakładkę Friends
        click_button(driver, By.ID, "notificationsFriendsTab")
        wait_for(delay)

        # Szukam i klikam "Zaakceptuj"
        click_button(driver, By.ID, "JohnDoeNotificationAcceptFriendRequest")
        wait_for(delay)

        # Test się powiódł
        return True

    except Exception as e:
        result(str(e), False)
        info("Friend invite test failed")
        info(f"Current URL: {driver.current_url}")
        info(f"Page title: {driver.title}")
        return False  # Test nieudany

    finally:
        wait_for(delay)


if __name__ == "__main__":
    driver = webdriver.Edge()
    driver.maximize_window()
    test_user_login(driver, False)
    test_accept_friend_invite(driver)
    driver.quit()
