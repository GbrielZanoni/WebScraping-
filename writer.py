import csv

FIELDNAMES = [
    'Name', 'Price', 'UPC', 'Product Type',
    'Price (excl. tax)', 'Price (incl. tax)',
    'Tax', 'Availability', 'Number of Reviews'
]

def create_csv_file(filename):
    f = open(filename, 'w', newline='', encoding='utf-8')
    writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
    writer.writeheader()
    return f, writer