# Online Marketplace Scraper

This project contains a BeautifulSoup web scraping script that scrapes computers from Jumia with pagination and database strorage.

## Tools
* **Extraction:** Python, Requests, BeautifulSoup4 
* **Transformation:** Pandas
* **Storage:** PostgreSQL, SQLAlchemy

## Setup & Installation
Clone the repository and install the required dependencies:
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt

## Project structure
```text
jumia_computers_scraper/
├── jumia_scraper.py              # extraction logic & BeautifulSoup parser
├── requirements.txt             # Project dependencies
└── .env  
```

## How it works
* **Extraction:** The script iterates through the first 20 pages of the Jumia Computers category.
* **Validation:** It isolates individual product cards and extracts fields based on their CSS classes. A record is only appended if it has a valid `item_name`, `current_price`, `product_link`, and `image`.
* **Database Load:** Data is batched into a Pandas DataFrame and loaded into Postgres.
