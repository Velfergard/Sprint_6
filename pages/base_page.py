from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import main_page_locators
from data import urls
import allure


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Открываем ресурс {url}")
    def go_to_site(self, url):
        self.driver.get(url)
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(main_page_locators.SCOOTER_IMG))

    @allure.step("Переключаемся на открывшуюся вкладку")
    def switch_to_dzen_window(self):
        self.driver.switch_to.window(self.driver.window_handles[1])
