import logging
import os
import random

from dotenv import load_dotenv
import time
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException

load_dotenv()
logging.basicConfig(filename='test_log.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')


def get_variable_value(var_key: str):
    return os.getenv(var_key)


timeout = int(get_variable_value("TIMEOUT"))


def get_all_variables():
    return os.environ.items()


def wait_for(seconds):
    time.sleep(seconds)


def result(message, success=True):
    if success:
        logging.info("[TEST PASSED] " + message)
        print("[TEST PASSED] " + message)
    else:
        logging.error("[TEST FAILED] " + message)
        print("[TEST FAILED] " + message)


def info(message):
    logging.info(message)
    print(message)


def click_button(driver, selector_type, selector_value, critical=True):
    """
    Znajduje i klika przycisk na stronie używając podanego selektora.
    Czeka maksymalnie TIMEOUT sekund, aż przycisk stanie się dostępny.
    Jeśli critical=True, rzuca wyjątek przy niepowodzeniu. Jeśli False, tylko loguje błąd.
    """
    try:
        # Oczekiwanie na element
        wait_for_element(driver, selector_type, selector_value, critical)

        # Znajdowanie elementu po oczekiwaniu
        button = driver.find_element(selector_type, selector_value)
        button.click()
        result(f"Successfully clicked button with {selector_type} '{selector_value}'")
    except (NoSuchElementException, TimeoutException) as e:
        result(f"Couldn't click button with {selector_type} '{selector_value}': {str(e)}", False)
        if critical:
            raise Exception(f"Couldn't click button with {selector_type} '{selector_value}'") from e


def wait_for_element(driver, selector_type, selector_value, critical=True):
    """
    Czeka na obecność elementu na stronie w określonym czasie.
    Jeśli critical=True, rzuca wyjątek przy niepowodzeniu. Jeśli False, tylko loguje błąd.
    """

    try:
        element = WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((selector_type, selector_value))
        )
        result(f"Element with {selector_type} '{selector_value}' is present on the page.")
        return element
    except TimeoutException as e:
        result(
            f"Element with {selector_type} '{selector_value}' is not present on the page within {timeout} seconds: {str(e)}",
            False)
        if critical:
            raise TimeoutException(
                f"Element with {selector_type} '{selector_value}' is not present on the page within {timeout} seconds.") from e


def enter_text(driver, selector_type, selector_value, text, critical=True):
    """
    Znajduje element na stronie i wpisuje do niego tekst.
    Jeśli critical=True, rzuca wyjątek przy niepowodzeniu. Jeśli False, tylko loguje błąd.
    """
    try:
        # Oczekiwanie na element
        wait_for_element(driver, selector_type, selector_value, critical)

        input_field = driver.find_element(selector_type, selector_value)
        input_field.send_keys(text)
        input_field.send_keys(Keys.TAB)
        result(f"Successfully entered text into element with {selector_type} '{selector_value}'")
    except NoSuchElementException as e:
        result(f"Couldn't find element with {selector_type} '{selector_value}' to enter text: {str(e)}", False)
        if critical:
            raise NoSuchElementException(
                f"Couldn't find element with {selector_type} '{selector_value}' to enter text.") from e


def universal_wait_for(driver, condition_type, selector_type=None, selector_value=None, different_value=None,
                       critical=True):
    """
    Uniwersalna funkcja oczekiwania, która czeka na spełnienie różnych warunków.
    Jeśli critical=True, rzuca wyjątek przy niepowodzeniu. Jeśli False, tylko loguje błąd.
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
        result(f"Condition {condition_type.__name__} met for element with {selector_type} '{selector_value}'")
        return element
    except TimeoutException as e:
        result(
            f"Condition {condition_type.__name__} not met for element with {selector_type} '{selector_value}' within {timeout} seconds: {str(e)}",
            False)
        if critical:
            raise TimeoutException(
                f"Condition {condition_type.__name__} not met for element with {selector_type} '{selector_value}' within {timeout} seconds.") from e


def click_text_field(driver, selector_type, selector_value, critical=True):
    """
    Znajduje i klika pole tekstowe na stronie używając podanego selektora.
    Jeśli critical=True, rzuca wyjątek przy niepowodzeniu. Jeśli False, tylko loguje błąd.
    """
    try:
        # Oczekiwanie na element
        wait_for_element(driver, selector_type, selector_value, critical)

        text_field = driver.find_element(selector_type, selector_value)
        text_field.click()
        result(f"Successfully clicked text field with {selector_type} '{selector_value}'")
    except NoSuchElementException as e:
        result(f"Couldn't find text field with {selector_type} '{selector_value}': {str(e)}", False)
        if critical:
            raise NoSuchElementException(f"Couldn't find text field with {selector_type} '{selector_value}'") from e


def press_tab_key(driver, critical=True):
    """
    Symuluje naciśnięcie klawisza TAB w przeglądarce.
    Jeśli critical=True, rzuca wyjątek przy niepowodzeniu. Jeśli False, tylko loguje błąd.
    """
    try:
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.perform()
        result("Successfully pressed TAB key.")
    except Exception as e:
        result(f"Failed to press TAB key: {str(e)}", False)
        if critical:
            raise Exception("Failed to press TAB key.") from e


def get_text_from_elements_by_class(driver, selector_type, selector_value, critical=True):
    """
    Pobiera wartości tekstowe z elementów HTML o podanym selektorze.

    Args:
    driver (webdriver): Instancja WebDriver używana do kontroli przeglądarki.
    selector_type (By): Typ selektora (np. By.CLASS_NAME, By.CSS_SELECTOR).
    selector_value (str): Wartość selektora, używana do znalezienia elementów.

    Returns:
    List[str]: Lista zawierająca wartości tekstowe z elementów znalezionych przy użyciu selektora.

    Raises:
    NoSuchElementException: Jeśli elementy nie zostaną znalezione (jeśli critical=True).
    """
    try:
        # Oczekiwanie na element
        wait_for_element(driver, selector_type, selector_value, critical)

        # Znajdowanie elementów po podanym selektorze
        elements = driver.find_elements(selector_type, selector_value)

        # Sprawdzenie, czy elementy zostały znalezione
        if not elements:
            raise NoSuchElementException(f"No elements found with {selector_type} '{selector_value}'")

        # Pobieranie tekstów z każdego elementu
        texts = [element.text for element in elements]
        result(f"Successfully retrieved text from elements with {selector_type} '{selector_value}'")
        return texts

    except NoSuchElementException as e:
        result(f"Couldn't find elements with {selector_type} '{selector_value}': {str(e)}", False)
        if critical:
            raise NoSuchElementException(f"Couldn't find elements with {selector_type} '{selector_value}'") from e


def check_page_title(driver, expected_title, critical=False):
    """
    Sprawdza, czy tytuł strony jest zgodny z oczekiwanym.

    Args:
    driver (webdriver): Instancja WebDriver używana do kontroli przeglądarki.
    expected_title (str): Oczekiwany tytuł strony.
    critical (bool): Określa, czy niezgodność tytułu ma być traktowana jako krytyczna. Domyślnie False.

    """
    try:
        actual_title = driver.title
        if actual_title == expected_title:
            result(f"Page title is correct: '{actual_title}'")
        else:
            result(f"Page title is incorrect. Expected: '{expected_title}', but got: '{actual_title}'", False)
            if critical:
                raise AssertionError(f"Expected page title '{expected_title}', but got '{actual_title}'")
    except Exception as e:
        result(f"Failed to check page title: {str(e)}", False)
        if critical:
            raise e


def wait_for_url_to_be(driver, expected_url, critical=True):
    """
    Czeka na zmianę URL do oczekiwanego w określonym czasie.

    Args:
    driver (webdriver): Instancja WebDriver używana do kontroli przeglądarki.
    expected_url (str): Oczekiwany URL strony.
    timeout (int): Maksymalny czas oczekiwania na zmianę URL (w sekundach). Jeśli None, pobiera z konfiguracji.
    critical (bool): Określa, czy błąd ma być traktowany jako krytyczny. Domyślnie True.
    """

    try:
        # Czekamy, aż URL stanie się oczekiwanym
        WebDriverWait(driver, timeout).until(EC.url_to_be(expected_url))
        result(f"URL changed to expected: '{expected_url}'")
    except TimeoutException as e:
        result(
            f"URL did not change to expected within {timeout} seconds. Expected: '{expected_url}', but got: '{driver.current_url}'",
            False)
        if critical:
            raise TimeoutException(
                f"URL did not change to expected within {timeout} seconds. Expected: '{expected_url}', but got: '{driver.current_url}'") from e


def verify_unique_column_values(driver, column_selector, critical=True):
    """
    Sprawdza, czy wszystkie wartości w danej kolumnie są unikalne.

    Args:
    driver (webdriver): Instancja WebDriver używana do kontroli przeglądarki.
    column_selector (str): Selektor CSS dla elementów w danej kolumnie.
    critical (bool): Określa, czy błąd ma być krytyczny. Domyślnie ustawiony na True.

    Returns:
    None
    """
    try:
        # Znajdź wszystkie elementy w kolumnie
        wait_for_element(driver, By.CSS_SELECTOR, column_selector, critical)
        elements = driver.find_elements(By.CSS_SELECTOR, column_selector)

        # Pobierz wartości tekstowe z elementów
        values = [element.text for element in elements]

        # Sprawdź unikalność wartości
        if len(values) == len(set(values)):
            result(f"All values in the column '{column_selector}' are unique.")
        else:
            result(f"Duplicate values found in the column '{column_selector}'.", False)
            if critical:
                raise Exception(f"Duplicate values found in the column '{column_selector}'.")
    except Exception as e:
        result(f"Failed to verify uniqueness in column '{column_selector}': {str(e)}", False)
        if critical:
            raise e


def select_option_by_visible_text(driver, selector_type, selector_value, text, critical=True):
    """
    Wybiera opcję w elemencie <select> na podstawie widocznego tekstu.
    Jeśli critical=True, rzuca wyjątek przy niepowodzeniu. Jeśli False, tylko loguje błąd.

    Args:
    driver (webdriver): Instancja WebDriver.
    select_id (str): ID elementu <select>.
    text (str): Tekst widoczny w opcji, którą chcemy wybrać.
    critical (bool): Jeśli True, podnosi wyjątek w przypadku niepowodzenia, inaczej tylko loguje.
    """
    try:
        wait_for_element(driver, selector_type, selector_value, critical)
        select_element = driver.find_element(selector_type, selector_value)
        select = Select(select_element)
        select.select_by_visible_text(text)
        result(f"Successfully selected option with text '{text}' from '{selector_value}'")
    except Exception as e:
        result(f"Failed to select option with text '{text}' from '{selector_value}': {str(e)}", False)
        if critical:
            raise Exception(f"Failed to select option with text '{text}' from '{selector_value}'") from e


def upload_file(driver, selector_type, selector_value, file_path, critical=True):
    """
    Wstawia plik do elementu na stronie za pomocą send_keys.
    Jeśli critical=True, rzuca wyjątek przy niepowodzeniu. Jeśli False, tylko loguje błąd.

    Args:
    driver (webdriver): Instancja WebDriver używana do kontroli przeglądarki.
    selector_type (By): Typ selektora używany do znalezienia elementu (np. By.CSS_SELECTOR, By.ID).
    selector_value (str): Wartość selektora.
    file_path (str): Ścieżka do pliku, który ma zostać wstawiony.
    critical (bool): Jeśli True, rzuca wyjątek przy niepowodzeniu. Jeśli False, loguje błąd.
    """
    try:
        wait_for_element(driver, selector_type, selector_value, critical)

        # Konwertujemy ścieżkę na absolutną, jeśli nie jest już absolutna
        absolute_file_path = os.path.abspath(file_path)

        file_input = driver.find_element(selector_type, selector_value)
        file_input.send_keys(absolute_file_path)
        result(f"File successfully uploaded using {selector_type} '{selector_value}'")
    except NoSuchElementException as e:
        result(f"Could not upload file using {selector_type} '{selector_value}': {str(e)}", False)
        if critical:
            raise Exception(f"File upload failed for {selector_type} '{selector_value}'") from e


def select_random_tags(driver, selector_type, selector_value, tag_count, critical=True):
    """
    Zaznacza losowe checkboxy (tagi) na stronie.

    Args:
    driver (webdriver): Instancja WebDriver używana do kontroli przeglądarki.
    tag_count (int): Liczba losowych tagów do zaznaczenia.
    selector_type (By): Typ selektora (np. By.ID, By.CSS_SELECTOR, By.XPATH).
    selector_value (str): Wartość selektora używana do wyboru checkboxów.
    critical (bool): Jeśli True, rzuca wyjątek przy niepowodzeniu. Jeśli False, tylko loguje błąd.
    """
    try:
        wait_for_element(driver, selector_type, selector_value, critical)
        # Znajdujemy wszystkie checkboxy przy użyciu przekazanego selektora
        checkboxes = driver.find_elements(selector_type, selector_value)

        # Jeśli liczba checkboxów jest mniejsza niż wymagana liczba tagów do zaznaczenia
        if len(checkboxes) < tag_count:
            result(f"Not enough tags available. Found {len(checkboxes)}, but need {tag_count}.", False)
            if critical:
                raise Exception(f"Not enough tags available to select {tag_count} random tags.")
            return

        # Wybieramy losowe checkboxy
        random_tags = random.sample(checkboxes, tag_count)

        # Klikamy losowe checkboxy
        for tag in random_tags:
            tag.click()

        result(f"Successfully selected {tag_count} random tags.")
    except NoSuchElementException as e:
        result(f"Failed to select random tags: {str(e)}", False)
        if critical:
            raise Exception(f"Failed to select random tags.") from e


def check_checkbox(driver, selector_type, selector_value, critical=True):
    """
    Zaznacza checkbox, jeśli nie jest jeszcze zaznaczony.

    Args:
    driver (webdriver): Instancja WebDriver używana do kontroli przeglądarki.
    selector_type (By): Typ selektora (np. By.ID, By.CSS_SELECTOR, By.XPATH).
    selector_value (str): Wartość selektora używana do wyboru checkboxa.
    critical (bool): Jeśli True, rzuca wyjątek przy niepowodzeniu. Jeśli False, tylko loguje błąd.
    """
    try:
        wait_for_element(driver, selector_type, selector_value, critical)
        # Znajdujemy checkbox
        checkbox = driver.find_element(selector_type, selector_value)

        # Sprawdzamy, czy checkbox nie jest zaznaczony
        if not checkbox.is_selected():
            checkbox.click()
            result(f"Checkbox with {selector_type} '{selector_value}' is checked.")
        else:
            result(f"Checkbox with {selector_type} '{selector_value}' is already checked.")
    except NoSuchElementException as e:
        result(f"Couldn't find checkbox with {selector_type} '{selector_value}': {str(e)}", False)
        if critical:
            raise Exception(f"Couldn't find checkbox with {selector_type} '{selector_value}'") from e


if __name__ == "__main__":
    print()
