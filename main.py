from selenium import webdriver
from Selenium.UserRegister import test_user_register
from Selenium.UserLogin import test_user_login


def main():
    driver = webdriver.Edge()
    test_user_register(driver)
    print()
    test_user_login(driver)
    driver.quit()


if __name__ == "__main__":
    main()
