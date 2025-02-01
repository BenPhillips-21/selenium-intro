from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = 'https://quotes.toscrape.com/js-delayed'

options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=options)
driver.implicitly_wait(10)
# tells program wait for 10 seconds before it errors from not finding any element on page
driver.get(url)

#              maximum amount of time it will wait                           must be in parenthises
WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.quote')))

quotes = driver.find_elements(By.CSS_SELECTOR, 'div.quote')
print(len(quotes))