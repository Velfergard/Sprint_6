from selenium.webdriver.common.by import By


# Локаторы для элементов в хэдере страницы
YANDEX_LOGO = [By.XPATH, '//a[contains(@class, "Yandex")]']  # Логотип "Яндекс"
SCOOTER_LOGO = [By.XPATH, '//a[contains(@class, "Scooter")]']  # Логотип "Самокат"
ORDER_BUTTON_HEADER = [By.XPATH, '//div[contains(@class, "Nav")]/button[text() = "Заказать"]']  # Кнопка "Заказать" в хэдере страницы
