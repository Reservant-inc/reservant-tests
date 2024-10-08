from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from Selenium.UserRegister import test_user_register
from Selenium.UserLogin import test_user_login
from Selenium.EmployeeRegister import test_register_employee



def main():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-gpu")
    driver = webdriver.Chrome(options=chrome_options)
    test_user_register(driver)
    print()
    test_user_login(driver)
    print()
    test_register_employee(driver)
    driver.quit()


if __name__ == "__main__":
    main()
