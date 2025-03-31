import pytest
from selenium import webdriver


@pytest.fixture(autouse=True)
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()
