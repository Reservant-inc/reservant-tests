from utils.utils import *

# Getting values from .env file
delay = int(get_variable_value("DELAY"))


def test_name(driver):
    info("EXAMPLE TEST")
    # driver.get(url)

    try:
        info("checking something...")
        # test code here
        # some functions from utils.py

    except Exception as e:
        # If error
        result(str(e), False)
        info("Example test failed: ")
        info("some debug info here")

    # Leave as it is
    finally:
        wait_for(delay)
