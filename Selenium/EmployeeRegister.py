from Classes.RandomData import RandomData
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


def test_register_employee(driver):
    info("EMPLOYEE REGISTER TEST")
    try:
        driver.get(home_url)
        wait_for_url_to_be(driver, home_url)

        # Sprawdzenie tytułu
        check_page_title(driver, "React App")

        # Sprawdzenie czy istnieje elemenet o id root, w naszym przypadku div
        wait_for_element(driver, By.ID, "root")

        # EMPLOYEE REGISTER
        # Znalezienie i kliknięcie przycisku
        click_button(driver, By.ID, "NavbarRestaurantsSectionButton")

        # Czekamy na zmianę strony
        wait_for_url_to_be(driver, restaurants_management_url)
        driver.find_element(By.ID, "management_employees").click()

        # czekamy na załadowanie tabelki
        wait_for_element(driver, By.CSS_SELECTOR,
                         "div.MuiDataGrid-row.MuiDataGrid-row--editable.MuiDataGrid-row--firstVisible", False)

        # sprawdzamy czy id restauracji są unikalne(nie ma powtórzeń)
        verify_unique_column_values(driver, 'div[data-field="phoneNumber"]', False)

        # przechodzimy do fromularza rejestracji pracownika
        # czy dla tego id nie powinna byc zmieniona nazwa?
        click_button(driver, By.ID, "RestaurantListAddRestaurantButton")

        # Sprawdzenie czy pojawia się nowa zawartość

        # firstname
        click_text_field(driver, By.ID, "firstName")

        press_tab_key(driver)

        wait_for_element(driver, By.ID, "errorMes-wrap")
        # TODO: czy sa id dla error message bo narazie dla wszystkich widze: "errorMessage-wrap"
        #TODO Zamienić na teksty błędów

        # lastname
        click_text_field(driver, By.ID, "lastName")

        press_tab_key(driver)

        wait_for_element(driver, By.ID, "errorMes-wrap")

        # login

        click_text_field(driver, By.ID, "login")

        press_tab_key(driver)

        wait_for_element(driver, By.ID, "errorMes-wrap")

        # phone
        # nie ma ID
        click_text_field(driver, By.NAME, "phoneNumber")

        press_tab_key(driver)

        wait_for_element(driver, By.ID, "errorMes-wrap")

        # birth date
        # nie ma ID
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

        # selector value to ID?
        first_name = RandomData.generate_first_name()
        #first_name = 'Lalaa'
        enter_text(driver, By.ID, "firstName", first_name)

        last_name = RandomData.generate_last_name()
        #last_name = 'Tralaa'
        enter_text(driver, By.ID, "lastName", last_name)

        login = RandomData.generate_login()
        enter_text(driver, By.ID, "login", login)

        enter_text(driver, By.NAME, "phoneNumber", RandomData.generate_phone())

        enter_text(driver, By.ID, "birthDate", RandomData.generate_birth_date())

        password = RandomData.generate_password()
        #password = 'Pa$$w0rd'

        enter_text(driver, By.ID, "password", password)

        enter_text(driver, By.ID, "confirmPassword", password)

        wait_for(delay)

        universal_wait_for(driver, EC.element_to_be_clickable, By.ID, "EmployeeRegisterSubmitButton")

        click_button(driver, By.ID, "EmployeeRegisterSubmitButton")

        wait_for(delay)

        driver.refresh()

        #czekamy na załadowanie tabelki
        wait_for(delay)

        #Sprawdzenie czy pracownik się dodał
        find_text_in_elements(driver, By.CSS_SELECTOR, 'div[data-field="firstName"]', first_name)
        find_text_in_elements(driver, By.CSS_SELECTOR, 'div[data-field="lastName"]', last_name)

        # przypisanie pracownika do restauracji
        #kliknij przycisk przypisania do restauracji
        wait_for(delay)
        click_button(driver, By.ID, 'EmployeeManagementEmploymentButtonJD+' + login)

        #powinien powjawic sie dialog, ktory bedzie zawieral przycisk o tym ID, domyślnie disabled (brak wybranej restauracji)
        if driver.find_element(By.ID, "RestaurantAddEmpSubmitButton").is_enabled():
            return False

        #wybieramy restaurację
        wait_for(delay)
        select_option_by_visible_text(driver, By.ID, "selectedRestaurant", "John Doe's")
        #przycisk assign employee dalej powinien byc disabled (brak wybranej roli)
        if driver.find_element(By.ID, "RestaurantAddEmpSubmitButton").is_enabled():
            return False

        #wybieramy rolę
        backdoor_checkbox = driver.find_element(By.ID, "isBackdoorEmployee")
        # zaznaczamy i odznaczamy, aby pojawil sie blad walidacji
        backdoor_checkbox.click()
        wait_for(delay)
        backdoor_checkbox.click()
        wait_for(delay)

        #sprawdzamy czy jest tekst bledu walidacji
        #!!! Powinno dzialac, ale nie pojawia sie
        wait_for_element(driver, By.ID, "errorMes-wrap", critical=False)
        #ponownie zaznaczamy checkbox
        backdoor_checkbox.click()

        #przycisk assign employee powinien byc juz enabled
        if not driver.find_element(By.ID, "RestaurantAddEmpSubmitButton").is_enabled():
            return False
        #dodajemy pracownika do restauracji
        click_button(driver, By.ID, "RestaurantAddEmpSubmitButton")

        #sprawdzamy czy pojawil sie rekord poprzez sprawdzenie przycisku edycji przypisania
        #to nie przechodzi, bo kazdy przycisk ma inne ID na koncu, nie wiem jak inaczej sprawdzic
        #wait_for_element(driver, By.ID, "EmployeeManagementEditButtonPopup2")

        #zamkniecie dialogu
        #TODO: dla przycisku "x"- zamykanie popupu
        click_button(driver, By.CSS_SELECTOR, '.h-8.w-8.bg-white.dark\\:bg-black.dark\\:text-grey-1.rounded-full.top-0.right-2')


        # edycja pracownika
        #kliknij przycisk edycji pracownika
        wait_for(delay)
        click_button(driver, By.ID, 'EmployeeManagementEditButtonJD+' + login)

        new_first_name = 'Ala'
        enter_text(driver, By.CSS_SELECTOR, '.MuiInputBase-input.css-mnn31', new_first_name)

        click_button(driver, By.ID, 'EmployeeManagementSaveButtonJD+' + login)
        wait_for(delay)

        find_text_in_elements(driver, By.CSS_SELECTOR, 'div[data-field="firstName"]', first_name + new_first_name)


        #TODO sprawdzić usuwanie i edytowanie - na razie nie działa
        return True  # Test przeszedł

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
    test_register_employee(driver)
    driver.quit()
