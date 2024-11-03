from Classes.RandomData import RandomData
from utils.utils import *
from Selenium.UserLogin import test_user_login

ip = get_variable_value("IP_FRONTEND")
delay = int(get_variable_value("DELAY"))
home_path = get_variable_value("HOME_PATH")
home_url = f"http://{ip}{home_path}"
restaurants_management_path = get_variable_value("RESTAURANTS_MANAGEMENT")
restaurants_management_url = f"http://{ip}{restaurants_management_path}"


def test_register_restaurant(driver, diff_path=False):
    info("RESTAURANT REGISTER TEST")
    try:
        driver.get(home_url)
        wait_for_url_to_be(driver, home_url)

        # Sprawdzenie tytułu
        check_page_title(driver, "React App")

        # Sprawdzenie czy istnieje elemenet o id root, w naszym przypadku div
        wait_for_element(driver, By.ID, "root")

        # REGISTER RESTAURANT
        # Znalezienie i kliknięcie przycisku
        click_button(driver, By.ID, "NavbarRestaurantsSectionButton")

        # Czekamy na zmianę strony
        wait_for_url_to_be(driver, restaurants_management_url)

        find_text_in_elements(driver, By.CSS_SELECTOR, "div.flex.items-center.gap-4", "Restaurants").click()

        # czekamy na załadowanie tabelki
        wait_for_element(driver, By.CSS_SELECTOR,
                         "div.MuiDataGrid-row.MuiDataGrid-row--editable.MuiDataGrid-row--firstVisible", False)

        # sprawdzamy czy id restauracji są unikalne(nie ma powtórzeń)
        verify_unique_column_values(driver, 'div[data-field="restaurantId"]', False)

        # przechodzimy do fromularza rejestracji restauracji
        click_button(driver, By.ID, "RestaurantListAddRestaurantButton")

        # Sprawdzenie czy pojawia się nowa zawartość
        # Name
        click_text_field(driver, By.ID, "name")

        press_tab_key(driver)

        wait_for_element(driver, By.ID, "restaruantRegister-errorMessage-name")

        # address
        click_text_field(driver, By.ID, "address")

        press_tab_key(driver)

        wait_for_element(driver, By.ID, "restaruantRegister-errorMessage-address")

        # postalIndex
        click_text_field(driver, By.ID, "postalIndex")

        press_tab_key(driver)

        wait_for_element(driver, By.ID, "restaruantRegister-errorMessage-postalIndex")

        # city
        click_text_field(driver, By.ID, "city")

        press_tab_key(driver)

        wait_for_element(driver, By.ID, "restaruantRegister-errorMessage-city")

        # nip
        click_text_field(driver, By.ID, "nip")

        press_tab_key(driver)

        wait_for_element(driver, By.ID, "restaruantRegister-errorMessage-nip")

        wait_for(delay)

        # Znaleznienie pola i wypełnienie go danymi

        enter_text(driver, By.ID, "name", RandomData.generate_first_name())

        enter_text(driver, By.ID, "address", RandomData.generate_address())

        enter_text(driver, By.ID, "postalIndex", RandomData.generate_postal_code())

        enter_text(driver, By.ID, "city", RandomData.generate_city())

        enter_text(driver, By.ID, "nip", RandomData.generate_nip())

        select_option_by_visible_text(driver, By.ID, "restaurantType", RandomData.generate_business_type())

        if(diff_path):
            pdf = "Files/test.pdf"
            png = "Files/test.png"
        else:
            pdf = "../Files/test.pdf"
            png = "../Files/test.png"

        upload_file(driver, By.ID, "idCard", pdf)

        upload_file(driver, By.ID, "businessPermission", pdf)

        upload_file(driver, By.ID, "rentalContract", pdf)

        upload_file(driver, By.ID, "alcoholLicense", pdf)

        wait_for(delay)

        universal_wait_for(driver, EC.element_to_be_clickable, By.ID, "RestaurantRegisterNextButton")

        click_button(driver, By.ID, "RestaurantRegisterNextButton")

        select_random_tags(driver, By.ID, "restaurantRegister-wrapper-tags", 3)

        check_checkbox(driver, selector_type=By.ID, selector_value='provideDelivery')

        upload_file(driver, By.ID, "logo", png)

        upload_file(driver, By.ID, "photos", png)

        enter_text(driver, By.ID, "description", RandomData.generate_description())

        click_button(driver, By.ID, "RestaurantRegisterNextButton")

        # wait_for_element() #TODO nie wiem jeszcze jak sprawdzic czy test przeszedł bo nie działa we froncie

        return True  # Test przeszedł

    except Exception as e:
        result(str(e), False)
        info("Register restaurant test failed")
        info(f"Current URL: {driver.current_url}")
        info(f"Page title: {driver.title}")
        return False  # Test nieudany

    finally:
        wait_for(delay)


if __name__ == "__main__":
    driver = webdriver.Edge()
    test_user_login(driver, False)
    test_register_restaurant(driver)
    driver.quit()
