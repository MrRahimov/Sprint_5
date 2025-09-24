from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urls import BASE_URL
from locators import ConstructorTabs

class TestConstructorTabs:

    def test_sauces_tab_active(self, driver):
        driver.get(BASE_URL)
        driver.find_element(*ConstructorTabs.SAUCES_TAB).click()
        assert WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element(ConstructorTabs.ACTIVE_TAB, "Соусы")
        )

    def test_fillings_tab_active(self, driver):
        driver.get(BASE_URL)
        driver.find_element(*ConstructorTabs.FILLINGS_TAB).click()
        assert WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element(ConstructorTabs.ACTIVE_TAB, "Начинки")
        )

    def test_buns_tab_active(self, driver):
        driver.get(BASE_URL)
        driver.find_element(*ConstructorTabs.BUNS_TAB).click()
        assert WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element(ConstructorTabs.ACTIVE_TAB, "Булки")
        )

