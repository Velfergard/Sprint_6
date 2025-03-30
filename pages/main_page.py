from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import main_page_locators
from data import answers
import allure


class MainPage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Пролистываем страницу до кнопки 'Заказать' в блоке 'Как это работает'")
    def scroll_page_to_order_button(self):
        order_button = self.driver.find_element(*main_page_locators.ORDER_BUTTON_ROADMAP)
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(main_page_locators.ORDER_BUTTON_ROADMAP))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", order_button)

    @allure.step("Нажимаем на кнопку 'Заказать'")
    def click_roadmap_order_button(self):
        order_button = self.driver.find_element(*main_page_locators.ORDER_BUTTON_ROADMAP)
        self.driver.execute_script("arguments[0].click();", order_button)

    @allure.step("Пролистываем страницу до блока 'Вопросы о важном'")
    def scroll_page_to_questions_section(self):
        questions_section = self.driver.find_element(*main_page_locators.QUESTIONS_SECTION)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", questions_section)

    @allure.step("Нажимаем на 1 вопрос и проверяем текст ответа")
    def check_question_one_answer(self):
        question = self.driver.find_element(*main_page_locators.QUESTION_ONE)
        self.driver.execute_script("arguments[0].click();", question)
        answer = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(main_page_locators.ANSWER_ONE)).text

        assert answer == answers.answer_one

    @allure.step("Нажимаем на 2 вопрос и проверяем текст ответа")
    def check_question_two_answer(self):
        question = self.driver.find_element(*main_page_locators.QUESTION_TWO)
        self.driver.execute_script("arguments[0].click();", question)
        answer = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(main_page_locators.ANSWER_TWO)).text

        assert answer == answers.answer_two

    @allure.step("Нажимаем на 3 вопрос и проверяем текст ответа")
    def check_question_three_answer(self):
        question = self.driver.find_element(*main_page_locators.QUESTION_THREE)
        self.driver.execute_script("arguments[0].click();", question)
        answer = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(main_page_locators.ANSWER_THREE)).text

        assert answer == answers.answer_three

    @allure.step("Нажимаем на 4 вопрос и проверяем текст ответа")
    def check_question_four_answer(self):
        question = self.driver.find_element(*main_page_locators.QUESTION_FOUR)
        self.driver.execute_script("arguments[0].click();", question)
        answer = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(main_page_locators.ANSWER_FOUR)).text

        assert answer == answers.answer_four

    @allure.step("Нажимаем на 5 вопрос и проверяем текст ответа")
    def check_question_five_answer(self):
        question = self.driver.find_element(*main_page_locators.QUESTION_FIVE)
        self.driver.execute_script("arguments[0].click();", question)
        answer = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(main_page_locators.ANSWER_FIVE)).text

        assert answer == answers.answer_five

    @allure.step("Нажимаем на 6 вопрос и проверяем текст ответа")
    def check_question_six_answer(self):
        question = self.driver.find_element(*main_page_locators.QUESTION_SIX)
        self.driver.execute_script("arguments[0].click();", question)
        answer = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(main_page_locators.ANSWER_SIX)).text

        assert answer == answers.answer_six

    @allure.step("Нажимаем на 7 вопрос и проверяем текст ответа")
    def check_question_seven_answer(self):
        question = self.driver.find_element(*main_page_locators.QUESTION_SEVEN)
        self.driver.execute_script("arguments[0].click();", question)
        answer = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(main_page_locators.ANSWER_SEVEN)).text

        assert answer == answers.answer_seven

    @allure.step("Нажимаем на 8 вопрос и проверяем текст ответа")
    def check_question_eight_answer(self):
        question = self.driver.find_element(*main_page_locators.QUESTION_EIGHT)
        self.driver.execute_script("arguments[0].click();", question)
        answer = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(main_page_locators.ANSWER_EIGHT)).text

        assert answer == answers.answer_eight
