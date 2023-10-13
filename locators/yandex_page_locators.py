from selenium.webdriver.common.by import By


class YandexPageLocators:
    SEARCH_INPUT = (By.XPATH, "//input[@class='arrow__input mini-suggest__input']")
    SEARCH_BUTTON = (By.XPATH, "//button[@type='submit']")
    SEARCH_RESULTS = (By.XPATH, "//*[@id='search-result']/li/div/div/div[not(@class='MissingWords')]/a")
