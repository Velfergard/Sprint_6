from locators import order_page_locators
from pages.order_page import OrderPage
from pages.main_page import MainPage
from selenium import webdriver
from data import urls
import helpers
import pytest
import allure


class TestOrderPage:
    test_data = [
        (
            helpers.gen_test_data_one(),
            [*order_page_locators.BLACK_COLOR]
         ),
        (
            helpers.gen_test_data_two(),
            [*order_page_locators.GREY_COLOR]
        )
    ]

    @allure.title("Проверка оформления заказа с заданными параметрами")
    @allure.description("Позитивный сценарий оформления заказа с заданными параметрами."
                        "Точка входа: - кнопка 'Заказать' в хэдере страницы.")
    @pytest.mark.parametrize('dataset,color', test_data)
    def test_order_from_header_button(self, driver, dataset, color):
        order_page = OrderPage(driver)
        main_page = MainPage(driver)

        main_page.go_to_site(urls.scooter_url)
        main_page.click_header_order_button()
        order_page.make_order(dataset["name"], dataset["surname"], dataset["address"], dataset["phone"],
                              dataset["delivery_date"], color, dataset["comment"])

        order_page.check_confirmation_message()
