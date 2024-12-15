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
        #potrzebne ID

        # 1.2 sprawdzamy wyswietlane menu



        # 2.1 sprawdzamy czy można kliknąć "zarezerwuj"
        #potrzebne ID
        #click_button(driver, By.CSS_SELECTOR,
                    # '.h-12.w-12.rounded-full.border-[1px].border-primary.text-primary.transition.hover\\:scale-105.hover\\:bg-primary.hover\\:text-white.dark\\:border-secondary.dark\\:text-secondary.dark\\:text-secondary.dark\\:hover\\:bg-secondary.dark\\:hover\\:text-black')
        # 2.2 przenosi nas do ekranu logowania



        # 3.1 sprawdzamy czy można kliknąć "sprawdz wydarzenie"
        #potrzebne ID

        # 3.2 przenosi do ekranu logowania



        #sprawdzamy, ze wyswietla sie przycisk "LOGIN"
        #potrzebne ID
        click_button(driver, By.XPATH, "//button[text()='LOGIN']")
        current_url = driver.current_url
        assert current_url == login_url

        #go back
        driver.back()

        #sprawdzamy, ze wyswietla sie przycisk "REGISTER"
        #potrzebne ID
        click_button(driver, By.XPATH, "//button[text()='REGISTER']")
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


