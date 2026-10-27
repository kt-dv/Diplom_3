import pytest
from selenium import webdriver
from config import Urls
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    if request.param == "chrome":
        options = ChromeOptions()
        # Отключаем автоматизацию, чтобы сайт не блокировал
        options.add_argument("--disable-blink-features=AutomationControlled")
        driver = webdriver.Chrome(options=options)
    elif request.param == "firefox":
        options = FirefoxOptions()
        driver = webdriver.Firefox(options=options)

    # Устанавливаем таймаут на загрузку страницы (30 секунд)
    driver.set_page_load_timeout(30)
    # Неявное ожидание для поиска элементов
    driver.implicitly_wait(10)
    # Разворачиваем окно на весь экран
    driver.maximize_window()

    try:
        driver.get(Urls.BASE_URL)
    except Exception as e:
        print(f"Ошибка при загрузке страницы: {e}")
        driver.quit()
        raise

    yield driver
    driver.quit()