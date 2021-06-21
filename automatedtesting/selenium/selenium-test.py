# #!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
import datetime

# Start the browser and login with standard_user
def login(driver, user, password):
    url = 'https://www.saucedemo.com/'
    print(timestamp() + 'Navigating to the webpage : ' + url)
    driver.get(url)
    driver.find_element_by_css_selector("input[id='user-name']").send_keys(user)
    driver.find_element_by_css_selector("input[id='password']").send_keys(password)
    driver.find_element_by_id("login-button").click()
    product_label = driver.find_element_by_css_selector("div[class='product_label']").text
    assert "Products" in product_label
    print(timestamp() + 'Login successful with username {:s}'.format(user))

# Add products to the cart
def add_cart(driver, number):
    for i in range(number):
        element = "a[id='item_" + str(i) + "_title_link']"
        driver.find_element_by_css_selector(element).click()
        driver.find_element_by_css_selector("button.btn_primary.btn_inventory").click() 
        product = driver.find_element_by_css_selector("div[class='inventory_details_name']").text 
        print(timestamp() + "Shopping cart += " + product) 
        driver.find_element_by_css_selector("button.inventory_details_back_button").click() 
    print(timestamp() + 'Number of items added to the shopping cart : {:d}'.format(number))
    number_element = "div[span='shopping_cart_link']"
    cart_number = driver.find_element_by_css_selector(number_element).text
    assert cart_number == 6


# Remove products to the cart
def remove_cart(driver, number):
    for i in range(number):
        element = "a[id='item_" + str(i) + "_title_link']"
        driver.find_element_by_css_selector(element).click()
        driver.find_element_by_css_selector("button.btn_secondary.btn_inventory").click()
        product = driver.find_element_by_css_selector("div[class='inventory_details_name']").text
        print(timestamp() + "Shopping cart -= " + product) 
        driver.find_element_by_css_selector("button.inventory_details_back_button").click()
    print(timestamp() + 'Number of items added to the shopping cart : {:d}'.format(number))
    number_element = "div[span='shopping_cart_link']"
    cart_number = driver.find_element_by_css_selector(number_element).text
    assert cart_number == 0

# Get chrome drive
def getChromeDriver():
    options = ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument("--headless") 
    driver = webdriver.Chrome(options=options)
    print(timestamp() + 'Browser Started.')
    return driver

# Get timestamp
def timestamp():
    ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return (ts + '\t')


if __name__ == "__main__":
    number = 6
    TEST_USERNAME = 'standard_user'
    TEST_PASSWORD = 'secret_sauce'
    driver = getChromeDriver()
    login(driver, TEST_USERNAME, TEST_PASSWORD)
    add_cart(driver, number)
    remove_cart(driver, number)
    print(timestamp() + 'All tests are successfully completed!')