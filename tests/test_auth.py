from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import BASE_URL, MainPage, AuthPage, AccountPage
from utils.generators import gen_email, gen_password

def open_login(driver):
    driver.get(BASE_URL)
    driver.find_element(*MainPage.SIGN_IN).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(AuthPage.LOGIN_BUTTON))

def register_flow(driver, name, email, password):
    driver.get(BASE_URL)
    driver.find_element(*MainPage.ACCOUNT).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(AuthPage.REGISTER_LINK)).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(AuthPage.NAME))
    driver.find_element(*AuthPage.NAME).send_keys(name)
    driver.find_element(*AuthPage.EMAIL).send_keys(email)
    driver.find_element(*AuthPage.PASSWORD).send_keys(password)
    driver.find_element(*AuthPage.REGISTER_BUTTON).click()

def login_flow(driver, email, password):
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(AuthPage.EMAIL))
    driver.find_element(*AuthPage.EMAIL).clear()
    driver.find_element(*AuthPage.EMAIL).send_keys(email)
    driver.find_element(*AuthPage.PASSWORD).clear()
    driver.find_element(*AuthPage.PASSWORD).send_keys(password)
    driver.find_element(*AuthPage.LOGIN_BUTTON).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(MainPage.ACCOUNT))

def test_registration_success(driver):
    email = gen_email("elmar_")
    password = gen_password(8)
    register_flow(driver, "Эльмар", email, password)
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(AuthPage.LOGIN_BUTTON))
    login_flow(driver, email, password)

def test_registration_short_password_error(driver):
    email = gen_email("short_")
    register_flow(driver, "Тест", email, "12345")
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(AuthPage.ERROR_PASSWORD))

def test_login_via_main_button(driver):
    email = gen_email("btn_")
    password = gen_password(8)
    register_flow(driver, "Кнопка", email, password)
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(AuthPage.LOGIN_BUTTON))
    open_login(driver)
    login_flow(driver, email, password)

def test_login_via_account_button(driver):
    email = gen_email("acc_")
    password = gen_password(8)
    register_flow(driver, "Акк", email, password)
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(AuthPage.LOGIN_BUTTON))
    driver.get(BASE_URL)
    driver.find_element(*MainPage.ACCOUNT).click()
    login_flow(driver, email, password)

def test_login_via_register_form_button(driver):
    email = gen_email("reg_")
    password = gen_password(8)
    register_flow(driver, "Рег", email, password)
    WebDriverWait(driver, 15).until(EC.visibility_of_element_located(AuthPage.LOGIN_BUTTON))
    driver.find_element(*AuthPage.EMAIL).send_keys(email)
    driver.find_element(*AuthPage.PASSWORD).send_keys(password)
    driver.find_element(*AuthPage.LOGIN_BUTTON).click()
    WebDriverWait(driver, 15).until(EC.invisibility_of_element_located(AuthPage.LOGIN_BUTTON))
    WebDriverWait(driver, 15).until(
        EC.any_of(
            EC.visibility_of_element_located(MainPage.SIGN_IN),   
            EC.visibility_of_element_located(MainPage.ACCOUNT)    
        )
    )

def test_login_via_forgot_password_button(driver):
    email = gen_email("forgot_")
    password = gen_password(8)
    register_flow(driver, "Забыл", email, password)
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(AuthPage.LOGIN_BUTTON))
    driver.find_element(*AuthPage.FORGOT_PASSWORD_LINK).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(AuthPage.LOGIN_LINK)).click()
    login_flow(driver, email, password)

