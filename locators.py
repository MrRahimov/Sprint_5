from selenium.webdriver.common.by import By

class MainPage:
    SIGN_IN = (By.XPATH, "//button[normalize-space()='Войти в аккаунт']")
    ACCOUNT = (By.XPATH, "//p[normalize-space()='Личный Кабинет']")
    LOGO = (By.XPATH, "//div[contains(@class,'AppHeader_header__logo')]")
    CONSTRUCTOR = (By.XPATH, "//p[normalize-space()='Конструктор']")

class AuthPage:
    NAME = (By.NAME, "name")
    EMAIL = (By.NAME, "name") 
    PASSWORD = (By.NAME, "Пароль")  
    REGISTER_LINK = (By.XPATH, "//a[normalize-space()='Зарегистрироваться']")
    REGISTER_BUTTON = (By.XPATH, "//button[normalize-space()='Зарегистрироваться']")
    LOGIN_BUTTON = (By.XPATH, "//button[normalize-space()='Войти']")
    LOGIN_LINK = (By.XPATH, "//a[normalize-space()='Войти']")
    FORGOT_PASSWORD_LINK = (By.XPATH, "//a[normalize-space()='Восстановить пароль']")
    ERROR_PASSWORD = (By.XPATH, "//*[contains(text(),'Некорректный пароль')]")

class AccountPage:
    PROFILE_EXIT = (By.XPATH, "//button[normalize-space()='Выход']")
    CONSTRUCTOR = (By.XPATH, "//p[normalize-space()='Конструктор']")

class ConstructorTabs:
    SAUCES_TAB = (By.XPATH, "//span[normalize-space()='Соусы']")
    FILLINGS_TAB = (By.XPATH, "//span[normalize-space()='Начинки']")
    BUNS_TAB = (By.XPATH, "//span[normalize-space()='Булки']")
    ACTIVE_TAB = (By.XPATH, "//div[contains(@class,'tab_tab_type_current')]/span")

