from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import openpyxl
from time import sleep

options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
# options.add_argument('--headless')
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(5)

url = 'https://www.imdb.com/search/title/?explore=genres&title_type=feature'
driver.get(url)
sleep(1)
print(driver.title)

bio_filter_button_span = driver.find_element(By.XPATH, '//span[text()="Biography"]')
bio_filter_button = bio_filter_button_span.find_element(By.XPATH, './..')
driver.execute_script("arguments[0].click();", bio_filter_button)

doco_checkbox = driver.find_element(By.ID, 'exclude-documentary-checkbox')
print(doco_checkbox.get_attribute('type'))
driver.execute_script("arguments[0].click();", doco_checkbox)

short_checkbox = driver.find_element(By.ID, 'exclude-short-checkbox')
print(short_checkbox.get_attribute('type'))
driver.execute_script("arguments[0].click();", short_checkbox)

awards_accordion = driver.find_element(By.XPATH, '/html/body/div[2]/main/div[2]/div[3]/section/section/div/section/section/div[2]/div/section/div[2]/div[1]/section/div/div[6]/div[1]/label')
driver.execute_script("arguments[0].click();", awards_accordion)

oscar_nominated_filter_span = driver.find_element(By.XPATH, '//span[text()="Oscar-Nominated"]')
oscar_nominated_filter = oscar_nominated_filter_span.find_element(By.XPATH, './..')
driver.execute_script("arguments[0].click();", oscar_nominated_filter)

top_1000_filter_span = driver.find_element(By.XPATH, '//span[text()="IMDb Top 1000"]')
top_1000_filter = top_1000_filter_span.find_element(By.XPATH, './..')
driver.execute_script("arguments[0].click();", top_1000_filter)

view_more_button_grandchild = driver.find_element(By.XPATH, '//span[text()="29 more"]')
view_more_button = view_more_button_grandchild.find_element(By.XPATH, './../..')
driver.execute_script("arguments[0].click();", view_more_button)

sleep(2)

biopics_container = driver.find_element(By.XPATH, '//ul[@class="ipc-metadata-list ipc-metadata-list--dividers-between sc-e22973a9-0 khSCXM detailed-list-view ipc-metadata-list--base"]')
print(biopics_container.tag_name)
biopics = biopics_container.find_elements(By.XPATH, './li')

biopic_links = []

print(len(biopics))

for pic in biopics:
    pic_anchor = pic.find_element(By.XPATH, './/a[@class="ipc-title-link-wrapper"]')
    pic_href = pic_anchor.get_attribute('href')
    biopic_links.append(pic_href)

director_page_links = []

def scrape_bio_page(le_driver, le_link):
    le_driver.get(le_link)
    sleep(1)
    directors_ul = le_driver.find_element(By.XPATH, '//ul[@class="ipc-inline-list ipc-inline-list--show-dividers ipc-inline-list--inline ipc-metadata-list-item__list-content baseAlt"]')
    directors = directors_ul.find_elements(By.XPATH, './li')
    for dir in directors:
        director_page_links.append(dir.find_element(By.XPATH, './a').get_attribute('href'))


for link in biopic_links:
    scrape_bio_page(driver, link)



def scrape_director_page(le_driver, le_link):
    le_driver.get(le_link)
    director_name = le_driver.find_element(By.XPATH, '//span[@class="hero__primary-text"]').text
    try:
        quotes_anchor = le_driver.find_element(By.XPATH, '//a[text()="Quotes"]')
        top_quote_div = quotes_anchor.find_element(By.XPATH, './following-sibling::div[1]')
        top_quote = top_quote_div.text
    except:
        top_quote = "N/A"
    try:
        height_span = le_driver.find_element(By.XPATH, '//span[text()="Height"]')
        height_div = height_span.find_element(By.XPATH, './following-sibling::div[1]')
        height = height_div.text
    except:
        height = "N/A"
    return director_name, top_quote, height

directors_info = {
    'name': [],
    'top_quote': [],
    'height': []
}

for link in director_page_links:
    name, quote, height = scrape_director_page(driver, link)
    directors_info['name'].append(name)
    directors_info['top_quote'].append(quote)
    directors_info['height'].append(height)

df = pd.DataFrame(directors_info)
df.to_excel('directors.xlsx')

driver.quit()
