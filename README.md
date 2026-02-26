# Online Marketplace Scraper

This project contains a BeautifulSoup web scraping script that scrapes computers from an online marketplace with pagination and database strorage.

## Tools
* **Scraper:** BeautifulSoup4
* **Storage:** psql

## Project structure
```text
jumia_computers_scraper/
├── jumia_scraper.py              # extraction logic & BeautifulSoup parser
├── requirements.txt             # Project dependencies
└── .env  
```

## How it works
The script iterates over the product cards selecting the required fields based on the html class of the elements. These fields are then stored in a dictionary if the `item_name`, `current_price`, `product_link` and `image` exist. The scraped fields are the added to the empty `products` list defined and stored in a Pandas DataFrame. To ensure multiple pages are scraped, a `for loop` is initialized for `range(1, 21)` that iterates over the computers' pages and adding the fields to the empty `pages` list and later added to the dataframe. The `to_sql` pandas function is then initialized to upload the data to the database
