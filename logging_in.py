from selenium import webdriver
from selenium.webdriver.common.by import By

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


def scrape_page(le_driver):
    quotes = le_driver.find_elements(By.CLASS_NAME, 'quote')
    print(len(quotes))
    for element in quotes:
        quote = element.find_element(By.CSS_SELECTOR, 'span').text
        print(quote)

        author = element.find_element(By.CLASS_NAME, 'author').text
        print(author)

        tag_container = element.find_element(By.CLASS_NAME, 'tags')
        a_tags = tag_container.find_elements(By.CSS_SELECTOR, 'a')
        tags = ''
        for tag in a_tags:
            tags += tag.text + ' '
        print(tags)
        print('\n')

login(driver)
scrape_page(driver)
