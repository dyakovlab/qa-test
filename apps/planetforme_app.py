from appium.webdriver.common.appiumby import AppiumBy

from apps.base_app import BaseApp
from locators.planetforme_app_locators import PlanetForMeLocators as Locators


class PlanetformeApp(BaseApp):

    def open_app(self):
        self.driver.start_activity('com.planet.forme', ".ui.activities.main.MainActivity")

    def log_in(self):
        self.driver.implicitly_wait(20)
        self.driver.find_element(AppiumBy.ID, Locators.LOGIN_TAB_BUTTON).click()
        self.driver.find_element(AppiumBy.ID, Locators.LOGIN_INPUT).send_keys('melnikova3552')
        self.driver.find_element(AppiumBy.ID, Locators.PASSWORD_INPUT).send_keys('"njvjzdtxthbyrf')
        self.driver.find_element(AppiumBy.ID, Locators.LOGIN_BUTTON).click()

    def fill_search_and_submit(self, search):
        self.driver.implicitly_wait(20)
        self.driver.find_element(AppiumBy.ID, Locators.SEARCH_TAB_BUTTON).click()
        self.driver.find_element(AppiumBy.ID, Locators.SEARCH_INPUT).send_keys(search + '\n')

    def search_result(self):
        self.driver.implicitly_wait(20)
        search_list = self.driver.find_elements(AppiumBy.ID, Locators.SEARCH_RESULTS)
        result_text = [element.text for element in search_list]
        return result_text
