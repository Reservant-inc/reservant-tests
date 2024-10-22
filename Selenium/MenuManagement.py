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

        click_button(driver, By.ID, "menu-listItem-menuManagement")
        wait_for(delay)

        click_button(driver, By.CSS_SELECTOR, '[data-testid="AddIcon"]')
        wait_for(delay)

        click_button(driver, By.ID, "addmenuSubmit")

        name = RandomData.generate_name()
        click_text_field(driver, By.ID, "name")
        enter_text(driver, By.ID, "name", name)

        click_text_field(driver, By.ID, "alternateName")
        enter_text(driver, By.ID, "alternateName", RandomData.generate_name())

        click_button(driver, By.ID, "menuType")
        click_button(driver, By.CSS_SELECTOR, f'[value="{RandomData.generate_menu_type()}"]')

        click_text_field(driver, By.ID, "dateFrom")
        enter_text(driver, By.ID, "dateFrom", RandomData.generate_menu_date_from())

        click_text_field(driver, By.ID, "dateUntil")
        enter_text(driver, By.ID, "dateUntil", RandomData.generate_menu_date_until())

        wait_for(delay)
        click_button(driver, By.ID, "addmenuSubmit")
        wait_for(delay)

        # MODYFIKOWANIE MENU

        element = find_text_in_elements(driver, By.CSS_SELECTOR, "div.w-full.flex.justify-between.pr-3", name)

        elements = element.find_elements(By.CSS_SELECTOR, "button")
        elements[0].click()


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
    test_user_login(driver, False)
    test_menu_management(driver)
    driver.quit()
