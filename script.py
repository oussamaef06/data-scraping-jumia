import requests
from bs4 import BeautifulSoup
import csv

url = 'https://www.jumia.ma/iphone/'

def main(url):
    page = requests.get(url)
    src = page.content
    soup = BeautifulSoup(src, 'lxml')

    # Find all product info divs
    product_info_divs = soup.find_all('div', class_='info')

    # Initialize lists to store product titles and prices
    product_titles = []
    product_prices = []

    for product_info in product_info_divs:
        # Extract product titles and prices from the info div
        title = product_info.find('h3', class_='name').text.strip()
        price = product_info.find('div', class_='prc').text.strip()

        product_titles.append(title)
        product_prices.append(price)

    # Create a list of tuples with (title, price) pairs
    product_data = list(zip(product_titles, product_prices))

    # Save the data to a CSV file
    with open('jumia_products.csv', 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['Title', 'Price'])  # Write header row
        csv_writer.writerows(product_data)

if __name__ == '__main__':
    main(url)
