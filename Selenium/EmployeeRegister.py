from Classes.EmployeeRegistrationData import EmployeeRegistrationData
from utils.utils import *
from Selenium.UserLogin import test_user_login

ip = get_variable_value("IP_FRONTEND")
delay = int(get_variable_value("DELAY"))
home_path = get_variable_value("HOME_PATH")
home_url = f"http://{ip}{home_path}"

# employee_management_path = get_variable_value("EMPLOYEE_MANAGEMENT")
# employee_management_url = f"http://{ip}{employee_management_path}"
restaurants_management_path = get_variable_value("RESTAURANTS_MANAGEMENT")
restaurants_management_url = f"http://{ip}{restaurants_management_path}"
sample_data = EmployeeRegistrationData.generate_employee_data()

def test_register_employee(driver):
    test_user_login(driver, False)

    info("EMPLOYEE REGISTER TEST")
    try:
        # Sprawdzenie tytułu
        check_page_title(driver, "React App")

        # Sprawdzenie czy istnieje elemenet o id root, w naszym przypadku div
        wait_for_element(driver, By.ID, "root")

        #EMPLOYEE REGISTER
        # Znalezienie i kliknięcie przycisku
        click_button(driver, By.ID, "NavbarRestaurantsSectionButton")

        # Czekamy na zmianę strony
        wait_for_url_to_be(driver, restaurants_management_url)
        click_button(driver, By.ID, "menu-listItem-employees-button")

        # czekamy na załadowanie tabelki
        # to do

        # przechodzimy do fromularza rejestracji pracownika
        # czy dla tego id nie powinna byc zmieniona nazwa?
        click_button(driver, By.ID, "RestaurantListAddRestaurantButton")

        # Sprawdzenie czy pojawia się nowa zawartość

        #firstname
        click_text_field(driver, By.ID, "firstName")

        press_tab_key(driver)

        wait_for_element(driver, By.ID, "errorMes-wrap")
        #czy sa id dla error message bo narazie dla wszystkich widze: "errorMessage-wrap"

        #lastname
        click_text_field(driver, By.ID, "lastName")

        press_tab_key(driver)

        wait_for_element(driver, By.ID, "errorMes-wrap")

        #login

        click_text_field(driver, By.ID, "login")

        press_tab_key(driver)

        wait_for_element(driver, By.ID, "errorMes-wrap")

        #phone
        #nie ma ID
        click_text_field(driver, By.NAME, "phoneNumber")

        press_tab_key(driver)

        wait_for_element(driver, By.ID, "errorMes-wrap")

        #password

        click_text_field(driver, By.ID, "password")

        press_tab_key(driver)

        wait_for_element(driver, By.ID, "errorMes-wrap")

        #password_confirmation
        click_text_field(driver, By.ID, "confirmPassword")

        press_tab_key(driver)

        wait_for_element(driver, By.ID, "errorMes-wrap")


        # Znaleznienie pola i wypełnienie go danymi

        #selector value to ID?
        enter_text(driver, By.ID, "firstName", sample_data.first_name)

        enter_text(driver, By.ID, "lastName", sample_data.last_name)

        enter_text(driver, By.ID, "login", sample_data.login)

        enter_text(driver, By.NAME, "phoneNumber", sample_data.phone)

        enter_text(driver, By.ID, "password", sample_data.password)

        enter_text(driver, By.ID, "confirmPassword", sample_data.password_confirmation)

        wait_for(delay)

        universal_wait_for(driver, EC.element_to_be_clickable, By.ID, "EmployeeRegisterSubmitButton")

        click_button(driver, By.ID, "EmployeeRegisterSubmitButton")

        # TODO sprawdzic czy test przeszedł
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
    test_register_employee(driver)
    driver.quit()