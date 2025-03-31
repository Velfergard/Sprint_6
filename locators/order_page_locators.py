from selenium.webdriver.common.by import By
import random


# Локаторы страницы оформления заказа
INPUT_NAME = [By.XPATH, '//input[contains(@placeholder, "Имя")]']  # Поле ввода имени
INPUT_SURNAME = [By.XPATH, '//input[contains(@placeholder, "Фамилия")]']  # Поле ввода фамилии
INPUT_ADDRESS = [By.XPATH, '//input[contains(@placeholder, "Адрес")]']  # Поле ввода адреса доставки
INPUT_SUBWAY = [By.XPATH, '//input[contains(@placeholder, "Станция метро")]']  # Поле ввода станции метро
CHOOSE_SUBWAY = [By.XPATH, f'//div[contains(@class, "__select")]//li[{random.randint(1,5)}]/button']  # Выбор станции метро из выпадающего списка
INPUT_PHONE_NUMBER = [By.XPATH, '//input[contains(@placeholder, "Телефон")]']  # Поле ввода номера телефона
BUTTON_CONTINUE = [By.XPATH, '//button[text() = "Далее"]']  # Кнопка "Далее"

ORDER_FORM_HEADER = [By.XPATH, '//div[contains(@class, "Order_Header")]']  # Заголовок формы заказа
DELIVERY_DATE = [By.XPATH, '//input[contains(@placeholder, "Когда")]']  # Поле ввода даты доставки
RENT_PERIOD = [By.XPATH, '//div/span']  # Кнопка выпадающего меню для срока аренды
DROPDOWN_PERIOD = [By.XPATH, f'//div[@class = "Dropdown-menu"]/div[{random.randint(1,7)}]']  # Выпадающее меню с периодами аренды
BLACK_COLOR = [By.XPATH, '//input[@id = "black"]']  # Чек-бокс цвета "чёрный жемчуг"
GREY_COLOR = [By.XPATH, '//input[@id = "grey"]']  # Чек-бокс цвета "серая безысходность"
INPUT_COMMENT = [By.XPATH, '//input[contains(@placeholder, "Комментарий")]']  # Поле ввода комментария к заказу
MAKE_ORDER_BUTTON = [By.XPATH, '//button[contains(@class, "Middle") and text() = "Заказать"]']  # Кнопка "Заказать"
CONFIRM_ORDER_HEADER = [By.XPATH, '//div[contains(@class, "ModalHeader") and text() = "Заказ оформлен"]']  # Заголовок окна с подтверждением заказа
BUTTON_YES = [By.XPATH, '//button[text() = "Да"]']  # Кнопка "Да" в окне подтверждения заказа
BUTTON_CHECK_STATUS = [By.XPATH, '//button[text() = "Посмотреть статус"]']  # Кнопка "Посмотреть статус"
