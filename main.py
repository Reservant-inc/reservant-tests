from selenium import webdriver
from Selenium.UserRegister import test_user_register
from Selenium.UserLogin import test_user_login
from Services.APIService import APIService
from Services.RestaurantService import RestaurantService


def main():
    api_service = APIService()

    # Replace with actual login credentials and login URL
    credentials = {
        'login': 'JD',
        'password': 'Pa$$w0rd'
    }
    login_success = api_service.login_user('auth/login', credentials)

    if login_success:
        print("Login successful and token saved.")

        # Fetching restaurant data using the RestaurantService
        restaurant_service = RestaurantService(api_service)
        restaurants = restaurant_service.get_restaurants()
        print("Restaurants:", restaurants)
    else:
        print("Login failed.")

    # driver = webdriver.Edge()
    # test_user_register(driver)
    # print()
    # test_user_login(driver)
    # driver.quit()


if __name__ == "__main__":
    main()
