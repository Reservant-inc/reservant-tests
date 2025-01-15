from Classes.RandomData import RandomData
from utils.utils import *
from Selenium.UserLogin import test_user_login

ip = get_variable_value("IP_FRONTEND")
delay = int(get_variable_value("DELAY"))
home_path = get_variable_value("HOME_PATH")
home_url = f"http://{ip}{home_path}"

restaurants_management_path = get_variable_value("RESTAURANTS_MANAGEMENT")
restaurants_management_url = f"http://{ip}{restaurants_management_path}"

def deliveries_test(driver):
    info("DELIVERIES TEST")
    try:
        driver.get(home_url)
        wait_for_url_to_be(driver, home_url)

        # Sprawdzenie tytułu
        check_page_title(driver, "React App")

        # Sprawdzenie czy istnieje elemenet o id root, w naszym przypadku div
        wait_for_element(driver, By.ID, "root")

        click_button(driver, By.ID, "NavbarRestaurantsSectionButton")

        # przejscie do zarzadzania restauracjami
        driver.find_element(By.ID, "management_restaurants").click()

        # wybor restauracji
        wait_for(delay)
        click_button(driver, By.ID, "RestaurantSeeDetailsButton1John Doe's")

        # zakladka Deliveries
        driver.find_element(By.ID, "management_restaurant_deliveries").click()

        verify_unique_column_values(driver, 'div[data-field="deliveryId"]', False)
        # sprawdzamy ilosc wierszy - wszystkie dostawy (oczekiwane to 3, bo jeszcze naglowek)
        # zakladamy, ze zostaly utworzone 2 dostawy, jedna dostarczona
        rows_count = len(driver.find_elements(By.CSS_SELECTOR, 'div[data-field="deliveryId"]'))
        assert rows_count == 3, "Wrong rows count"

        #sprawdzamy ilosc niedostarczonych
        deliveries_kind_select = Select(driver.find_element(By.XPATH, "//select[@class='border-[1px] border-primary px-3 py-1 text-primary rounded-md hover:bg-primary hover:text-white dark:border-secondary dark:text-secondary dark:hover:bg-secondary dark:hover:text-black']"))
        deliveries_kind_select.select_by_value('delivered')
        rows_count = len(driver.find_elements(By.CSS_SELECTOR, 'div[data-field="deliveryId"]'))
        assert rows_count == 2, "Wrong rows count for delivered records"
        #sprawdzamy czy dostarczone mają wyłączone przyciski akcji
        button_action_enabled = driver.find_element(By.XPATH, "//button[@class='flex items-center justify-center rounded-md p-1 text-black dark:text-white']").is_enabled()
        assert button_action_enabled == False, "Button should be disabled"

        #sprawdzamy niedostarczone adekwatnie
        deliveries_kind_select.select_by_value("notDelivered")
        rows_count = len(driver.find_elements(By.CSS_SELECTOR, 'div[data-field="deliveryId"]'))
        assert rows_count == 2, "Wrong rows count for delivered records"
        button_approve = driver.find_element(By.XPATH, "//button[@class='flex items-center justify-center rounded-md p-1 text-green dark:text-green']")
        assert button_approve.is_enabled() == True, "Button should be enabled"
        #sprawdzamy czy po kliknieciu dostarczenia pojawia sie popup
        button_approve.click()
        wait_for(delay)
        driver.find_element(By.XPATH, '//button[text()="Confirm delivery"]')
        #zamkniecie popupu
        driver.find_element(By.XPATH, '//button[text()="Back"]').click()

        # sprawdzamy czy po kliknieciu informacji pojawia sie popup
        button_info = driver.find_element(By.XPATH, "//button[@class='flex items-center justify-center rounded-md p-1 text-primary dark:text-secondary']")
        button_info.click()
        wait_for(delay)
        # przez klikniecie back sprawdzamy czy popup sie pojawia
        driver.find_element(By.XPATH, '//button[text()="Back"]').click()

        # sprawdzamy czy po kliknieciu niedostarczenia pojawia sie popup
        button_reject = driver.find_element(By.XPATH, "//button[@class='flex items-center justify-center rounded-md p-1 text-red dark:text-red']")
        assert button_reject.is_enabled() == True, "Button to reject should be enabled"
        button_reject.click()
        wait_for(delay)
        driver.find_element(By.XPATH, '//button[text()="Cancel delivery"]')
        # zamkniecie popupu
        driver.find_element(By.XPATH, '//button[text()="Back"]').click()

        # sprawdzamy czy po kliknieciu informacji pojawia sie popup
        button_info = driver.find_element(By.XPATH,
                                            "//button[@class='flex items-center justify-center rounded-md p-1 text-primary dark:text-secondary']")
        button_info.click()
        wait_for(delay)
        #przez klikniecie back sprawdzamy czy popup sie pojawia
        driver.find_element(By.XPATH, '//button[text()="Back"]').click()


    except Exception as e:
        result(str(e), False)
        info("Deliveries test failed")
        info(f"Current URL: {driver.current_url}")
        info(f"Page title: {driver.title}")
        return False  # Test nieudany

    finally:
        wait_for(delay)

if __name__ == "__main__":
    driver = webdriver.Edge()
    driver.maximize_window()
    test_user_login(driver, False)
    deliveries_test(driver)
    driver.quit()
