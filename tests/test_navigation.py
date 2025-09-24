from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urls import BASE_URL
from locators import MainPage, AccountPage, AuthPage
from utils.flows import auth_ready_user

class TestNavigation:

    def test_go_to_account(self, driver):
        auth_ready_user(driver)
        driver.find_element(*MainPage.ACCOUNT).click()
        assert WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(AccountPage.PROFILE_EXIT)
        )

    def test_account_to_constructor_via_button(self, driver):
        auth_ready_user(driver)
        driver.find_element(*MainPage.ACCOUNT).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(AccountPage.CONSTRUCTOR)).click()
        assert WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(MainPage.SIGN_IN)
        )

    def test_account_to_constructor_via_logo(self, driver):
        auth_ready_user(driver)
        driver.find_element(*MainPage.ACCOUNT).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(AccountPage.PROFILE_EXIT))
        driver.find_element(*MainPage.LOGO).click()
        assert WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(MainPage.SIGN_IN)
        )

    def test_logout(self, driver):
        auth_ready_user(driver)
        driver.find_element(*MainPage.ACCOUNT).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(AccountPage.PROFILE_EXIT)).click()
        assert WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(AuthPage.LOGIN_BUTTON)
        )

