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

        # Wypełnienie formularza składnika
        ingredient_name = RandomData.generate_word()
        enter_text(driver, By.NAME, "name", ingredient_name)
        unit = RandomData.generate_unit_of_measurement()
        select_option_by_visible_text(driver, By.NAME, "unitOfMeasurement", unit)

        # Wprowadzenie wartości ilościowych
        enter_text(driver, By.NAME, "minimalAmount", RandomData.generate_number())
        enter_text(driver, By.NAME, "amount", RandomData.generate_number())

        # Dodanie składnika
        click_button(driver, By.ID, "SubmitAddIngredientDialog")
        wait_for(delay)

        # FIXME mimo poprawnego wyslania na backend, dodany skladnik nie wyswietla się
        # Weryfikacja dodania składnika
        find_text_in_elements(driver, By.NAME, "name", ingredient_name)

        # Modyfikacja składnika
        edit_button_id = f'IngredientEditButton{ingredient_name}'
        click_button(driver, By.ID, edit_button_id)
        wait_for_element(driver, By.ID, "ingredientEditDialog")

        new_ingredient_name = ingredient_name + "_updated"
        enter_text(driver, By.NAME, "name", new_ingredient_name)

        # Zapisanie zmian
        click_button(driver, By.ID, "IngredientSaveButton")
        wait_for(delay)

        # Weryfikacja modyfikacji
        find_text_in_elements(driver, By.CSS_SELECTOR, 'div[data-field="name"]', new_ingredient_name)

        # Usunięcie składnika
        delete_button_id = f'IngredientDeleteButton{new_ingredient_name}'
        click_button(driver, By.ID, delete_button_id)
        click_button(driver, By.ID, "ConfirmDeletionButton")
        wait_for(delay)

        # Weryfikacja usunięcia
        try:
            find_text_in_elements(driver, By.CSS_SELECTOR, 'div[data-field="name"]', new_ingredient_name)
            raise Exception("Składnik nie został usunięty.")
        except NoSuchElementException:
            pass  # Składnik został pomyślnie usunięty

        return True  # Test przeszedł pomyślnie

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
