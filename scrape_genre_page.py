from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

def scrape_genre_page(le_driver, link):
    le_driver.get(link)
    sleep(1)
    genre_name = le_driver.find_element(By.XPATH, '//h3[@class="ipc-title__text"]').text

    genre_description = le_driver.find_element(By.XPATH, '//div[@class="ipc-html-content-inner-div"]').text

    top_rated_movies_title = le_driver.find_element(By.XPATH, '//h3[text()="Top rated movies" or text()="Top rated TV shows" or text()="Popular movies"]')
    top_rated_movies_section = top_rated_movies_title.find_element(By.XPATH, './../../..')
    top_rated_movies_carousel_container = top_rated_movies_section.find_element(By.XPATH, '(./div)[2]')
    top_rated_movies_carousel_div = top_rated_movies_carousel_container.find_element(By.XPATH, '(./div)[2]')
    all_top_rated_movies = top_rated_movies_carousel_div.find_elements(By.XPATH, './*')
    all_movies = ''
    for movie in all_top_rated_movies:
        movie_poster_card_title_anchor = movie.find_element(By.XPATH, './a')
        movie_name = movie_poster_card_title_anchor.find_element(By.XPATH, './span').text
        all_movies += movie_name + ', '

    return genre_name, genre_description, all_movies