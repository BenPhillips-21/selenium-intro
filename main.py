from selenium import webdriver

url = 'https://books.toscrape.com/'

options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=options)
driver.get(url)
print(driver.title)