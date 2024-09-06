from utils.utils import *
from Selenium.UserLogin import test_user_login

ip = get_variable_value("IP_FRONTEND")
delay = int(get_variable_value("DELAY"))
home_path = get_variable_value("HOME_PATH")
home_url = f"http://{ip}{home_path}"
restaurants_management_path = get_variable_value("RESTAURANTS_MANAGEMENT")
restaurants_management_url = f"http://{ip}{restaurants_management_path}"


def test_register_restaurant(driver):
    test_user_login(driver, False)

    info("USER REGISTER TEST")
    try:
        # Sprawdzenie tytułu
        check_page_title(driver, "React App")

        # Sprawdzenie czy istnieje elemenet o id root, w naszym przypadku div
        wait_for_element(driver, By.ID, "root")

        #REGISTER RESTAURANT
        # Znalezienie i kliknięcie przycisku
        click_button(driver, By.ID, "NavbarRestaurantsSectionButton")

        # Czekamy na zmianę strony
        wait_for_url_to_be(driver, restaurants_management_url)

        click_button(driver, By.ID, "menu-listItem-restaurants-button")

        #czekamy na załadowanie tabelki
        #TODO zmienic z XPath na coś innego
        wait_for_element(driver, By.XPATH, "/html/body/div/div/div/div/div[2]/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[2]", False)

        # sprawdzamy czy id restauracji są unikalne(nie ma powtórzeń)
        verify_unique_column_values(driver, 'div[data-field="restaurantId"]', False)

        #przechodzimy do fromularza rejestracji restauracji
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

        enter_text(driver, By.ID, "name", sample_login.login)

        # enter_text(driver, By.ID, "email", sample_login.email)
        #
        # enter_text(driver, By.ID, "password", sample_login.password)
        #
        # enter_text(driver, By.ID, "confirmPassword", sample_login.password)
        # result("Form filled correctly")
        #
        # wait_for(delay)
        #
        # # Czekamy na pojawienie się przycisku
        # universal_wait_for(driver, EC.element_to_be_clickable, By.CSS_SELECTOR, "button")
        # result("NEXT button is clickable.")
        #
        # click_button(driver, By.CSS_SELECTOR, "button")
        # result("Successfully clicked NEXT button")
        #
        # universal_wait_for(driver, EC.element_to_be_clickable, By.ID, "firstName")
        #
        # # FIRST NAME
        # click_text_field(driver, By.ID, "firstName")
        # result("Successfully clicked the first name text field")
        #
        # press_tab_key(driver)
        #
        # wait_for_element(driver, By.ID, "firstName-helper-text")
        # result("First name error is displayed.")
        #
        # # LAST NAME
        # click_text_field(driver, By.ID, "lastName")
        # result("Successfully clicked the last name text field")
        #
        # press_tab_key(driver)
        #
        # wait_for_element(driver, By.ID, "lastName-helper-text")
        # result("Last name error is displayed.")
        #
        # # PHONE
        # click_text_field(driver, By.ID, "userRegister-phoneNumber-field")
        # result("Successfully clicked the phone text field")
        #
        # press_tab_key(driver)
        #
        # wait_for_element(driver, By.ID, "userRegister-phoneNumber-field")
        # result("Phone error is displayed.")
        #
        # # DATE
        # click_text_field(driver, By.ID, "birthDate")
        # result("Successfully clicked the birth date text field")
        #
        # press_tab_key(driver)
        #
        # wait_for_element(driver, By.ID, "userRegister-phoneNumber-field")
        # result("Birth date error is displayed.")
        #
        # enter_text(driver, By.ID, "firstName", sample_login.first_name)
        #
        # enter_text(driver, By.ID, "lastName", sample_login.last_name)
        #
        # enter_text(driver, By.ID, "userRegister-phoneNumber-field", sample_login.phone_number)
        #
        # enter_text(driver, By.ID, "birthDate", sample_login.birth_day)
        #
        # # Czekamy na pojawienie się przycisku
        # #TODO id
        # universal_wait_for(driver, EC.element_to_be_clickable, By.CSS_SELECTOR, "button.pointer:nth-child(2)")
        # result("SUBMIT button is clickable.")
        #
        # click_button(driver, By.CSS_SELECTOR, "button.pointer:nth-child(2)")
        # result("Successfully clicked SUBMIT button")
        #
        # # Czekamy na zmianę strony
        # universal_wait_for(driver, EC.url_changes, different_value=register_url)
        # result("URL has changed successfully")
        #
        # # Sprawdzenie czy strona zmieniła się na taką jaką chcemy w naszym przypadku login
        # assert driver.current_url == login_url, f"URL did not change to expected. Current URL: {driver.current_url}"
        # result("Form submitted successfully and result is correct.")

        return True  # Test przeszedł

    except Exception as e:
        result(str(e), False)
        info("Register restaurant test failed")
        info(f"Current URL: {driver.current_url}")
        info(f"Page title: {driver.title}")
        print("-----------------------")
        # info("Problem with following login data:")
        # info(sample_login)
        return False  # Test nieudany


    finally:
        wait_for(delay)


if __name__ == "__main__":
    driver = webdriver.Edge()
    test_register_restaurant(driver)
    driver.quit()