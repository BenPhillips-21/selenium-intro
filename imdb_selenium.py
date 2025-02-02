from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd
import openpyxl
from time import sleep
from scrape_genre_page import scrape_genre_page

options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
# options.add_argument('--headless')
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(3)

genre_info = {
    'name': [],
    'description': [],
    'top_rated_movies': []
}

driver.get('https://www.imdb.com/')

sleep(2)

try:
    accept_cookies = driver.find_element(By.XPATH, '//button[text()="Accept"]')
    accept_cookies.click()
except:
    pass

menu_button = driver.find_element(By.ID, 'imdbHeader-navDrawerOpen')
menu_button.click()

sleep(1)

by_genre_button = driver.find_element(By.XPATH, '//span[text()="Browse Movies by Genre"]')
by_genre_button.click()
sleep(1)

comedy_h3 = driver.find_element(By.XPATH, '//h3[text()="Comedy"]')
comedy_section = comedy_h3.find_element(By.XPATH, './../../..')
comedy_carousel_container = comedy_section.find_element(By.XPATH, '(./div)[2]')
comedy_carousel_div = comedy_carousel_container.find_element(By.XPATH, '(./div)[2]')
all_genres = comedy_carousel_div.find_elements(By.XPATH, './*')

genre_page_links = []

for genre in all_genres:
    genre_href = genre.find_element(By.XPATH, './a').get_attribute('href')
    genre_page_links.append(genre_href)


for link in genre_page_links:
    genre_name, genre_description, all_movies = scrape_genre_page(driver, link)
    genre_info['name'].append(genre_name)
    genre_info['description'].append(genre_description)
    genre_info['top_rated_movies'].append(all_movies)

df = pd.DataFrame(genre_info)
df.to_excel('genres.xlsx')
driver.quit()