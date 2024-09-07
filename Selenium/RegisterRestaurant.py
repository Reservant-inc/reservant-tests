from Classes.RestaurantRegistrationData import RestaurantRegistrationData
from utils.utils import *
from Selenium.UserLogin import test_user_login

ip = get_variable_value("IP_FRONTEND")
delay = int(get_variable_value("DELAY"))
home_path = get_variable_value("HOME_PATH")
home_url = f"http://{ip}{home_path}"
restaurants_management_path = get_variable_value("RESTAURANTS_MANAGEMENT")
restaurants_management_url = f"http://{ip}{restaurants_management_path}"
sample_data = RestaurantRegistrationData.generate_restaurant_data()


def test_register_restaurant(driver):
    test_user_login(driver, False)

    info("USER REGISTER TEST")
    try:
        # Sprawdzenie tytułu
        check_page_title(driver, "React App")

        # Sprawdzenie czy istnieje elemenet o id root, w naszym przypadku div
        wait_for_element(driver, By.ID, "root")

        # REGISTER RESTAURANT
        # Znalezienie i kliknięcie przycisku
        click_button(driver, By.ID, "NavbarRestaurantsSectionButton")

        # Czekamy na zmianę strony
        wait_for_url_to_be(driver, restaurants_management_url)

        click_button(driver, By.ID, "menu-listItem-restaurants-button")

        # czekamy na załadowanie tabelki
        # TODO zmienic z XPath na coś innego
        wait_for_element(driver, By.XPATH,
                         "/html/body/div/div/div/div/div[2]/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[2]",
                         False)

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

        enter_text(driver, By.ID, "name", sample_data.name)

        enter_text(driver, By.ID, "address", sample_data.address)

        enter_text(driver, By.ID, "postalIndex", sample_data.postal_code)

        enter_text(driver, By.ID, "city", sample_data.city)

        enter_text(driver, By.ID, "nip", sample_data.nip)

        select_option_by_visible_text(driver, By.ID, "restaurantType", sample_data.business_type)

        upload_file(driver, By.ID, "idCard", "../Files/test.pdf")

        upload_file(driver, By.ID, "businessPermission", "../Files/test.pdf")

        upload_file(driver, By.ID, "rentalContract", "../Files/test.pdf")

        upload_file(driver, By.ID, "alcoholLicense", "../Files/test.pdf")

        wait_for(delay)

        universal_wait_for(driver, EC.element_to_be_clickable, By.ID, "RestaurantRegisterNextButton")

        click_button(driver, By.ID, "RestaurantRegisterNextButton")

        select_random_tags(driver, By.ID, "restaurantRegister-wrapper-tags", 3)

        check_checkbox(driver, selector_type=By.ID, selector_value='provideDelivery')

        upload_file(driver, By.ID, "logo", "../Files/test.png")

        upload_file(driver, By.ID, "photos", "../Files/test.png")

        enter_text(driver, By.ID, "description", sample_data.description)

        click_button(driver, By.ID, "RestaurantRegisterNextButton")

        # wait_for_element() #TODO nie wiem jeszcze jak sprawdzic czy test przeszedł bo nie działa we froncie

        return True  # Test przeszedł

    except Exception as e:
        result(str(e), False)
        info("Register restaurant test failed")
        info(f"Current URL: {driver.current_url}")
        info(f"Page title: {driver.title}")
        print("-----------------------")
        info("Problem with following login data:")
        info(sample_data)
        return False  # Test nieudany


    finally:
        wait_for(delay)


if __name__ == "__main__":
    driver = webdriver.Edge()
    test_register_restaurant(driver)
    driver.quit()
