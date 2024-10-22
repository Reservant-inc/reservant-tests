from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from Selenium.UserRegister import test_user_register
from Selenium.UserLogin import test_user_login
from Selenium.EmployeeRegister import test_register_employee
from Selenium.RegisterRestaurant import test_register_restaurant
from Selenium.MenuManagement import test_menu_management
from Selenium.CheckRestaurant import test_check_restaurant


def main():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=chrome_options)
    test_user_register(driver)
    print()
    test_user_login(driver)
    print()
    test_user_login(driver, False)
    print()
    test_check_restaurant(driver)
    print()
    test_register_restaurant(driver, True)
    print()
    test_register_employee(driver)
    print()
    test_menu_management(driver)
    driver.quit()


if __name__ == "__main__":
    main()
