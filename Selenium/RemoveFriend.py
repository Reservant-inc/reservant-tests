# Usuwa znajomego. Przed każdym odpaleniem należy wykonać recreate database, żeby upewnić się, że
# KK jest na liście znajomych JB

from utils.utils import *
from Selenium.UserLogin import test_user_login

ip = get_variable_value("IP_FRONTEND")
login_path = get_variable_value("LOGIN_USER")
register_path = get_variable_value("REGISTER_USER")

delay = int(get_variable_value("DELAY"))
login_url = f"http://{ip}{login_path}"
home_path = get_variable_value("HOME_PATH")
home_url = f"http://{ip}{home_path}"


def test_remove_friend(driver):
    info("TEST REMOVING A FRIEND FROM YOUR FRIENDS LIST VIA USER'S PROFILE TAB")
    try:
        driver.get(home_url)
        wait_for_url_to_be(driver, home_url)

        # Sprawdzenie tytułu strony
        check_page_title(driver, "React App")
        wait_for_element(driver, By.ID, "root")

        # Klikaw na avatar
        click_button(driver, By.ID, "ToolsButton")
        wait_for(delay)

        # Klikam Profil
        click_button(driver, By.ID, "profileDropdownItem")
        wait_for(delay)

        # Otwieram zakładkę Znajomi
        click_button(driver, By.XPATH, "//h1[contains(text(), 'Friends') or contains(text(), 'Znajomi')]")
        wait_for(delay)

        # Szukam elementu listy który zawiera 'Krzysztof Kowalski'
        # Jeśli nie ma elementu to kończy tekst (trzeba wykonać rebuild db)
        # TODO id
        li_element = wait_for_element(driver, By.XPATH, "//li[contains(., 'Krzysztof') and contains(., 'Kowalski')]",
                                      critical=True)

        # Szukam diva z przyciskami
        div_element = li_element.find_element(By.CSS_SELECTOR, "div.flex.gap-4.mt-2")

        # Szukam pierwszy guzik (Odpowiedzialny za usuwanie znajomego)
        first_child = div_element.find_element(By.XPATH, "./*")
        first_child.click()
        wait_for(delay)

        # Klikam 'Tak' w Popupie potwierdzającym usunięcie znajomego
        click_button(driver, By.XPATH, "(//button[contains(text(), 'Tak') or contains(text(), 'Yes')])")
        wait_for(delay)

        return True
    except Exception as e:
        result(str(e), False)
        info("Friend removal test failed")
        info(f"Current URL: {driver.current_url}")
        info(f"Page title: {driver.title}")
        return False  # Test nieudany

    finally:
        wait_for(delay)


if __name__ == "__main__":
    driver = webdriver.Edge()
    driver.maximize_window()
    test_user_login(driver, False)
    test_remove_friend(driver)
    driver.quit()
