from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://books.toscrape.com/'

options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)
driver.get(url)


list_items = driver.find_elements(By.CSS_SELECTOR, 'li')
print(len(list_items))

list_item = driver.find_element(By.CSS_SELECTOR, 'li').text
print(list_item)

# selecting by class name
prices = driver.find_elements(By.CSS_SELECTOR, 'p.price_color')
for price in prices:
    print(price.text)

price = driver.find_element(By.CSS_SELECTOR, 'p.price_color').text
print(price)

# selecting by id
body = driver.find_element(By.CSS_SELECTOR, 'body#default')
print(body.text)

# selecting by id - selenium
# body_ = driver.find_element(By.ID, 'default')
# print(body_.text)


# select element by attributes
alert = driver.find_element(By.CSS_SELECTOR, 'div[role="alert"]')
print(alert.text)

# select nested elements
img_src = driver.find_element(By.CSS_SELECTOR, 'article.product_pod div a img').get_attribute('src')
print(img_src)

first_book = driver.find_element(By.CSS_SELECTOR, 'article.product_pod')
print(first_book.text)

warning_div_attribute = driver.find_element(By.CSS_SELECTOR, 'div.alert-warning').get_attribute('role')
print(warning_div_attribute)

book_name = driver.find_element(By.CSS_SELECTOR, 'article.product_pod img').get_attribute('alt')
print(book_name)

# XPath
list_items = driver.find_elements(By.XPATH, '//li')
print(len(list_items))

list_item = driver.find_element(By.XPATH, '//li').text
print(list_item)

# select elements using class name
prices = driver.find_elements(By.XPATH, '//p[@class="price_color"]')
for price in prices:
    print(price.text)

price = driver.find_element(By.XPATH, '//p[@class="price_color"]')
print(f'First elements price = {price.text}')

body = driver.find_element(By.XPATH, '//body[@id="default"]')
print(body.text)

# select elements using attributes
alert = driver.find_element(By.XPATH, '//div[@role="alert"]')
print(alert.text)

# select element using the text inside of it
next_button = driver.find_element(By.XPATH, '//a[text()="next"]')
next_href = next_button.get_attribute('href')
print(next_href)

# selecting nested elements
img_src = driver.find_element(By.XPATH, '//article[@class="product_pod"]/div/a/img').get_attribute('src')
print(img_src)

# navigation - sibling - parents
first_book = driver.find_element(By.XPATH, '//article[@class="product_pod"]')
first_books_div = first_book.find_element(By.XPATH, './div').get_attribute('class')
print(first_books_div)

parent_of_first = first_book.find_element(By.XPATH, './..')
print(parent_of_first.tag_name)
#                                                                         Indexing doesn't start at 0
following_sibling = parent_of_first.find_element(By.XPATH, './following-sibling::li[1]')
second_book_name =  following_sibling.find_element(By.XPATH, './article/div/a/img').get_attribute('alt')
print(second_book_name)

book_name = driver.find_element(By.XPATH, '//article[@class="product_pod"]/../following-sibling::li[18]/article/div/a/img').get_attribute('alt')
print(book_name)

driver.quit()

