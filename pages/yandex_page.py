import time

from pages.base_page import BasePage
from locators.yandex_page_locators import YandexPageLocators as Locators


class YandexPage(BasePage):

    def fill_search_and_submit(self):
        search_text = 'Planet for me'
        self.driver.switch_to.frame(0)
        self.element_is_visible(Locators.SEARCH_INPUT).send_keys(search_text)
        self.driver.switch_to.default_content()
        self.driver.execute_script("arguments[0].click();", self.element_is_clickable(Locators.SEARCH_BUTTON))

    def search_result(self):
        time.sleep(1)
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[1])
        search_list = self.elements_are_visible(Locators.SEARCH_RESULTS)
        result_links = [i.get_attribute('href') for i in search_list]
        return result_links
