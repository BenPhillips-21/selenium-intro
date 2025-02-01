from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import openpyxl

quote_dict = {
    'quote': [],
    'author': [],
    'tags': []
}

def login(le_driver):
    login_button = le_driver.find_element(By.XPATH, '//a[text()="Login"]')
    login_button.click()

    username_input = le_driver.find_element(By.ID, 'username')
    username_input.send_keys('ben')

    password_input = le_driver.find_element(By.ID, 'password')
    password_input.send_keys('password')

    log_me_in = le_driver.find_element(By.XPATH, '//input[@type="submit"]')
    log_me_in.click()

    print(le_driver.title)

url = 'https://quotes.toscrape.com/js'

options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--headless')
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=options)
driver.get(url)


def scrape_page(le_driver, le_dict):
    quotes = le_driver.find_elements(By.CLASS_NAME, 'quote')
    for element in quotes:
        quote = element.find_element(By.CSS_SELECTOR, 'span').text
        le_dict['quote'].append(quote)

        author = element.find_element(By.CLASS_NAME, 'author').text
        le_dict['author'].append(author)

        tag_container = element.find_element(By.CLASS_NAME, 'tags')
        a_tags = tag_container.find_elements(By.CSS_SELECTOR, 'a')
        tags = ''
        for tag in a_tags:
            tags += tag.text + ' '
        le_dict['tags'].append(tags)

login(driver)

while True:
    scrape_page(driver, quote_dict)
    # selenium throws an error when it can't find an element, hence the try/except
    try:
        next_button = driver.find_element(By.CSS_SELECTOR, 'li.next a')
        next_button.click()
    except:
        break


df = pd.DataFrame(quote_dict)
df.to_excel('quotes.xlsx')
