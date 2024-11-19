from utils.utils import *
from Selenium.UserLogin import test_user_login
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

ip = get_variable_value("IP_FRONTEND")
login_path = get_variable_value("LOGIN_USER")
register_path = get_variable_value("REGISTER_USER")
delay = int(get_variable_value("DELAY"))
login_url = f"http://{ip}{login_path}"
register_url = f"http://{ip}{register_path}"
home_path = get_variable_value("HOME_PATH")
home_url = f"http://{ip}{home_path}"


def test_check_restaurant(driver):
    info("TEST CHECK RESTAURANTS")
    try:
        driver.get(home_url)
        wait_for_url_to_be(driver, home_url)

        check_page_title(driver, "React App")

        wait_for_element(driver, By.ID, "root")

        click_button(driver, By.ID, "homePage-listItemButton")
        wait_for(delay)
        click_button(driver, By.CSS_SELECTOR, '[data-testid="EditCalendarIcon"]')
        # click_button(driver, By.CSS_SELECTOR, '[data-testid="CloseSharpIcon"]')
        driver.back()
        click_button(driver, By.ID, "homePage-listItemButton")
        wait_for(delay)
        click_button(driver, By.CSS_SELECTOR, '[data-testid="EventIcon"]')
        wait_for(delay)
        click_button(driver, By.CSS_SELECTOR, '[data-testid="CloseSharpIcon"]')
        wait_for(delay)
        click_button(driver, By.CSS_SELECTOR, '[data-testid="RestaurantMenuIcon"]')
        wait_for(delay)
        #Sprawdzamy czy wyświetlają się jakieś dania \/
        find_text_in_elements(driver, By.CSS_SELECTOR, "div.flex.gap-3", "zł")
        click_button(driver, By.CSS_SELECTOR, '[data-testid="ChevronRightIcon"]');
        click_button(driver, By.CSS_SELECTOR, '[data-testid="ChevronLeftIcon"]');
        wait_for(delay)
        # menuitem_name = wait_for_element(driver, By.CSS_SELECTOR, 'h1.dark\\:text-white.text-lg.h-\\[22px\\]')
        # assert menuitem_name is not None, "Nazwa jedzenia nie jest widoczna."
        # info(f"Nazwa jedzenia: {menuitem_name.text}")
        # wait_for(delay)
        click_button(driver, By.CSS_SELECTOR, '[data-testid="CloseSharpIcon"]')
        wait_for(delay)
        click_button(driver, By.CSS_SELECTOR, '[data-testid="DeliveryDiningIcon"]')
        wait_for(delay)
        click_button(driver, By.CSS_SELECTOR, '[data-testid="CloseSharpIcon"]')

        wait_for(delay)
        driver.refresh()
        wait_for(delay)
        click_button(driver, By.ID, "homePage-listItemButton")
        wait_for(delay)
        three_star_input = driver.find_element(By.XPATH, "//input[@type='radio' and @value='3']")
        three_star_input.find_element(By.XPATH, "./..").click()
        wait_for(delay)
        click_button(driver, By.CSS_SELECTOR, '[data-testid="SwapVertIcon"]')
        wait_for(delay)
        # click_button(driver, By.CSS_SELECTOR, '[data-testid="AddIcon"]')
        # wait_for(delay)
        # Nizej: Message: element click intercepted Do sprawdzenia
        # three_star_input = WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, "//input[@type='radio' and @value='3']"))
        # )
        # three_star_input.click()
        # textarea = driver.find_element(By.CSS_SELECTOR, ".w-full.p-4.border.rounded")
        # textarea.send_keys("Testowa opinia")
        # wait_for(delay)
        # submit_button = driver.find_element(By.CSS_SELECTOR, ".MuiButton-root.MuiButton-textPrimary.rounded-lg")
        # submit_button.click()

        elements = get_elements_list(driver, By.CSS_SELECTOR, '[id="homePage-listItemButton"]')

        for element in elements:
            element.click()
            wait_for_element(driver, By.ID, "after-image-slider-controls")
            wait_for(delay)

            # Sprawdzenie obecności nazwy restauracji
            restaurant_name = wait_for_element(driver, By.CSS_SELECTOR, 'h2.text-2xl.font-bold.dark\\:text-white')
            assert restaurant_name is not None, "Nazwa restauracji nie jest widoczna."
            info(f"Nazwa restauracji: {restaurant_name.text}")

            # Sprawdzenie obecności opinii (średnia liczba gwiazdek oraz wizualne gwiazdki)
            rating_value = wait_for_element(driver, By.CSS_SELECTOR, 'div.flex.items-center.gap-2.dark\\:text-white h1')
            assert rating_value is not None, "Średnia ocena restauracji nie jest widoczna."
            info(f"Średnia ocena restauracji: {rating_value.text}")

            # Sprawdzenie obecności wizualnych gwiazdek
            rating_stars = wait_for_element(driver, By.CSS_SELECTOR,
                                            'div.flex.items-center.gap-2.dark\\:text-white span.MuiRating-root')
            assert rating_stars is not None, "Gwiazdkowa ocena restauracji nie jest widoczna."
            info("Wizualne gwiazdki są widoczne.")

            # Sprawdzenie przewijania zdjęć
            left_arrow = wait_for_element(driver, By.CSS_SELECTOR, '[data-testid="ArrowBackIosNewRoundedIcon"]')
            right_arrow = wait_for_element(driver, By.CSS_SELECTOR, '[data-testid="ArrowForwardIosRoundedIcon"]')

            # Weryfikacja, że przyciski przewijania są widoczne i działają
            assert left_arrow is not None, "Przycisk przewijania zdjęć w lewo nie jest widoczny."
            assert right_arrow is not None, "Przycisk przewijania zdjęć w prawo nie jest widoczny."

            # Kliknięcie przycisków przewijania, aby przetestować ich działanie
            info("Kliknięcie strzałki w prawo")
            right_arrow.click()
            wait_for(delay)

            info("Kliknięcie strzałki w lewo")
            left_arrow.click()


    except Exception as e:
        result(str(e), False)
        info("Restaurant check failed")
        info(f"Current URL: {driver.current_url}")
        info(f"Page title: {driver.title}")
        return False  # Test nieudany

    finally:
        wait_for(delay)


if __name__ == "__main__":
    driver = webdriver.Edge()
    driver.maximize_window()
    test_user_login(driver, False)
    test_check_restaurant(driver)
    driver.quit()
