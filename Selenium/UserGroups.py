from utils.utils import *

ip = get_variable_value("IP_FRONTEND")
home_path = get_variable_value("HOME")
delay = int(get_variable_value("DELAY"))
home_url = f"http://{ip}{home_path}"


def test_user_groups(driver):

    login(driver, "JD", "Pa$$w0rd")

    info("USER HOME TEST")
    driver.get(home_url)

    try:
        # Sprawdzenie tytułu
        assert "React App" in driver.title, f"Oczekiwano tytułu zawierającego 'React App', otrzymano: {driver.title}"

    except Exception as e:
        print("Could not load home webpage")


if __name__ == "__main__":
    driver = webdriver.Edge()
    test_user_groups(driver)
    time.sleep(delay)
    driver.quit()
