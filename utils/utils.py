import os
from dotenv import load_dotenv
import time
from faker.decode import unidecode
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from faker import Faker
from DTOs.LoginDataDTO import LoginData

load_dotenv()


def get_variable_value(var_key: str):
    return os.getenv(var_key)


def get_all_variables():
    return os.environ.items()


def wait_for(seconds):
    time.sleep(seconds)


def log(result: bool, message: str):
    if result:
        print(f"[TEST PASSED] {message}")
    else:
        print(f"[TEST FAILED] {message}")


def click_button(driver, selector_type, selector_value):
    """
    Znajduje i klika przycisk na stronie używając podanego selektora CSS.
    Rzuca wyjątek, jeśli przycisk nie zostanie znaleziony.

    Args:
    driver (WebDriver): Instancja WebDrivera używana do interakcji z przeglądarką.
    selector (str): Selektor CSS użyty do znalezienia przycisku.

    Raises:
    Exception: Jeśli przycisk nie zostanie znaleziony.
    """
    try:
        button = driver.find_element(selector_type, selector_value)  # TODO zmienic na id
        button.click()
    except NoSuchElementException:
        raise Exception(f"Couldn't click button with {selector_type} '{selector_value}'")


def wait_for_element(driver, selector_type, selector_value, timeout=get_variable_value("TIMEOUT")):
    """
    Czeka na obecność elementu na stronie w określonym czasie.

    Args:
    driver (WebDriver): Instancja WebDrivera używana do interakcji z przeglądarką.
    selector_type (By): Typ selektora (np. By.ID, By.CSS_SELECTOR).
    selector_value (str): Wartość selektora.
    timeout (int): Maksymalny czas oczekiwania w sekundach (domyślnie 10).

    Raises:
    TimeoutException: Jeśli element nie zostanie znaleziony w określonym czasie.
    """
    try:
        return WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((selector_type, selector_value))
        )
    except TimeoutException:
        raise TimeoutException(
            f"Element with {selector_type} '{selector_value}' is not present on the page within {timeout} seconds.")


def enter_text(driver, selector_type, selector_value, text):
    """
    Znajduje element na stronie i wpisuje do niego tekst.

    Args:
    driver (WebDriver): Instancja WebDrivera używana do interakcji z przeglądarką.
    selector_type (By): Typ selektora (np. By.ID, By.CSS_SELECTOR).
    selector_value (str): Wartość selektora.
    text (str): Tekst do wpisania w element.

    Raises:
    NoSuchElementException: Jeśli element nie zostanie znaleziony.
    """
    try:
        input_field = driver.find_element(selector_type, selector_value)
        input_field.send_keys(text)
        input_field.send_keys(Keys.TAB)
    except NoSuchElementException:
        raise NoSuchElementException(f"Element with {selector_type} '{selector_value}' not found.")


def universal_wait_for(driver, condition_type, selector_type=None, selector_value=None, different_value=None,
                       timeout=get_variable_value("TIMEOUT")):
    """
    Uniwersalna funkcja oczekiwania, która czeka na spełnienie różnych warunków.

    Args:
    driver (WebDriver): Instancja WebDrivera używana do interakcji z przeglądarką.
    condition_type (callable): Typ warunku z modułu expected_conditions.
    selector_type (By): Typ selektora (np. By.ID, By.CSS_SELECTOR).
    selector_value (str): Wartość selektora.
    timeout (int): Maksymalny czas oczekiwania w sekundach (domyślnie 10).

    Returns:
    WebElement: Znaleziony element, jeśli warunek został spełniony.

    Raises:
    TimeoutException: Jeśli warunek nie zostanie spełniony w określonym czasie.
    """
    try:
        if selector_value is not None and selector_type is not None:
            element = WebDriverWait(driver, timeout).until(
                condition_type((selector_type, selector_value))
            )
        else:
            element = WebDriverWait(driver, timeout).until(
                condition_type(different_value)
            )
        return element
    except TimeoutException:
        raise TimeoutException(
            f"Condition {condition_type.__name__} not met for element with {selector_type} '{selector_value}' within {timeout} seconds.")


def get_text_from_elements_by_class(driver, selector_type, selector_value):
    """
    Pobiera wartości tekstowe z elementów HTML o podanej klasie.

    Args:
    driver (webdriver): Instancja WebDriver używana do kontroli przeglądarki.
    class_name (str): Nazwa klasy elementów, z których ma być pobierany tekst.

    Returns:
    List[str]: Lista zawierająca wartości tekstowe z elementów o podanej klasie.
    """
    # Znajdowanie elementów po klasie
    elements = driver.find_elements(selector_type, selector_value)

    # Pobieranie tekstów z każdego elementu
    texts = [element.text for element in elements]

    return texts


def generate_login_data():
    fake = Faker('pl_PL')
    first_name = fake.first_name()
    last_name = fake.last_name()
    login = unidecode(first_name).lower()[:3] + unidecode(last_name).lower()[:3]
    email = fake.email()
    phone_number = fake.phone_number().replace(' ', '')[-9:]
    birth_day = fake.date_of_birth().strftime('%d.%m.%Y')
    password = get_variable_value("TEST_PASSWORD")

    return LoginData(first_name, last_name, login, email, phone_number, birth_day, password)


if __name__ == "__main__":

    def print_all_env_variables():
        print("All variables:")
        for key, value in get_all_variables():
            print(f"{key}: {value}")


    print_all_env_variables()
