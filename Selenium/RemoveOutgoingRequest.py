# Usuwa wychodzące zaproszenie do znajomych z zakładki Profil > Znajomi.
# Przed odpaleniem należy wykonać recreate database.

from utils.utils import *
from Selenium.UserLogin import test_user_login

ip = get_variable_value("IP_FRONTEND")
login_path = get_variable_value("LOGIN_USER")
register_path = get_variable_value("REGISTER_USER")

delay = int(get_variable_value("DELAY"))
login_url = f"http://{ip}{login_path}"
home_path = get_variable_value("HOME_PATH")
home_url = f"http://{ip}{home_path}"

def test_remove_outgoing_request(driver):
    info("REMOVE AN OUTGOING FRIEND REQUEST VIA USER'S PROFILE TAB")
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

        # Przełączam zakładkę na 'Wysłane zaproszenia'
        click_button(driver, By.XPATH, "//button[contains(text(), 'Wysłane zaproszenia') or contains(text(), 'Outgoing requests')]")
        wait_for(delay)

        # Szukam elementu listy który zawiera 'Geralt Riv'
        # Jeśli nie ma elementu to kończy tekst (trzeba wykonać recreate database)
        li_element = wait_for_element(driver, By.XPATH, "//li[contains(., 'Geralt') and contains(., 'Riv')]",
                                      critical=True)

        # Szukam guzika do cofnięcia zaproszenia
        button = li_element.find_element(By.CSS_SELECTOR, "button.mt-2.border-\\[1px\\].text-sm.p-2.w-fit.rounded-lg.bg-grey-0.border-primary.text-primary.transition.hover\\:scale-105.hover\\:bg-primary.hover\\:text-white")
        button.click()
        wait_for(delay)

        return True

    except Exception as e:
        result(str(e), False)
        info("Friend request removal test failed")
        info(f"Current URL: {driver.current_url}")
        info(f"Page title: {driver.title}")
        return False  # Test nieudany

    finally:
        wait_for(delay)


if __name__ == "__main__":
    driver = webdriver.Edge()
    driver.maximize_window()
    test_user_login(driver, False)
    test_remove_outgoing_request(driver)
    driver.quit()