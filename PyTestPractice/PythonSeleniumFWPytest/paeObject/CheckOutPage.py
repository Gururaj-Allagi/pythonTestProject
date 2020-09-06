from selenium.webdriver.common.by import By


class CheckOutPage:
    def __init__(self, driver):
        self.driver = driver

    cardTitle = (By.XPATH, "//div[@class='card h-100']")
    checkOut = (By.XPATH, "//a[@class='nav-link btn btn-primary']")

    def getCardTitles(self):
        return self.driver.find_elements(*CheckOutPage.cardTitle)

    def checkOutItems(self):
        return self.driver.find_elements(*CheckOutPage.checkOut)