from selenium import webdriver


def headLessBrowser(url):
    chrome_Option = webdriver.ChromeOptions()
    chrome_Option.add_argument("headless")

    driver = webdriver.Chrome(options=chrome_Option)
    driver.maximize_window()
    driver.get(url)