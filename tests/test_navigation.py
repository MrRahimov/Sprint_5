from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import BASE_URL, MainPage, AuthPage, AccountPage
from utils.generators import gen_email, gen_password

def auth_ready_user(driver):
    email = gen_email("nav_")
    password = gen_password(8)
    driver.get(BASE_URL)
    driver.find_element(*MainPage.ACCOUNT).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(AuthPage.REGISTER_LINK)).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(AuthPage.NAME))
    driver.find_element(*AuthPage.NAME).send_keys("Нав")
    driver.find_element(*AuthPage.EMAIL).send_keys(email)
    driver.find_element(*AuthPage.PASSWORD).send_keys(password)
    driver.find_element(*AuthPage.REGISTER_BUTTON).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(AuthPage.LOGIN_BUTTON))
    driver.find_element(*AuthPage.EMAIL).send_keys(email)
    driver.find_element(*AuthPage.PASSWORD).send_keys(password)
    driver.find_element(*AuthPage.LOGIN_BUTTON).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(MainPage.ACCOUNT))
    return email, password

def test_go_to_account(driver):
    auth_ready_user(driver)
    driver.find_element(*MainPage.ACCOUNT).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(AccountPage.PROFILE_EXIT))

def test_account_to_constructor_via_button(driver):
    auth_ready_user(driver)
    driver.find_element(*MainPage.ACCOUNT).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(AccountPage.CONSTRUCTOR)).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(MainPage.CHECKOUT))

def test_account_to_constructor_via_logo(driver):
    auth_ready_user(driver)
    driver.find_element(*MainPage.ACCOUNT).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(AccountPage.PROFILE_EXIT))
    driver.find_element(*MainPage.LOGO).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(MainPage.CHECKOUT))

def test_logout(driver):
    auth_ready_user(driver)
    driver.find_element(*MainPage.ACCOUNT).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(AccountPage.PROFILE_EXIT)).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(AuthPage.LOGIN_BUTTON))

