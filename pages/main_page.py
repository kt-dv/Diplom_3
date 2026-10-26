from pages.base_page import BasePage
from locators import MainPageLocators
import allure


class MainPage(BasePage):
    """Класс для главной страницы Stellar Burgers"""

    @allure.step("Клик на кнопку «Конструктор»")
    def click_constructor(self):
        self.click_element(MainPageLocators.CONSTRUCTOR_BUTTON)

    @allure.step("Клик на кнопку «Лента заказов»")
    def click_order_feed(self):
        self.click_element(MainPageLocators.ORDER_FEED_BUTTON)

    @allure.step("Клик на ингредиент")
    def click_ingredient(self):
        self.click_element(MainPageLocators.INGREDIENT_CARD)

    @allure.step("Закрытие модального окна")
    def close_modal(self):
        self.click_element(MainPageLocators.MODAL_CLOSE_BUTTON)

    @allure.step("Получение текста счётчика ингредиента")
    def get_counter_text(self):
        # Ищем все элементы счетчика на странице, используя метод из BasePage
        counters = self.find_elements(MainPageLocators.COUNTER)
        for counter in counters:
            # Если элемент видим и содержит цифру — возвращаем его текст
            if counter.is_displayed() and counter.text.strip():
                return counter.text
        return "0"

    @allure.step("Клик на кнопку «Оформить заказ»")
    def click_checkout(self):
        self.click_element(MainPageLocators.CHECKOUT_BUTTON)

    @allure.step("Получение номера заказа из модального окна")
    def get_order_number(self):
        return self.get_text(MainPageLocators.ORDER_NUMBER_IN_MODAL)
    @allure.step("Проверка, что открыт Конструктор")
    def is_constructor_opened(self):
        return self.find_element(MainPageLocators.CONSTRUCTOR_HEADER).is_displayed()

    @allure.step("Проверка, что открыта Лента заказов")
    def is_order_feed_opened(self):
        return self.find_element(MainPageLocators.ORDER_FEED_HEADER).is_displayed()