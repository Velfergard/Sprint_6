from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import main_page_locators
from locators import base_page_locators
from data import urls
import allure


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Открываем ресурс {url}")
    def go_to_site(self, url):
        self.driver.get(url)
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(main_page_locators.SCOOTER_IMG))

    @allure.step("Нажимаем кнопку 'Заказать' в хэдере страницы")
    def click_header_order_button(self):
        self.driver.find_element(*base_page_locators.ORDER_BUTTON_HEADER).click()

    @allure.step("Нажимаем на логотип 'Самокат'")
    def click_on_scooter_logo(self):
        self.driver.find_element(*base_page_locators.SCOOTER_LOGO).click()

    @allure.step("Проверяем, что текущая страница - главная страница Самоката")
    def check_current_page_is_scooter(self):
        assert WebDriverWait(self.driver, 5).until(EC.url_to_be(urls.scooter_url))

    @allure.step("Сценарий проверки перехода по логотипу 'Самокат'")
    def check_scooter_logo_transition(self):
        self.click_on_scooter_logo()
        self.check_current_page_is_scooter()

    @allure.step("Нажимаем на логотип 'Яндекс'")
    def click_on_yandex_logo(self):
        self.driver.find_element(*base_page_locators.YANDEX_LOGO).click()

    @allure.step("Переключаемся на открывшуюся вкладку")
    def switch_to_dzen_window(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    @allure.step("Проверяем, что текущая страница - главная страница Дзена")
    def check_current_page_is_dzen(self):
        assert WebDriverWait(self.driver, 7).until(EC.url_contains(urls.dzen_url))

    @allure.step("Сценарий проверки перехода по логотипу 'Яндекс'")
    def check_yandex_logo_transition(self):
        self.click_on_yandex_logo()
        self.switch_to_dzen_window()
        self.check_current_page_is_dzen()
