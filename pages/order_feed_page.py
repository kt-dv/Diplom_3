from pages.base_page import BasePage
from locators import OrderFeedLocators
import allure


class OrderFeedPage(BasePage):
    """Класс для страницы «Лента заказов»"""

    @allure.step("Получение количества заказов за всё время")
    def get_total_orders(self):
        return int(self.get_text(OrderFeedLocators.TOTAL_ORDERS))

    @allure.step("Получение количества заказов за сегодня")
    def get_today_orders(self):
        return int(self.get_text(OrderFeedLocators.TODAY_ORDERS))

    @allure.step("Получение списка заказов в работе")
    def get_in_progress_orders(self):
        # Используем метод find_elements из BasePage
        elements = self.find_elements(OrderFeedLocators.IN_PROGRESS_ORDERS)
        return [el.text for el in elements]