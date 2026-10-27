import allure
import time
from pages.main_page import MainPage


@allure.feature("Основная функциональность")
class TestMainFunctionality:
    """Тесты основной функциональности главной страницы"""

    @allure.title("Переход по клику на «Конструктор»")
    def test_go_to_constructor(self, driver):
        main_page = MainPage(driver)
        main_page.click_constructor()
        # Проверяем, что открылся конструктор (метод внутри Page-объекта)
        assert main_page.is_constructor_opened()

    @allure.title("Переход по клику на «Лента заказов»")
    def test_go_to_order_feed(self, driver):
        main_page = MainPage(driver)
        main_page.click_order_feed()
        # Проверяем, что открылась лента заказов
        assert main_page.is_order_feed_opened()

    @allure.title("Клик на ингредиент открывает всплывающее окно")
    def test_click_ingredient_opens_modal(self, driver):
        main_page = MainPage(driver)
        main_page.click_ingredient()
        # Проверяем, что модалка видна
        assert main_page.is_modal_opened()

    @allure.title("Закрытие всплывающего окна по крестику")
    def test_close_modal(self, driver):
        main_page = MainPage(driver)
        main_page.click_ingredient()
        main_page.close_modal()
        # Ждем, пока модалка исчезнет, и проверяем это
        assert main_page.is_modal_closed()

    @allure.title("Увеличение счётчика ингредиента при добавлении")
    def test_counter_increases(self, driver):
        main_page = MainPage(driver)
        # Берем текст счетчика до
        counter_before = int(main_page.get_counter_text())

        # Кликаем на соус и добавляем в заказ
        main_page.click_ingredient()
        # Закрываем модалку
        main_page.close_modal()

        # Небольшая пауза, чтобы счетчик успел обновиться
        time.sleep(1)

        # Берем текст счетчика после
        counter_after = int(main_page.get_counter_text())

        assert counter_after > counter_before