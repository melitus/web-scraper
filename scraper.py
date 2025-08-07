# scraper.py

import requests
from bs4 import BeautifulSoup
from requests.exceptions import RequestException

BASE_URL = 'http://books.toscrape.com/catalogue/page-{}.html'
HEADERS = {'User-Agent': 'Mozilla/5.0'}

def fetch_page(url):
    """Fetch the HTML content of a page with error handling."""
    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
        response.raise_for_status()
        return response.text
    except RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None

def parse_book_data(book):
    """Extract and return title, price, and availability from a book element."""
    try:
        title = book.h3.a.get('title', 'No Title Found')
        price = book.find('p', class_='price_color')
        availability = book.find('p', class_='instock availability')

        price_text = price.text.strip() if price else 'No Price Found'
        availability_text = availability.text.strip() if availability else 'No Availability Info'

        return {
            'title': title,
            'price': price_text,
            'availability': availability_text
        }
    except AttributeError:
        print("Error parsing a book element. Skipping...")
        return None

def scrape_books(pages=1):
    """Main function to scrape books across multiple pages."""
    if pages < 1:
        print("Page count must be at least 1.")
        return

    for page in range(1, pages + 1):
        url = BASE_URL.format(page)
        html = fetch_page(url)

        if not html:
            print(f"Skipping page {page} due to fetch error.")
            continue

        soup = BeautifulSoup(html, 'html.parser')
        books = soup.find_all('article', class_='product_pod')

        if not books:
            print(f"No books found on page {page}.")
            continue

        print(f"\n📄 Page {page} Results:\n" + "-" * 30)

        for book in books:
            data = parse_book_data(book)
            if data:
                print(f"Title: {data['title']}")
                print(f"Price: {data['price']}")
                print(f"Availability: {data['availability']}\n")

if __name__ == '__main__':
    try:
        scrape_books(pages=3)
    except KeyboardInterrupt:
        print("\nScraping interrupted by user.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
