from Classes.RandomData import RandomData
from utils.utils import *
from Selenium.UserLogin import test_user_login

ip = get_variable_value("IP_FRONTEND")
delay = int(get_variable_value("DELAY"))
home_path = get_variable_value("HOME_PATH")
home_url = f"http://{ip}{home_path}"


def test_warehouse_management(driver):
    info("TEST WAREHOUSE MANAGEMENT")
    try:
        driver.get(home_url)
        wait_for_url_to_be(driver, home_url)
        check_page_title(driver, "React App")

        wait_for_element(driver, By.ID, "root")

        go_to_restaurant_management(driver)

        click_button(driver, By.ID, "management_restaurant_warehouse")
        wait_for(delay)

        # button nazywa sie RestaurantListAddRestaurantButton, ale dodaje składniki
        click_button(driver, By.ID, "RestaurantListAddRestaurantButton")
        wait_for(delay)

        enter_text(driver, By.NAME, "name", RandomData.generate_word())
        select_option_by_visible_text(driver, By.NAME, "unitOfMeasurement", RandomData.generate_unit_of_measurement())

        # TODO dodać wprowadzenie wartości do pól z ilościami, po tym jak zostaną im nadane unikatowe nazwy/id

        # TODO dodać click_button dla przycisku do dodawania składnika

        # TODO dodać zmodyfikowanie/usunięcie składnika

        # TODO dodać wypełnienie formularza do listy zakupów

        return True

    except Exception as e:
        result(str(e), False)
        info("Employee management test failed")
        info(f"Current URL: {driver.current_url}")
        info(f"Page title: {driver.title}")
        return False

    finally:
        wait_for(delay)


if __name__ == "__main__":
    driver = webdriver.Edge()
    driver.maximize_window()
    test_user_login(driver, False)
    test_warehouse_management(driver)
    driver.quit()
