from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import openpyxl
from logging_in import login

author_page_links = []

author_info = {
    'name': [],
    'birth_date': [],
    'birth_place': [],
}

url = 'https://quotes.toscrape.com/js'

options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--headless')
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=options)
driver.get(url)


def get_author_links(driver, author_page_links):
    about_elements = driver.find_elements(By.XPATH, '//a[text()="(about)"]')
    for element in about_elements:
        author_page_links.append(element.get_attribute('href'))

def scrape_author_page(driver, author_info):
    author_name = driver.find_element(By.XPATH, '//h3[@class="author-title"]').text
    author_info['name'].append(author_name)

    birth_date = driver.find_element(By.XPATH, '//span[@class="author-born-date"]').text
    author_info['birth_date'].append(birth_date)

    birth_place = driver.find_element(By.XPATH, '//span[@class="author-born-location"]').text
    author_info['birth_place'].append(birth_place[2:])

login(driver)
while True:
    get_author_links(driver, author_page_links)

    try:
        next_button = driver.find_element(By.CSS_SELECTOR, 'li.next a')
        next_button.click()
    except:
        print('No more pages')
        break

authors_no_duplicates = list(set(author_page_links))

for link in authors_no_duplicates:
    driver.get(link)
    scrape_author_page(driver, author_info)

df = pd.DataFrame(author_info)
df.to_excel('authors.xlsx')
driver.quit()

