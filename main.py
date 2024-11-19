from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from Selenium.AcceptFriendRequest import test_accept_friend_invite
from Selenium.DeclineFriendRequest import test_decline_friend_invite
from Selenium.EmployeeManagement import test_employee_management
from Selenium.RemoveFriend import test_remove_friend
from Selenium.RemoveOutgoingRequest import test_remove_outgoing_request
from Selenium.ReviewTest import test_review
from Selenium.UserRegister import test_user_register
from Selenium.UserLogin import test_user_login
from Selenium.EmployeeRegister import test_register_employee
from Selenium.RegisterRestaurant import test_register_restaurant
from Selenium.MenuManagement import test_menu_management
from Selenium.CheckRestaurant import test_check_restaurant
from Selenium.WarehouseManagement import test_warehouse_management
from Services.recreate_database import DebugService
from utils.utils import get_variable_value

ip = get_variable_value("IP_BACKEND")
backend_url = f"http://{ip}"


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
    test_employee_management(driver)
    print()
    test_register_employee(driver)
    print()
    test_menu_management(driver, True)
    print()
    test_review(driver)
    print()
    test_warehouse_management(driver)
    print()
    test_accept_friend_invite(driver)
    print()
    test_decline_friend_invite(driver)
    print()
    test_remove_outgoing_request(driver)
    print()
    test_remove_friend(driver)
    driver.quit()


if __name__ == "__main__":
    service = DebugService(backend_url)
    try:
        result = service.recreate_database()
        print("Odpowiedź serwera:", result)
        main()
    except Exception as e:
        print("Nie udało się wywołać końcówki:", e)
