from driver import setup_driver
from scraper import get_book_links, extract_book_info
from writer import create_csv_file
from concurrent.futures import ThreadPoolExecutor, as_completed

def scrape_books():
    base_url = "https://books.toscrape.com/catalogue/page-{}.html"
    page_count = 1
    book_count = 0

    driver = setup_driver(headless=True)
    csv_file, writer = create_csv_file('books.csv')

    try:
        while True:
            page_url = base_url.format(page_count)
            print(f"\nPágina {page_count}: {page_url}")

            book_links = get_book_links(driver, page_url)

            if not book_links:
                print("\nFim das páginas ou página inválida.")
                break

            print(f"Livros encontrados: {len(book_links)}")

            with ThreadPoolExecutor(max_workers=5) as executor:
                futures = {executor.submit(extract_book_info, link): link for link in book_links}
                for future in as_completed(futures):
                    book_info = future.result()
                    if book_info:
                        writer.writerow(book_info)
                        book_count += 1
                        print(f"Livro {book_count} salvo: {book_info['Name']}")

            page_count += 1

    finally:
        csv_file.close()
        driver.quit()
        print(f"\nColeta finalizada. {book_count} livros salvos.")
        print("Dados salvos em books.csv")

if __name__ == "__main__":
    scrape_books()
