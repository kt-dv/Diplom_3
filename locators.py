from selenium.webdriver.common.by import By


class RegistrationLocators:
    NAME_INPUT = (By.NAME, "name")
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    PASSWORD_INPUT = (By.NAME, "Пароль")
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")
    LOGIN_BUTTON = (By.XPATH, "//button[normalize-space(.)='Войти']")
    PASSWORD_ERROR = (By.XPATH, "//p[text()='Некорректный пароль']")
    REGISTRATION_LINK = (By.XPATH, "//a[text()='Зарегистрироваться']")
    FORGOT_PASSWORD_LINK = (By.XPATH, "//a[text()='Восстановить пароль']")
    LOGIN_LINK = (By.XPATH, "//a[text()='Войти']")


class MainPageLocators:
    ACCOUNT_BUTTON = (By.XPATH, "//a[@href='/account']")
    LOGIN_BUTTON = (By.XPATH, "//button[normalize-space()='Войти в аккаунт']")

    # --- Кнопки навигации (используем CSS-селекторы по href) ---
    CONSTRUCTOR_BUTTON = (By.CSS_SELECTOR, "a[href='/']")
    ORDER_FEED_BUTTON = (By.CSS_SELECTOR, "a[href='/feed']")
    CONSTRUCTOR_HEADER = (By.XPATH, "//h1[contains(text(), 'Соберите бургер')]")
    ORDER_FEED_HEADER = (By.XPATH, "//h1[contains(text(), 'Лента заказов')]")

    # --- Ингредиенты и модальное окно ---
    INGREDIENT_CARD = (By.XPATH, "(//a[contains(@class, 'BurgerIngredient_ingredient')])[2]")
    MODAL_WINDOW = (By.XPATH, "//div[contains(@class, 'Modal_modal__content')]")
    MODAL_CLOSE_BUTTON = (By.CSS_SELECTOR, "button.Modal_modal__close_modified__3V5XS")
    COUNTER = (By.CSS_SELECTOR, "p.counter_counter__num__3nue1")
    # --- Оформление заказа ---
    CHECKOUT_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
    ORDER_NUMBER_IN_MODAL = (By.XPATH, "//h2[contains(@class, 'Modal_modal__title')]")


class ConstructorLocators:
    CONSTRUCTOR_LINK = (By.XPATH, "//a[@href='/']")
    LOGO = (By.XPATH, "//a[@href='/']")
    BUNS_TAB = (By.XPATH, "//div[.//span[normalize-space()='Булки']]")
    SAUCES_TAB = (By.XPATH, "//span[normalize-space()='Соусы']")
    FILLINGS_TAB = (By.XPATH, "//span[normalize-space()='Начинки']")


class AccountLocators:
    LOGOUT_BUTTON = (By.XPATH, "//button[@type='button' and normalize-space(.)='Выход']")
    ACCOUNT_TEXT = (By.XPATH, "//*[contains(normalize-space(), 'Личный кабинет')]")


class OrderFeedLocators:
    # Счетчики в ленте. Ищем параграфы, содержащие текст "Выполнено", и берем следующий за ними
    TOTAL_ORDERS = (By.XPATH, "//p[contains(text(), 'Выполнено за все время')]/following-sibling::p")
    TODAY_ORDERS = (By.XPATH, "//p[contains(text(), 'Выполнено за сегодня')]/following-sibling::p")

    # Заказы в статусе "В работе" (лента)
    IN_PROGRESS_ORDERS = (By.XPATH, "//ul[contains(@class, 'OrderFeed_orderListReady')]/li")