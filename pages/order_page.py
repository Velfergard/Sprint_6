from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import order_page_locators
from pages.base_page import BasePage
from data import urls
import allure

class OrderPage(BasePage):

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Ожидаем загрузку страницы оформления заказа")
    def wait_page_changed_to_order_page(self):
        WebDriverWait(self.driver, 5).until(EC.url_contains('order'))

    @allure.step("Проверяем, что текущая страница - страница оформления заказа")
    def check_current_page_is_order(self):
        assert self.driver.current_url == urls.order_url

    @allure.step("Вводим имя")
    def input_name(self, name):
        self.driver.find_element(*order_page_locators.INPUT_NAME).send_keys(name)

    @allure.step("Вводим фамилию")
    def input_surname(self, surname):
        self.driver.find_element(*order_page_locators.INPUT_SURNAME).send_keys(surname)

    @allure.step("Вводим адрес")
    def input_address(self, address):
        self.driver.find_element(*order_page_locators.INPUT_ADDRESS).send_keys(address)

    @allure.step("Выбираем станцию метро")
    def input_subway(self):
        subway_fld = self.driver.find_element(*order_page_locators.INPUT_SUBWAY).click()
        self.driver.find_element(*order_page_locators.CHOOSE_SUBWAY).click()

    @allure.step("Вводим номер телефона")
    def input_phone(self, phone):
        self.driver.find_element(*order_page_locators.INPUT_PHONE_NUMBER).send_keys(phone)

    @allure.step("Нажимаем кнопку 'Далее'")
    def click_on_continue_button(self):
        self.driver.find_element(*order_page_locators.BUTTON_CONTINUE).click()
        WebDriverWait(self.driver, 5).until(EC.text_to_be_present_in_element
                                            (order_page_locators.ORDER_FORM_HEADER, 'Про аренду'))

    @allure.step("Сценарий заполнения первой формы с данными для заказа")
    def fill_out_first_order_form(self, name, surname, address, phone):
        self.wait_page_changed_to_order_page()
        self.input_name(name)
        self.input_surname(surname)
        self.input_address(address)
        self.input_subway()
        self.input_phone(phone)
        self.click_on_continue_button()

    @allure.step("Вводим дату доставки")
    def input_delivery_date(self, delivery_date):
        self.driver.find_element(*order_page_locators.DELIVERY_DATE).send_keys(delivery_date)

    @allure.step("Выбираем срок аренды самоката")
    def choose_rent_period_from_dropdown(self):
        self.driver.find_element(*order_page_locators.RENT_PERIOD).click()
        self.driver.find_element(*order_page_locators.DROPDOWN_PERIOD).click()

    @allure.step("Выбираем цвет самоката")
    def choose_scooter_color(self, color):
        self.driver.find_element(*color).click()

    @allure.step("Вводим комментарий к заказу")
    def input_comment(self, comment):
        self.driver.find_element(*order_page_locators.INPUT_COMMENT).send_keys(comment)

    @allure.step("Нажимаем кнопку 'Заказать' для завершения оформления заказа")
    def click_on_order_button(self):
        self.driver.find_element(*order_page_locators.MAKE_ORDER_BUTTON).click()

    @allure.step("Нажимаем кнопку 'Да' для подтверждения заказа")
    def confirm_order(self):
        self.driver.find_element(*order_page_locators.BUTTON_YES).click()

    @allure.step("Проверяем заголовок окна об успешном оформлении заказа")
    def check_confirmation_message(self):
        confirmation_header = self.driver.find_element(*order_page_locators.CONFIRM_ORDER_HEADER).text

        assert 'Заказ оформлен' in confirmation_header

    @allure.step("Сценарий заполнения второй формы с данными для заказа")
    def fill_out_second_order_form(self, delivery_date, color, comment):
        self.input_delivery_date(delivery_date)
        self.choose_rent_period_from_dropdown()
        self.choose_scooter_color(color)
        self.input_comment(comment)
        self.click_on_order_button()
        self.confirm_order()

    @allure.step("Сценарий оформления заказа")
    def make_order(self, name, surname, address, phone, delivery_date, color, comment):
        self.fill_out_first_order_form(name, surname, address, phone)
        self.fill_out_second_order_form(delivery_date, color, comment)
