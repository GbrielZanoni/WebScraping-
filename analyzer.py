import csv
import re
import statistics

def extract_float(price_str):
    price_number = re.findall(r"\d+\.\d+", price_str)
    return float(price_number[0]) if price_number else 0.0

def analyze_books(csv_file='books.csv', log_file='analysis_log.txt'):
    prices = []
    ratings = []

    with open(csv_file, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            price = extract_float(row['Price'])
            rating = int(row.get('Rating', 0))

            prices.append(price)
            ratings.append(rating)

    avg_price = statistics.mean(prices) if prices else 0.0
    avg_rating = statistics.mean(ratings) if ratings else 0.0

    expensive_books = [ratings[i] for i in range(len(prices)) if prices[i] > avg_price]
    cheap_books = [ratings[i] for i in range(len(prices)) if prices[i] <= avg_price]

    avg_rating_expensive = statistics.mean(expensive_books) if expensive_books else 0.0
    avg_rating_cheap = statistics.mean(cheap_books) if cheap_books else 0.0

    with open(log_file, 'w', encoding='utf-8') as log:
        log.write(f"Total de livros: {len(prices)}\n")
        log.write(f"Preço médio: £{avg_price:.2f}\n")
        log.write(f"Rating médio: {avg_rating:.2f}\n")
        log.write(f"\nRating médio dos livros mais caros que a média: {avg_rating_expensive:.2f}\n")
        log.write(f"Rating médio dos livros mais baratos que a média: {avg_rating_cheap:.2f}\n")

    print(f"\nAnálise finalizada. Resultados salvos em '{log_file}'")
