from apps.planetforme_app import PlanetformeApp


class TestMobileUI:

    def test_search(self, mobile_driver):
        search_string = 'Москва'
        planetforme_app = PlanetformeApp(mobile_driver)
        planetforme_app.open_app()
        planetforme_app.log_in()
        planetforme_app.fill_search_and_submit(search_string)
        search_result = planetforme_app.search_result()
        search_result_string = ' '.join(map(str, search_result)).lower()
        assert search_string.lower() in search_result_string, 'Search result not contains ' + search_string
