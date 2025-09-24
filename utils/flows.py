from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urls import BASE_URL
from locators import MainPage, AuthPage
from utils.generators import gen_email, gen_password

def open_login(driver):
    driver.get(BASE_URL)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(MainPage.SIGN_IN)).click()

def register_flow(driver, name, email, password):
    open_login(driver)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(AuthPage.REGISTER_LINK)).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(AuthPage.NAME))
    driver.find_element(*AuthPage.NAME).send_keys(name)
    driver.find_element(*AuthPage.EMAIL).send_keys(email)
    driver.find_element(*AuthPage.PASSWORD).send_keys(password)
    driver.find_element(*AuthPage.REGISTER_BUTTON).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(AuthPage.LOGIN_BUTTON))

def login_flow(driver, email, password):
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(AuthPage.EMAIL))
    driver.find_element(*AuthPage.EMAIL).clear()
    driver.find_element(*AuthPage.EMAIL).send_keys(email)
    driver.find_element(*AuthPage.PASSWORD).clear()
    driver.find_element(*AuthPage.PASSWORD).send_keys(password)
    driver.find_element(*AuthPage.LOGIN_BUTTON).click()
    WebDriverWait(driver, 10).until(EC.invisibility_of_element_located(MainPage.SIGN_IN))

def auth_ready_user(driver):
    email = gen_email("nav_")
    password = gen_password(8)
    register_flow(driver, "Нав", email, password)
    login_flow(driver, email, password)
    return email, password

