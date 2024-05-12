from selenium import webdriver
from Selenium.UserRegister import test_user_register
from utils.utils import info


def main():
    driver = webdriver.Edge()
    test_user_register(driver)
    driver.quit()


if __name__ == "__main__":
    main()
