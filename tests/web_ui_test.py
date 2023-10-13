from pages.yandex_page import YandexPage

from pages.planetforme_page import PlanetForMePage


class TestWebUI:

    def test_search(self, web_driver):
        planetforme_link = 'https://planetfor.me/'

        yandex_page = YandexPage(web_driver, 'https://www.yandex.ru')
        yandex_page.open()
        yandex_page.fill_search_and_submit()
        yandex_links = yandex_page.search_result()
        assert planetforme_link in yandex_links, 'Search result not contains https://planetfor.me/'

        planetforme_page = PlanetForMePage(web_driver, planetforme_link)
        planetforme_page.open()
        planetforme_page.fill_search_and_submit()
        planetforme_elements = planetforme_page.search_result()
        planetforme_elements_string = ' '.join(map(str, planetforme_elements)).lower()
        assert 'qa' in planetforme_elements_string, 'Search result not contains qa'
