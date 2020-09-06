from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR, "a[href*='shop']")

    def shopItems(self):
        # * is user de serialization
        # * is convert is this form self.driver.find_element_by_css_selector("a[href*='shop']").click()
        return self.driver.find_element(*HomePage.shop)
