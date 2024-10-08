from Classes.RestaurantRegistrationData import RestaurantRegistrationData
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

def test_check_restaurant(driver):
    test_user_login(driver,False)
    info("Test check restaurant")
    try:
        check_page_title(driver, "React App")

        wait_for_element(driver, By.ID, "root")

        click_button(driver, By.ID, "homePage-listItemButton")

        wait_for(delay)

        wait_for_element(driver, By.ID, "after-image-slider-controls")

    except Exception as e:
        result(str(e), False)
        info("Restaurant check failed")
        info(f"Current URL: {driver.current_url}")
        info(f"Page title: {driver.title}")
        return False  # Test nieudany

    finally:
        wait_for(delay)

if __name__ == "__main__":
    driver = webdriver.Edge()
    test_check_restaurant(driver)
    driver.quit()