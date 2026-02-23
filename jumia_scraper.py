import requests
import pandas as  pd 
from bs4  import BeautifulSoup

url  = "https://www.jumia.co.ke/computers-tablets/"

def scrape_jumia(url): 
    html = requests.get(url).text 
    soup  = BeautifulSoup(html, "html.parser")
    
    products = []	

    cards = soup.select("article.prd")  
    for card in cards:
        # product name
        item_name = card.select_one("h3.name")
        item_name = item_name.text.strip() if item_name else None

        # current price
        current_price = card.select_one("div.prc")
        current_price = current_price.text.strip() if current_price else None

        # old price
        old_price = card.select_one("div.old")
        old_price = old_price.text.strip() if old_price else None

        # discount
        discount_pct = card.select_one("div.bdg._dsct")
        discount_pct = discount_pct.text.strip() if discount_pct else None

        # link
        link = card.select_one("a.core")
        product_link = "https://www.jumia.co.ke" + link["href"] if link else None

        #image
        image_element = card.select_one("img")
        image = image_element.get("data-src") if image_element else None
      
        if all([item_name, current_price, product_link, image]):
            products.append({
                "item_name": item_name,
                "current_price": current_price,
                "old_price": old_price,
                "discount_pct": discount_pct,
                "product_link": product_link,
		"image": image
            })

    return pd.DataFrame(products)

# Scrape the first 20 pages
pages = []
for page in range(1, 21):
	page_url = f"{url}?page={page}#catalog-listing"
	page_data = scrape_jumia(page_url)
	pages.append(page_data)

data = pd.concat(pages, ignore_index = True)
print(data)
