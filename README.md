# Stores-Crawler

A Scrapy crawler for the demo bookstore at
[books.toscrape.com](http://books.toscrape.com). It walks every catalogue page,
opens each book and saves the product details.

- Follows pagination until the last page
- Collects title, price, rating, image URL and description
- Reads the product information table (UPC, product type, prices with and
  without tax, availability, reviews) with XPath
- Sample output in `items.csv`

## Run it

```bash
pip install scrapy
scrapy crawl books -o books.csv
```

---

An early learning project from April 2023, kept for reference and archived. My current work is on [my profile](https://github.com/gaganggoyal) and at [gagan.indiaoffers.in](https://gagan.indiaoffers.in).
