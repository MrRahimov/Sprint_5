from selenium.webdriver.common.by import By

BASE_URL = "https://stellarburgers.nomoreparties.site/"

class MainPage:
    SIGN_IN = (By.XPATH, "//button[normalize-space()='Войти в аккаунт']")
    ACCOUNT = (By.XPATH, "//p[normalize-space()='Личный Кабинет']")
    LOGO = (By.XPATH, "//div[@class='AppHeader_header__logo__2D0X2']")
    CONSTRUCTOR = (By.XPATH, "//p[normalize-space()='Конструктор']")
    CHECKOUT = (By.XPATH, "//button[normalize-space()='Оформить заказ']")

    BUNS = (By.XPATH, "//span[text()='Булки']")
    SAUCES = (By.XPATH, "//span[text()='Соусы']")
    FILLINGS = (By.XPATH, "//span[text()='Начинки']")


class AuthPage:
    NAME = (By.XPATH, "//label[text()='Имя']/following-sibling::input")
    EMAIL = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    PASSWORD = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")

    REGISTER_BUTTON = (By.XPATH, "//button[normalize-space()='Зарегистрироваться']")
    REGISTER_LINK = (By.XPATH, "//a[normalize-space()='Зарегистрироваться']")
    FORGOT_PASSWORD_LINK = (By.XPATH, "//a[normalize-space()='Восстановить пароль']")
    
    
    TO_LOGIN_LINK = (By.XPATH, "//a[@href='/login' and normalize-space()='Войти']")
    LOGIN_BUTTON = (By.XPATH, "//form//button[normalize-space()='Войти']")
    LOGIN_LINK = (By.XPATH, "//a[normalize-space()='Войти']")         
    ERROR_PASSWORD = (By.XPATH, "//p[contains(@class,'input__error') and normalize-space()='Некорректный пароль']")

class AccountPage:
    PROFILE_EXIT = (By.XPATH, "//button[normalize-space()='Выход']")
    CONSTRUCTOR = (By.XPATH, "//p[normalize-space()='Конструктор']")

class ConstructorTabs:
    BUNS_TAB = (By.XPATH, "//span[normalize-space()='Булки']")
    SAUCES_TAB = (By.XPATH, "//span[normalize-space()='Соусы']")
    FILLINGS_TAB = (By.XPATH, "//span[normalize-space()='Начинки']")
    ACTIVE_TAB = (By.XPATH, "//div[contains(@class,'tab_tab_type_current')]/span")

