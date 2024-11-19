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


def test_employee_management(driver):
    info("TEST EMPLOYEE MANAGEMENT")
    try:
        driver.get(home_url)
        wait_for_url_to_be(driver, home_url)

        check_page_title(driver, "React App")

        wait_for_element(driver, By.ID, "root")

        go_to_restaurant_management(driver)

        click_button(driver, By.ID, "management_restaurant_employees")
        wait_for(delay)

        #czekamy na załadowanie tabelki
        wait_for_element(driver, By.CSS_SELECTOR,
                         "div.MuiDataGrid-virtualScrollerContent.css-1xdhyk6", False)

        # sprawdzamy czy id pracownikow są unikalne(nie ma powtórzeń)
        verify_unique_column_values(driver, 'div[data-field="login"]', False)

        # TWORZENIE PRACOWNIKA
        click_button(driver, By.ID, "RestaurantListAddRestaurantButton")

        # Sprawdzenie czy pojawia się nowa zawartość

        # firstname
        click_text_field(driver, By.ID, "firstName")

        press_tab_key(driver)

        wait_for_element(driver, By.ID, "errorMes-wrap")

        # lastname
        click_text_field(driver, By.ID, "lastName")

        press_tab_key(driver)

        wait_for_element(driver, By.ID, "errorMes-wrap")

        # login

        click_text_field(driver, By.ID, "login")

        press_tab_key(driver)

        wait_for_element(driver, By.ID, "errorMes-wrap")

        # phone
        click_text_field(driver, By.NAME, "phoneNumber")

        press_tab_key(driver)

        wait_for_element(driver, By.ID, "errorMes-wrap")

        #birthdate
        click_text_field(driver, By.ID, "birthDate")

        press_tab_key(driver)

        wait_for_element(driver, By.ID, "errorMes-wrap")

        # password

        click_text_field(driver, By.ID, "password")

        press_tab_key(driver)

        wait_for_element(driver, By.ID, "errorMes-wrap")

        # password_confirmation
        click_text_field(driver, By.ID, "confirmPassword")

        press_tab_key(driver)

        wait_for_element(driver, By.ID, "errorMes-wrap")

        # Znaleznienie pola i wypełnienie go danymi

        enter_text(driver, By.ID, "firstName", RandomData.generate_first_name())

        enter_text(driver, By.ID, "lastName", RandomData.generate_last_name())

        enter_text(driver, By.ID, "login", RandomData.generate_login())

        enter_text(driver, By.NAME, "phoneNumber", RandomData.generate_phone())

        enter_text(driver, By.ID, "birtDate", RandomData.generate_birth_date())

        password = RandomData.generate_password()

        enter_text(driver, By.ID, "password", password)

        enter_text(driver, By.ID, "confirmPassword", password)

        wait_for(delay)

        universal_wait_for(driver, EC.element_to_be_clickable, By.ID, "EmployeeRegisterSubmitButton")

        click_button(driver, By.ID, "EmployeeRegisterSubmitButton")


    #sprawdzenie przypisania (backdoor/hall)
        #TO DO

    #edytowanie pracownika
        #TO DO
        #nie działa edycja pracownika- issue zgłoszone

    #usunięcie pracownika
        # czekamy na załadowanie tabelki
        wait_for_element(driver, By.CSS_SELECTOR,
                         "div.MuiDataGrid-virtualScrollerContent.css-1xdhyk6", False)

        click_button(driver, By.ID, "EmployeeManagementDeleteButtonJD+employee")
        wait_for(delay)

        #sprawdzenie czy pracownik usunął się
        #TO DO
        #? po czym sprawdzić jak nie mamy id


    except Exception as e:
        result(str(e), False)
        info("Employee management test failed")
        info(f"Current URL: {driver.current_url}")
        info(f"Page title: {driver.title}")
        return False  # Test nieudany

    finally:
        wait_for(delay)


if __name__ == "__main__":
    driver = webdriver.Edge()
    driver.maximize_window()
    test_user_login(driver, False)
    test_employee_management(driver)
    driver.quit()

