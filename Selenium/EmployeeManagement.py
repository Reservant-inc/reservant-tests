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


        click_button(driver, By.ID, "NavbarRestaurantsSectionButton")
        wait_for(delay)

        click_button(driver, By.ID, "RestaurantSeeDetailsButton0John Doe's 2")
        wait_for(delay)

        click_button(driver, By.ID, "div.MuiButtonBase-root.MuiListItemButton-root.MuiListItemButton-gutters.MuiListItemButton-root.MuiListItemButton-gutters.bg-white.dark:bg-black.h-full.w-full.rounded-t-lg.px-4.dark:text-grey-1.css-1uwabd6")
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

        first_name = RandomData.generate_first_name()
        enter_text(driver, By.ID, "firstName", first_name)

        last_name = RandomData.generate_last_name()
        enter_text(driver, By.ID, "lastName", last_name)

        login = RandomData.generate_login()
        enter_text(driver, By.ID, "login", login)

        enter_text(driver, By.NAME, "phoneNumber", RandomData.generate_phone())

        enter_text(driver, By.ID, "birtDate", RandomData.generate_birth_date())

        password = RandomData.generate_password()

        enter_text(driver, By.ID, "password", password)

        enter_text(driver, By.ID, "confirmPassword", password)

        wait_for(delay)

        universal_wait_for(driver, EC.element_to_be_clickable, By.ID, "EmployeeRegisterSubmitButton")

        click_button(driver, By.ID, "EmployeeRegisterSubmitButton")


    #sprawdzenie przypisania (backdoor/hall)
        # czekamy na załadowanie tabelki
        wait_for(delay)

        # sprawdzam czy wyswietla sie pracownik


        # dla pracownika sprawdzam czy ,a w przynajmniej jednej kolumnie ("Hall" i "Backdoor") TICK icon

        #składnia: element = driver.find_element(By.CSS_SELECTOR, "[data-test-id='submit-button']")



    #edytowanie pracownika
        # czekamy na załadowanie tabelki
        wait_for(delay)

        # klikam przycisk "dlugopis" przy pracowniku, ktorego chce edytowac
        click_button(driver, By.ID, 'EmployeeManagementEditButtonJD+' + login)
        wait_for(delay)






    #usunięcie pracownika
        # czekamy na załadowanie tabelki
        wait_for(delay)

        # klikam przycisk "kosz" przy pracowniku, ktorego chce usunac
        click_button(driver, By.ID, 'EmployeeManagementDeleteButtonJD+' + login)
        wait_for(delay)

        #sprawdzam czy wyswietla sie pop up
        wait_for_element(driver, By.CSS_SELECTOR,
                         "div.MuiPaper-root.MuiPaper-elevation.MuiPaper-rounded.MuiPaper-elevation24.MuiDialog-paper.MuiDialog-paperScrollPaper.MuiDialog-paperWidthSm.css-uhb5lp", False)

        #potwierdzenie usuniecia
        click_button(driver, By.CSS_SELECTOR, "button.MuiButtonBase-root.MuiButton-root.MuiButton-text.MuiButton-textError.MuiButton-sizeMedium.MuiButton-textSizeMedium.MuiButton-colorError.MuiButton-root.MuiButton-text.MuiButton-textError.MuiButton-sizeMedium.MuiButton-textSizeMedium.MuiButton-colorError.css-51s2g2")

        #sprawdzam czy pracownik usunał się
        wait_for(delay)
        if driver.find_element(By.ID, 'EmployeeManagementDeleteButtonJD+' + login).is_displayed():
            return False

        #odswiezam strone
        driver.refresh()
        if driver.find_element(By.ID, 'EmployeeManagementDeleteButtonJD+' + login).is_displayed():
            return False



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
    test_user_login(driver, False)
    test_employee_management(driver)
    driver.quit()

