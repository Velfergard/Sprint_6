from pages.order_page import OrderPage
from pages.main_page import MainPage
from selenium import webdriver
from data import urls
import pytest
import allure


class TestTransitions:

    @allure.title("Проверка перехода по кнопке 'Заказать' в хэдэре страницы")
    @allure.description("Сценарий перехода по кнопке 'Заказать' в хэдэре на страницу /order.")
    def test_header_order_button(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        main_page.go_to_site(urls.scooter_url)
        main_page.click_header_order_button()
        order_page.wait_page_changed_to_order_page()
        order_page.check_current_page_is_order()

    @allure.title("Проверка перехода по кнопке 'Заказать' в блоке 'Как это работает'")
    @allure.description("Сценарий перехода по кнопке 'Заказать' в блоке 'Как это работает' на страницу /order.")
    def test_roadmap_order_button(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        main_page.go_to_site(urls.scooter_url)
        main_page.scroll_page_to_order_button()
        main_page.click_roadmap_order_button()
        order_page.wait_page_changed_to_order_page()
        order_page.check_current_page_is_order()

    @allure.title("Проверка перехода по логотипу 'Самокат'")
    @allure.description("Сценарий возврата на главную страницу с помощью логотипа 'Самокат' со страницы /order.")
    def test_scooter_logo_transition(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        main_page.go_to_site(urls.scooter_url)
        main_page.click_header_order_button()
        order_page.wait_page_changed_to_order_page()
        main_page.click_on_scooter_logo()
        main_page.check_scooter_logo_transition()

    @allure.title("Проверка перехода по логотипу 'Яндекс'")
    @allure.description("Сценарий перехода на главную страницу сервиса 'Дзен' с помощью логотипа 'Яндекс'.1")
    def test_yandex_logo_transition(self, driver):
        main_page = MainPage(driver)

        main_page.go_to_site(urls.scooter_url)
        main_page.check_yandex_logo_transition()
