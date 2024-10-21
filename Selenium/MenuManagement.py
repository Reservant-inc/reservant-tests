from Selenium.RegisterRestaurant import sample_data
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
    test_user_login(driver, False)
    info("Test check restaurant")
    try:
        check_page_title(driver, "React App")

        wait_for_element(driver, By.ID, "root")

        click_button(driver, By.ID, "NavbarRestaurantsSectionButton")
        wait_for(delay)

        click_button(driver, By.ID, "menu-listItem-menuManagement")
        wait_for(delay)

        click_button(driver, By.CSS_SELECTOR, '[data-testid="AddIcon"]')
        wait_for(delay)

        click_button(driver, By.ID, "addmenuSubmit")

        click_text_field(driver, By.ID, "name")
        enter_text(driver, By.ID, "name", sample_data.business_type)

        click_text_field(driver, By.ID, "alternateName")
        enter_text(driver, By.ID, "alternateName", sample_data.city)

        click_button(driver, By.ID, "menuType")
        click_button(driver, By.CSS_SELECTOR, '[value="Alcohol"]')

        click_text_field(driver, By.ID, "dateFrom")
        enter_text(driver, By.ID, "dateFrom", "12122000")

        click_text_field(driver, By.ID, "dateUntil")
        enter_text(driver, By.ID, "dateUntil", "11112011")

        wait_for(delay)

        universal_wait_for(driver, EC.element_to_be_clickable, By.ID, "addmenuSubmit")
        click_button(driver, By.ID, "addmenuSubmit")
        wait_for(delay)
        wait_for(delay)

    except Exception as e:
        result(str(e), False)
        info("Menu Management Failed")
        info(f"Current URL: {driver.current_url}")
        info(f"Page title: {driver.title}")
        return False  # Test nieudany

    finally:
        wait_for(delay)


if __name__ == "__main__":
    driver = webdriver.Edge()
    test_check_restaurant(driver)
    driver.quit()
