from pages.main_page import MainPage
from pages.base_page import BasePage
from selenium import webdriver
from data import urls
import allure


class TestMainPage:

    @allure.title("Проверка текста ответа на первый вопрос")
    @allure.description("Сценарий проверки текста ответа на первый вопрос."
                        "На главной странице 'Самоката' ищем блок 'Вопросы о важном' и нажимаем на вопрос.")
    def test_question_one_answer(self, driver):
        main_page = MainPage(driver)
        base_page = BasePage(driver)

        base_page.go_to_site(urls.scooter_url)
        main_page.scroll_page_to_questions_section()
        main_page.check_question_one_answer()

    @allure.title("Проверка текста ответа на второй вопрос")
    @allure.description("Сценарий проверки текста ответа на второй вопрос."
                        "На главной странице 'Самоката' ищем блок 'Вопросы о важном' и нажимаем на вопрос.")
    def test_question_two_answer(self, driver):
        main_page = MainPage(driver)
        base_page = BasePage(driver)

        base_page.go_to_site(urls.scooter_url)
        main_page.scroll_page_to_questions_section()
        main_page.check_question_two_answer()

    @allure.title("Проверка текста ответа на третий вопрос")
    @allure.description("Сценарий проверки текста ответа на третий вопрос."
                        "На главной странице 'Самоката' ищем блок 'Вопросы о важном' и нажимаем на вопрос.")
    def test_question_three_answer(self, driver):
        main_page = MainPage(driver)
        base_page = BasePage(driver)

        base_page.go_to_site(urls.scooter_url)
        main_page.scroll_page_to_questions_section()
        main_page.check_question_three_answer()

    @allure.title("Проверка текста ответа на четвертый вопрос")
    @allure.description("Сценарий проверки текста ответа на четвертый вопрос."
                        "На главной странице 'Самоката' ищем блок 'Вопросы о важном' и нажимаем на вопрос.")
    def test_question_four_answer(self, driver):
        main_page = MainPage(driver)
        base_page = BasePage(driver)

        base_page.go_to_site(urls.scooter_url)
        main_page.scroll_page_to_questions_section()
        main_page.check_question_four_answer()

    @allure.title("Проверка текста ответа на пятый вопрос")
    @allure.description("Сценарий проверки текста ответа на пятый вопрос."
                        "На главной странице 'Самоката' ищем блок 'Вопросы о важном' и нажимаем на вопрос.")
    def test_question_five_answer(self, driver):
        main_page = MainPage(driver)
        base_page = BasePage(driver)

        base_page.go_to_site(urls.scooter_url)
        main_page.scroll_page_to_questions_section()
        main_page.check_question_five_answer()

    @allure.title("Проверка текста ответа на шестой вопрос")
    @allure.description("Сценарий проверки текста ответа на шестой вопрос."
                        "На главной странице 'Самоката' ищем блок 'Вопросы о важном' и нажимаем на вопрос.")
    def test_question_six_answer(self, driver):
        main_page = MainPage(driver)
        base_page = BasePage(driver)

        base_page.go_to_site(urls.scooter_url)
        main_page.scroll_page_to_questions_section()
        main_page.check_question_six_answer()

    @allure.title("Проверка текста ответа на седьмой вопрос")
    @allure.description("Сценарий проверки текста ответа на седьмой вопрос."
                        "На главной странице 'Самоката' ищем блок 'Вопросы о важном' и нажимаем на вопрос.")
    def test_question_seven_answer(self, driver):
        main_page = MainPage(driver)
        base_page = BasePage(driver)

        base_page.go_to_site(urls.scooter_url)
        main_page.scroll_page_to_questions_section()
        main_page.check_question_seven_answer()

    @allure.title("Проверка текста ответа на восьмой вопрос")
    @allure.description("Сценарий проверки текста ответа на восьмой вопрос."
                        "На главной странице 'Самоката' ищем блок 'Вопросы о важном' и нажимаем на вопрос.")
    def test_question_eight_answer(self, driver):
        main_page = MainPage(driver)
        base_page = BasePage(driver)

        base_page.go_to_site(urls.scooter_url)
        main_page.scroll_page_to_questions_section()
        main_page.check_question_eight_answer()
