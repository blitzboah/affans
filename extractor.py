import sys
import requests
import json
from bs4 import BeautifulSoup

def extract():
    if(len(sys.argv) < 2):
        print("no search input provided, usage: uv run extractor.py <search_input>")
        sys.exit(1)

    search_input = ' '.join(sys.argv[1:])

    url = f"https://mdcomputers.in/?route=product/search&search={search_input}"

    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
    except Exception as e:
        print(f"error fetching data {e}")
        sys.exit(1)
    
    titles = soup.find_all('h3', class_='product-entities-title')
    price_spans = soup.find_all('span', class_='price')
    
    og_prices = []
    discounted_prices = []
    
    for price_span in price_spans:
        del_tag = price_span.find('span', class_='del')
        ins_tag = price_span.find('span', class_='ins')
        
        og_prices.append(del_tag.get_text(strip=True) if del_tag else 'n/a')
        discounted_prices.append(ins_tag.get_text(strip=True) if ins_tag else 'n/a')
    
    products = []
    for title, og_price, discounted_price in zip(titles, og_prices, discounted_prices):
        product = {
            'name': title.text.strip(),
            'original_price': og_price,
            'discounted_price': discounted_price
        }
        products.append(product)
    
    result = {
        'search_term': search_input,
        'total_products': len(products),
        'products': products
    }

    filename = f'{search_input.replace(" ", "_")}.json'
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(result, f, indent=2, ensure_ascii=False)

    print(f"saved data to {filename}")

extract()
