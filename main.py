from selenium import webdriver
from Selenium.UserRegister import test_user_register


def main():
    driver = webdriver.Edge()
    test_user_register(driver)
    driver.quit()


if __name__ == "__main__":
    main()
