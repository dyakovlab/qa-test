from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
from locators.planetforme_page_locators import PlanetForMeLocators as Locators


class PlanetForMePage(BasePage):

    def fill_search_and_submit(self):
        search_text = 'qa'
        self.element_is_visible(Locators.SEARCH_INPUT).send_keys(search_text)
        self.element_is_visible(Locators.SEARCH_INPUT).send_keys(Keys.RETURN)

    def search_result(self):
        search_elements = self.elements_are_visible(Locators.SEARCH_RESULTS)
        result_elements = [i.text for i in search_elements]
        return result_elements
