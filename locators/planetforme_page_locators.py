from selenium.webdriver.common.by import By


class PlanetForMeLocators:
    SEARCH_INPUT = (By.XPATH, "//input[@data-qa='navbar-search-input']")
    SEARCH_RESULTS = (By.XPATH, "//p[@data-qa='search-item-description']")
