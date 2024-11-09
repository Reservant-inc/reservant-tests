from Classes.RandomData import RandomData
from utils.utils import *
from Selenium.UserLogin import test_user_login

ip = get_variable_value("IP_FRONTEND")
login_path = get_variable_value("LOGIN_USER")
register_path = get_variable_value("REGISTER_USER")
delay = int(get_variable_value("DELAY"))
login_url = f"http://{ip}{login_path}"
register_url = f"http://{ip}{register_path}"
home_path = get_variable_value("HOME_PATH")
home_url = f"http://{ip}{home_path}"


def test_menu_management(driver, diff_path = False):
    info("TEST MENU MANAGEMENT")
    try:
        driver.get(home_url)
        wait_for_url_to_be(driver, home_url)

        # TWORZENIE MENU
        check_page_title(driver, "React App")

        wait_for_element(driver, By.ID, "root")

        click_button(driver, By.ID, "NavbarRestaurantsSectionButton")
        wait_for(delay)

        find_text_in_elements(driver, By.CSS_SELECTOR, "div.flex.items-center.gap-4", "Restaurants").click()
        wait_for(delay)

        click_button(driver, By.CSS_SELECTOR, '[data-testid="ArrowForwardIosIcon"]')
        wait_for(delay)

        find_text_in_elements(driver, By.CSS_SELECTOR, "div.flex.items-center.gap-4", "Menu management").click()

        click_button(driver, By.CSS_SELECTOR, '[data-testid="AddIcon"]')

        click_button(driver, By.ID, "addmenuSubmit")

        name = RandomData.generate_word()
        click_text_field(driver, By.ID, "name")
        enter_text(driver, By.ID, "name", name)

        click_text_field(driver, By.ID, "alternateName")
        enter_text(driver, By.ID, "alternateName", RandomData.generate_word())

        click_button(driver, By.ID, "menuType")
        click_button(driver, By.CSS_SELECTOR, f'[value="{RandomData.generate_menu_type()}"]')

        enter_text(driver, By.ID, "dateFrom", RandomData.generate_menu_date_from())

        enter_text(driver, By.ID, "dateUntil", RandomData.generate_menu_date_until())

        wait_for(delay)
        click_button(driver, By.ID, "addmenuSubmit")
        wait_for(delay)
        driver.refresh()

        element = find_text_in_elements(driver, By.CSS_SELECTOR, "div.w-full.flex.justify-between.pr-3", name)
        elements = element.find_elements(By.CSS_SELECTOR, "button")
        elements[1].click()

        # element = find_text_in_elements(driver, By.CSS_SELECTOR, "div.w-full.flex.justify-between.pr-3", name)
        # click_button(driver, By.CSS_SELECTOR, '[data-testid="EditIcon"]');
        wait_for(delay)
        click_text_field(driver, By.ID, "name")
        enter_text(driver, By.ID, "name", "2")
        click_text_field(driver, By.ID, "alternateName")
        enter_text(driver, By.ID, "alternateName", RandomData.generate_word())
        click_button(driver, By.ID, "menuType")
        click_button(driver, By.CSS_SELECTOR, f'[value="{RandomData.generate_menu_type()}"]')
        enter_text(driver, By.ID, "dateFrom", RandomData.generate_menu_date_from())
        wait_for(delay)
        click_button(driver, By.ID, "addmenuSubmit")
        wait_for(delay)

        element = find_text_in_elements(driver, By.CSS_SELECTOR, "div.w-full.flex.justify-between.pr-3", name+"2")
        elements = element.find_elements(By.CSS_SELECTOR, "button")
        elements[0].click()


        if (diff_path):
            png = "Files/test.png"
        else:
            png = "../Files/test.png"

        upload_file(driver, By.ID, "photo", png)
        click_text_field(driver, By.ID, "name")
        enter_text(driver, By.ID, "name", name+"menu")
        click_text_field(driver, By.ID, "price")
        enter_text(driver, By.ID, "price", "22")
        click_text_field(driver, By.ID, "alternateName")
        enter_text(driver, By.ID, "alternateName", RandomData.generate_word())
        click_text_field(driver, By.ID, "alcoholPercentage")
        enter_text(driver, By.ID, "alcoholPercentage", "5")
        select_element = driver.find_element(By.ID, "ingredientId")
        select = Select(select_element)
        select.select_by_value("4")
        click_text_field(driver, By.ID, "amountUsed")
        enter_text(driver, By.ID, "amountUsed", "3")
        click_button(driver, By.ID, "addIngridientToMenuItem")
        click_button(driver, By.ID, "addmenuitemsubmit")
        wait_for(delay)
        #Do edycji menu itemu
        element = find_text_in_elements(
            driver,
            By.CSS_SELECTOR,
            "div.relative.flex.gap-2.w-full.p-4.border-\\[1px\\].border-grey-1.dark\\:border-grey-5.rounded-lg",
            name+"menu"
        )

        actions = ActionChains(driver)
        actions.move_to_element(element).perform()
        elements2 = element.find_elements(By.CSS_SELECTOR, "button")
        print(elements2)
        elements2[0].click()
        click_text_field(driver, By.ID, "name")
        enter_text(driver, By.ID, "name", name+"3")
        click_button(driver, By.ID, "addmenuitemsubmit")
        # elements2[1].click()
        # button = driver.find_element(By.XPATH, "//button[text()='Yes']")

        # # Kliknij przycisk
        # button.click()
        # driver.refresh()

        find_text_in_elements(driver, By.CSS_SELECTOR, "div.w-full.flex.justify-between.pr-3", name+"2")


        # click_button(driver, By.CSS_SELECTOR, '[data-testid="DeleteIcon"]');
        # wait_for(delay)
        # cancel_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Cancel')]")
        # cancel_button.click()
        # scrollable_element = driver.find_element(By.CSS_SELECTOR,
        #                                          'div.overflow-y-auto.scroll.h-full.flex.flex-col.gap-5.scroll-smooth')
        # scrollable_element.send_keys(Keys.PAGE_DOWN)
        # scrollable_element.send_keys(Keys.PAGE_DOWN)
        # scrollable_element.send_keys(Keys.PAGE_DOWN)
        # scrollable_element.send_keys(Keys.PAGE_DOWN)
        # scrollable_element.send_keys(Keys.PAGE_DOWN)
        # scrollable_element.send_keys(Keys.PAGE_DOWN)
        # scrollable_element.send_keys(Keys.PAGE_DOWN)
        # scrollable_element.send_keys(Keys.PAGE_DOWN)
        # scrollable_element.send_keys(Keys.PAGE_DOWN)
        # scrollable_element.send_keys(Keys.PAGE_DOWN)


    except Exception as e:
        result(str(e), False)
        info("Menu Management Failed")
        info(f"Current URL: {driver.current_url}")
        info(f"Page title: {driver.title}")
        return False  # Test nieudany

    finally:
        wait_for(delay)


if __name__ == "__main__":
    driver = webdriver.Edge()
    driver.maximize_window()
    test_user_login(driver, False)
    test_menu_management(driver)
    driver.quit()
