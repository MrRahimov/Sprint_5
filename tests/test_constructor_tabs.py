from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import BASE_URL, MainPage, ConstructorTabs

def test_tabs_switch(driver):
    driver.get(BASE_URL)
    driver.find_element(*ConstructorTabs.SAUCES_TAB).click()
    WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element(ConstructorTabs.ACTIVE_TAB, "Соусы"))
    driver.find_element(*ConstructorTabs.FILLINGS_TAB).click()
    WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element(ConstructorTabs.ACTIVE_TAB, "Начинки"))
    driver.find_element(*ConstructorTabs.BUNS_TAB).click()
    WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element(ConstructorTabs.ACTIVE_TAB, "Булки"))

