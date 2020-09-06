import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from PyTestPractice.PythonSeleniumFWPytest.paeObject.CheckOutPage import CheckOutPage
from PyTestPractice.PythonSeleniumFWPytest.paeObject.HomePage import HomePage
from PyTestPractice.PythonSeleniumFWPytest.utilities.BaseClass import BaseClass


# @pytest.mark.usefixtures("setup")
class TestOne(BaseClass):

    def test_e2e(self):

        homePage = HomePage(self.driver)
        checkOutPage = CheckOutPage(self.driver)

        homePage.shopItems().click()

        products = checkOutPage.getCardTitles()

        wait = WebDriverWait(self.driver, 7)

        # //div[@class='card h-100']/div/h4/a
        # product =//div[@class='card h-100']
        for product in products:
            productName = product.find_element_by_xpath("div/h4/a").text
            if productName == "Blackberry":
                # Add item into cart
                product.find_element_by_xpath("div/button").click()

        checkOutPage.checkOutItems().click()

        self.driver.find_element_by_id("country").send_keys("ind")
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
        self.driver.find_element_by_link_text("India").click()
        self.driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()
        self.driver.find_element_by_css_selector("[type='submit']").click()
        successText = self.driver.find_element_by_class_name("alert-success").text

        assert "Success! Thank you!" in successText

        # driver.get_screenshot_as_file("screen.png")
