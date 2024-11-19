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


def test_menu_management(driver):
    info("TEST MENU MANAGEMENT")
    try:
        driver.get(home_url)
        wait_for_url_to_be(driver, home_url)

        # TWORZENIE MENU
        check_page_title(driver, "React App")

        wait_for_element(driver, By.ID, "root")

        click_button(driver, By.ID, "NavbarRestaurantsSectionButton")
        wait_for(delay)

        find_text_in_elements(driver, By.CSS_SELECTOR, "div.flex.items-center.gap-4", "Restaurants").click()
        wait_for(delay)

        click_button(driver, By.CSS_SELECTOR, '[data-testid="ArrowForwardIosIcon"]')
        wait_for(delay)

        find_text_in_elements(driver, By.CSS_SELECTOR, "div.flex.items-center.gap-4", "Reviews").click()

        click_button(driver, By.CSS_SELECTOR, '[data-testid="SwapVertIcon"]')
        wait_for(delay)
        respond_button = driver.find_element(By.XPATH,'//button[contains(@class, "MuiButton-root") and contains(text(), "Respond")]')
        respond_button.click()

        textarea = driver.find_element(By.XPATH, '//textarea[@placeholder="Write your response"]')
        textarea.send_keys('Testowa odpowiedz do recenzji')
        save_button = driver.find_element(By.XPATH, '//button[contains(text(), "Save")]')
        save_button.click()
        wait_for(delay)

        driver.refresh()
        wait_for(delay)

        edit_button = driver.find_element(By.XPATH, '//button[contains(text(), "Edit response")]')
        edit_button.click()
        textarea = driver.find_element(By.XPATH, '//textarea[@placeholder="Write your response"]')
        textarea.send_keys(' edytowana recenzja')
        save_button = driver.find_element(By.XPATH, '//button[contains(text(), "Save")]')
        save_button.click()
        wait_for(delay)

        delete_button = driver.find_element(By.XPATH, '//button[contains(text(), "Delete")]')
        delete_button.click()
        wait_for(delay)
        yes_button = driver.find_element(By.XPATH, '//button[contains(text(), "Yes")]')
        yes_button.click()
        wait_for(delay)
        driver.refresh()
        #TODO recenzje z poziomu użytkownika

    except Exception as e:
        result(str(e), False)
        info("Menu Management Failed")
        info(f"Current URL: {driver.current_url}")
        info(f"Page title: {driver.title}")
        return False  # Test nieudany

    finally:
        wait_for(delay)


if __name__ == "__main__":
    driver = webdriver.Edge()
    driver.maximize_window()
    test_user_login(driver, False)
    test_menu_management(driver)
    driver.quit()
