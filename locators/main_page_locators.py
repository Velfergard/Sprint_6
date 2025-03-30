from selenium.webdriver.common.by import By


# Локаторы для секции с вопросами
QUESTIONS_SECTION = [By.CLASS_NAME, 'accordion']  # Секция "Вопросы о важном"
QUESTION_ONE = [By.ID, 'accordion__heading-0']  # Вопрос "Сколько это стоит? И как оплатить?"
QUESTION_TWO = [By.ID, 'accordion__heading-1']  # Вопрос "Хочу сразу несколько самокатов! Так можно?"
QUESTION_THREE = [By.ID, 'accordion__heading-2']  # Вопрос "Как расчитывается время аренды?"
QUESTION_FOUR = [By.ID, 'accordion__heading-3']  # Вопрос "Можно ли заказать самокат прямо на сегодня?"
QUESTION_FIVE = [By.ID, 'accordion__heading-4']  # Вопрос "СМожно ли продлить заказ или вернуть самокат раньше?"
QUESTION_SIX = [By.ID, 'accordion__heading-5']  # Вопрос "Вы привозите зарядку вместе с самокатом?"
QUESTION_SEVEN = [By.ID, 'accordion__heading-6']  # Вопрос "Можно ли отменить заказ?"
QUESTION_EIGHT = [By.ID, 'accordion__heading-7']  # Вопрос "Я жизу за МКАДом, привезёте?"

ANSWER_ONE = [By.CSS_SELECTOR, '#accordion__panel-0 > p']  # Текст ответа на вопрос по локатору QUESTION_ONE
ANSWER_TWO = [By.CSS_SELECTOR, '#accordion__panel-1 > p']  # Текст ответа на вопрос по локатору QUESTION_TWO
ANSWER_THREE = [By.CSS_SELECTOR, '#accordion__panel-2 > p']  # Текст ответа на вопрос по локатору QUESTION_THREE
ANSWER_FOUR = [By.CSS_SELECTOR, '#accordion__panel-3 > p']  # Текст ответа на вопрос по локатору QUESTION_FOUR
ANSWER_FIVE = [By.CSS_SELECTOR, '#accordion__panel-4 > p']  # Текст ответа на вопрос по локатору QUESTION_FIVE
ANSWER_SIX = [By.CSS_SELECTOR, '#accordion__panel-5 > p']  # Текст ответа на вопрос по локатору QUESTION_SIX
ANSWER_SEVEN = [By.CSS_SELECTOR, '#accordion__panel-6 > p']  # Текст ответа на вопрос по локатору QUESTION_SEVEN
ANSWER_EIGHT = [By.CSS_SELECTOR, '#accordion__panel-7 > p']  # Текст ответа на вопрос по локатору QUESTION_EIGHT

# Локатор для кнопки "Заказать"
ORDER_BUTTON_ROADMAP = [By.XPATH, '//div[contains(@class, "RoadMap")]//button[text() = "Заказать"]']  # Кнопка "Заказать" в блоке "Как это работает"

# Локатор для картинки самоката
SCOOTER_IMG = [By.XPATH, '//img[contains(@alt, "blueprint")]']  # Картинка с примером самоката
