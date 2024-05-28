from utils.utils import *

ip = get_variable_value("IP_FRONTEND")
home_path = get_variable_value("HOME")
delay = int(get_variable_value("DELAY"))
home_url = f"http://{ip}{home_path}"


def test_user_groups(driver):
    info("Logging in user...")
    login(driver, "JD", "Pa$$w0rd")
    info("User logged in.")

    info("USER HOME TEST:\n")
    driver.get(home_url)

    try:
        # Sprawdzenie tytułu
        assert "React App" in driver.title, f"Oczekiwano tytułu zawierającego 'React App', otrzymano: {driver.title}"

        # Szukanie przycisku grup
        wait_for_element(driver, By.ID, "NavbarRestaurantsSectionButton")
        result("NavbarRestaurantsSectionButton found.")

        # Przechodzenie do groups
        click_button(driver, By.ID, "NavbarRestaurantsSectionButton")

        wait_for(delay)
        # TODO: implement groups testing

    except Exception as e:
        print("Could not load home webpage")


if __name__ == "__main__":
    driver = webdriver.Edge()
    test_user_groups(driver)
    driver.quit()
