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
    info("TEST CHECK RESTAURANTS")
    try:
        driver.get(home_url)
        wait_for_url_to_be(driver, home_url)

        check_page_title(driver, "React App")

        wait_for_element(driver, By.ID, "root")

        elements = get_elements_list(driver, By.CSS_SELECTOR, '[id="homePage-listItemButton"]')

        for element in elements:
            element.click()
            wait_for_element(driver, By.ID, "after-image-slider-controls")
            wait_for(delay)

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
    test_user_login(driver, False)
    test_check_restaurant(driver)
    driver.quit()
