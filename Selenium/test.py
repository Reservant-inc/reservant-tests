from Selenium.UserLogin import test_user_login
from utils.utils import wait_for


def foo(driver):

    try:
        print()

    except Exception:


        print("example test")
        test_user_login(driver, check_signup=False)
    # ...

    finally:
        wait_for(2)