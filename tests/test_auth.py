from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urls import BASE_URL
from locators import MainPage, AuthPage
from utils.generators import gen_email, gen_password
from utils.flows import open_login, register_flow, login_flow

class TestAuth:

    def test_registration_success(self, driver):
        email = gen_email("elmar_")
        password = gen_password(8)
        register_flow(driver, "Эльмар", email, password)
        assert WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(AuthPage.LOGIN_BUTTON)
        )

    def test_registration_short_password_error(self, driver):
        email = gen_email("short_")
        open_login(driver)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(AuthPage.REGISTER_LINK)).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(AuthPage.NAME))
        driver.find_element(*AuthPage.NAME).send_keys("Тест")
        driver.find_element(*AuthPage.EMAIL).send_keys(email)
        driver.find_element(*AuthPage.PASSWORD).send_keys("12345")
        driver.find_element(*AuthPage.REGISTER_BUTTON).click()
        assert WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(AuthPage.ERROR_PASSWORD)
        )

    def test_login_via_main_button(self, driver):
        email = gen_email("btn_")
        password = gen_password(8)
        register_flow(driver, "Кнопка", email, password)
        open_login(driver)
        login_flow(driver, email, password)
        assert WebDriverWait(driver, 10).until(
            EC.invisibility_of_element_located(MainPage.SIGN_IN)
        )

    def test_login_via_account_button(self, driver):
        email = gen_email("acc_")
        password = gen_password(8)
        register_flow(driver, "Акк", email, password)
        driver.get(BASE_URL)
        driver.find_element(*MainPage.ACCOUNT).click()
        login_flow(driver, email, password)
        assert WebDriverWait(driver, 10).until(
            EC.invisibility_of_element_located(MainPage.SIGN_IN)
        )

    def test_login_via_register_form_button(self, driver):
        email = gen_email("reg_")
        password = gen_password(8)
        register_flow(driver, "Рег", email, password)
        driver.find_element(*AuthPage.EMAIL).send_keys(email)
        driver.find_element(*AuthPage.PASSWORD).send_keys(password)
        driver.find_element(*AuthPage.LOGIN_BUTTON).click()
        assert WebDriverWait(driver, 10).until(
            EC.invisibility_of_element_located(MainPage.SIGN_IN)
        )

    def test_login_via_forgot_password_button(self, driver):
        email = gen_email("forgot_")
        password = gen_password(8)
        register_flow(driver, "Забыл", email, password)
        driver.find_element(*AuthPage.FORGOT_PASSWORD_LINK).click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(AuthPage.LOGIN_LINK)).click()
        login_flow(driver, email, password)
        assert WebDriverWait(driver, 10).until(
            EC.invisibility_of_element_located(MainPage.SIGN_IN)
        )

