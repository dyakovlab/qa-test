import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from appium import webdriver as appium_webdriver


@pytest.fixture()
def web_driver():
    driver_service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=driver_service)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture()
def mobile_driver():
    desired_capabilities = {
        'platformName': 'Android',
    }
    driver = appium_webdriver.Remote('http://localhost:4723/wd/hub', desired_capabilities)
    yield driver
    driver.quit()
