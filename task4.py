import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://example.com/products'  # Replace with the actual website
headers = {'User-Agent': 'Mozilla/5.0'}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')

# Example extraction (modify based on website structure)
products = []
for item in soup.find_all('div', class_='product'):
    name = item.find('h2').text
    price = item.find('span', class_='price').text
    rating = item.find('span', class_='rating').text
    products.append([name, price, rating])

# Save to CSV
df = pd.DataFrame(products, columns=['Name', 'Price', 'Rating'])
df.to_csv('products.csv', index=False)

print("Data saved to products.csv")