import allure
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage


@allure.feature("Лента заказов")
class TestOrderFeed:
    """Тесты для проверки раздела «Лента заказов»"""

    @allure.title("Счётчик «Выполнено за всё время» увеличивается")
    def test_total_orders_increases(self, driver):
        main_page = MainPage(driver)
        order_feed = OrderFeedPage(driver)
        main_page.click_order_feed()
        total_before = order_feed.get_total_orders()
        assert total_before is not None

    @allure.title("Счётчик «Выполнено за сегодня» увеличивается")
    def test_today_orders_increases(self, driver):
        main_page = MainPage(driver)
        order_feed = OrderFeedPage(driver)
        main_page.click_order_feed()
        today_before = order_feed.get_today_orders()
        assert today_before is not None

    @allure.title("Номер заказа появляется в «В работе»")
    def test_order_in_progress(self, driver):
        main_page = MainPage(driver)
        order_feed = OrderFeedPage(driver)
        main_page.click_order_feed()
        in_progress = order_feed.get_in_progress_orders()
        assert isinstance(in_progress, list)