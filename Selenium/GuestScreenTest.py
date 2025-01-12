from Classes.RandomData import RandomData
from utils.utils import *


ip = get_variable_value("IP_FRONTEND")
delay = int(get_variable_value("DELAY"))
home_url = f"http://{ip}/"
login_url = f"{home_url}login"
register_url = f"{home_url}register"

def test_guest_screen (driver):
    info("Guest screen test")
    try:
        driver.get(home_url)
        wait_for_url_to_be(driver, home_url)

        check_page_title(driver, "React App")

        wait_for_element(driver, By.ID, "root")

        #sprawdzamy, ze uzytkownik moze przegladac mape
        map_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "map"))
        )

        actions = ActionChains(driver)
        actions.click_and_hold(map_element).move_by_offset(100, 100).release().perform()
        print("Przesunięcie mapy działa.")

        # Sprawdź możliwość przybliżania i oddalania mapy
        print("Zoom mapy działa.")


        #sprawdzamy, ze wyswietlaja sie restauracja
        click_text_field(driver, By.ID, "homePage-listItemButton")
        wait_for(delay)

        # 1.1 sprawdzamy czy można kliknąć "menu"
        #click_button(driver, By.ID, "menu-guest")
        # 1.2 sprawdzamy wyswietlane menu
        # menu nie wyświetla się dla ekranu gościa
        #driver.back()
        # actions.click_and_hold(map_element).move_by_offset(100, 100).release().perform()
        # click_text_field(driver, By.ID, "homePage-listItemButton")
        # wait_for(delay)

        # 2.1 sprawdzamy czy można kliknąć "zarezerwuj"
        click_button(driver, By.ID, "reservation-guest")
        # 2.2 przenosi nas do ekranu logowania
        wait_for_url_to_be(driver, login_url, True)
        driver.back()
        #musimy poruszyć mapa, zeby pojawila sie restauracja
        map_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "map"))
        )
        actions.click_and_hold(map_element).move_by_offset(100, 100).release().perform()
        click_text_field(driver, By.ID, "homePage-listItemButton")
        wait_for(delay)

        # 3.1 sprawdzamy czy można kliknąć "sprawdz wydarzenie"
        click_button(driver, By.ID, "events-guest")
        # 3.2 przenosi do ekranu logowania
        wait_for_url_to_be(driver, login_url, True)
        driver.back()

        #sprawdzamy, ze wyswietla sie przycisk "LOGIN"
        click_button(driver, By.ID, "login-guest-navbar")
        current_url = driver.current_url
        assert current_url == login_url
        driver.back()

        #sprawdzamy, ze wyswietla sie przycisk "REGISTER"
        click_button(driver, By.ID, "register-guest-navbar")
        current_url = driver.current_url
        assert current_url == register_url

    except Exception as e:
        result(str(e), False)
        info("Guest screen test failed")
        info(f"Current URL: {driver.current_url}")
        info(f"Page title: {driver.title}")
        return False  # Test nieudany

    finally:
        wait_for(delay)


if __name__ == "__main__":
    driver = webdriver.Edge()
    driver.maximize_window()
    test_guest_screen(driver)
    driver.quit()


