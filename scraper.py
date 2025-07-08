import time
from selenium.webdriver.common.by import By
from urllib.parse import urljoin

def get_book_links(driver, page_url):
    driver.get(page_url)
    time.sleep(1)
    books = driver.find_elements(By.CSS_SELECTOR, 'article.product_pod h3 a')
    return [urljoin(page_url, b.get_attribute('href')) for b in books]
def extract_book_info(driver, book_url):
    driver.get(book_url)
    time.sleep(0.5)
    name = driver.find_element(By.TAG_NAME, 'h1').text
    price = driver.find_element(By.CLASS_NAME, 'price_color').text
    info = {
        row.find_element(By.TAG_NAME, 'th').text:
        row.find_element(By.TAG_NAME, 'td').text
        for row in driver.find_elements(By.CSS_SELECTOR, 'table.table-striped tr')
    }
    return {
        'Name': name,
        'Price': price,
        'UPC': info.get('UPC', ''),
        'Product Type': info.get('Product Type', ''),
        'Price (excl. tax)': info.get('Price (excl. tax)', ''),
        'Price (incl. tax)': info.get('Price (incl. tax)', ''),
        'Tax': info.get('Tax', ''),
        'Availability': info.get('Availability', ''),
        'Number of Reviews': info.get('Number of reviews', '')
    }
