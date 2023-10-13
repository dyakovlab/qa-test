
class BaseApp:
    def __init__(self, driver):
        self.driver = driver
    # def element_is_clickable(self, locator, timeout=5):
    #    return Wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    # def elements_are_visible(self, locator, timeout=5):
    #    return Wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))
