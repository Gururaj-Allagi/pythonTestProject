from selenium import webdriver

chrome_Option = webdriver.ChromeOptions()
chrome_Option.add_argument("headless")

try:
    driver = webdriver.Chrome(options=chrome_Option)
    driver.maximize_window()

except:
    print("except")

else:
    print("else")

finally:
    print("finally")

driver.get("https://github.com/Gururaj-Allagi")
print(driver.title)
driver.close()

