from selenium.webdriver.support import wait

from Classes.RandomData import RandomData
from utils.utils import *
from Selenium.UserLogin import test_user_login

ip = get_variable_value("IP_FRONTEND")
login_path = get_variable_value("BOK_LOGIN_PATH")
register_path = get_variable_value("REGISTER_USER")
delay = int(get_variable_value("DELAY"))
# login_url = f"http://{ip}{login_path}"
# register_url = f"http://{ip}{register_path}"
home_path = get_variable_value("HOME_PATH")
home_url = f"http://{ip}{home_path}"


def test_reports_management(driver, diff_path=False):
    info("TEST BOK MANAGEMENT")
    try:
        driver.get(home_url)

        wait_for(delay)
        # LOGIN
        # Znalezienie i kliknięcie przycisku
        click_text_field(driver, By.ID, "login")

        press_tab_key(driver)

        # Sprawdzenie czy pojawia się nowa zawartość
        wait_for_element(driver, By.ID, "login-helper-text")

        # PASSWORD
        click_text_field(driver, By.ID, "password")

        press_tab_key(driver)

        wait_for_element(driver, By.ID, "password-helper-text")

        # Wybór losowego adresu email
        email = "manager@mail.com"
        enter_text(driver, By.ID, "login", email)

        enter_text(driver, By.ID, "password", "Pa$$w0rd")

        universal_wait_for(driver, EC.element_to_be_clickable, By.ID, "LoginLoginButton")

        click_button(driver, By.ID, "LoginLoginButton")

        wait_for(delay)

        column_header = driver.find_element(By.XPATH, "//div[@data-field='isResolved']")
        column_header.click()

        click_button(driver, By.CSS_SELECTOR, '[data-testid="ChevronRightIcon"]')

        button = driver.find_element(By.XPATH,
                                     "//button[@class='px-4 py-2 text-sm dark:bg-black border-[1px] rounded-md bg-white text-primary transition border-primary hover:scale-105 hover:bg-primary hover:text-white']")
        button.click()

        click_text_field(driver, By.XPATH, "//textarea[@name='comment']")
        enter_text(driver, By.XPATH, "//textarea[@name='comment']", "Sprawa zamknięta ")

        button = driver.find_element(By.XPATH,
                                     "//button[@class='border-[1px] rounded-md p-1 border-primary text-primary hover:bg-primary hover:text-white hover:scale-105 transition']")
        button.click()

        driver.refresh()
        wait_for(delay)
        column_header = driver.find_element(By.XPATH, "//div[@data-field='isResolved']")
        column_header.click()
        wait_for(delay)
        click_button(driver, By.CSS_SELECTOR, '[data-testid="ChevronRightIcon"]')

        go_to_profile_button = driver.find_element(By.XPATH, "//h1[contains(text(), 'Go to profile')]")
        go_to_profile_button.click()

        ban_user_button = driver.find_element(By.CSS_SELECTOR, "button.border-\\[1px\\].rounded-lg.p-1.text-primary")
        ban_user_button.click()
        wait_for(delay)
        ban_button = driver.find_element(By.CSS_SELECTOR, "button.text-sm.border-primary")
        ban_button.click()
        wait_for(delay)
        driver.refresh()

    except Exception as e:
        result(str(e), False)
        info("BOK Management Failed")
        info(f"Current URL: {driver.current_url}")
        info(f"Page title: {driver.title}")
        return False  # Test nieudany

    finally:
        wait_for(delay)


if __name__ == "__main__":
    driver = webdriver.Edge()
    driver.maximize_window()
    test_reports_management(driver)
    driver.quit()
