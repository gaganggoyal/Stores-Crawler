import os
import glob
import csv
from openpyxl import Workbook
from scrapy import Spider
from scrapy.http import Request
from scrapy.loader import ItemLoader
from stores_crawler.items import StoresCrawlerItem

# def product_info(response, value):
#         return response.xpath('//th[text()="' + value + '"]/following-sibling::td/text()').extract_first()

class BooksSpider(Spider):
    name = "books"
    allowed_domains = ["books.toscrape.com"]
    # start_urls = ["http://books.toscrape.com/"]

    def __init__(self, category):
         self.start_urls = [category]

    def parse(self, response):

        books = response.xpath('//h3/a/@href').extract()
        for book in books:
            absolute_url = response.urljoin(book)
            yield Request(absolute_url, callback=self.parse_book)

        # process next page
        next_page_url = response.xpath('//a[text()="next"]/@href').extract_first()
        absolute_next_page_url = response.urljoin(next_page_url)
        yield Request(absolute_next_page_url)
    
    def parse_book(self, response):

        l = ItemLoader(item=StoresCrawlerItem(), response=response)

        title = response.css('h1::text').extract_first()
        price = response.xpath('//*[@class="price_color"]/text()').extract_first()
        image_urls = response.xpath('//img/@src').extract_first()
        image_urls = image_urls.replace('../..', 'http://books.toscrape.com/')

        l.add_value('title', title )
        l.add_value('price', price )
        l.add_value('image_urls', image_urls )

        return l.load_item()

    #     rating = response.xpath('//*[contains(@class, "star-rating")]/@class').extract_first()
    #     rating = rating.replace('star-rating', '')

    #     description = response.xpath(
    #         '//*[@id="product_description"]/following-sibling::p/text()').extract_first()

    #     # product information data points

    #     upc = product_info(response, 'UPC' )
    #     product_type = product_info(response, 'Product Type')
    #     price_without_tax = product_info(response, 'Price (excl. tax)')
    #     price_with_tax = product_info(response, 'Price (incl. tax)')
    #     tax = product_info(response, 'Tax')
    #     availability = product_info(response, 'Availability' )
    #     number_of_reviews = product_info(response, 'Number of reviews')
    #     yield {
    #         'title': title,
    #         'price': price,
    #         'image_url': image_url,
    #         'rating': rating,
    #         'description': description,
    #         'upc': upc,
    #         'product_type': product_type,
    #         'price_without_tax': price_without_tax,
    #         'price_with_tax': price_with_tax,
    #         'tax': tax,
    #         'availability': availability,
    #         'number_of_reviews': number_of_reviews

    #     }

    
    # # # function to convert name of csv
    # # def close(self, reason):
    # #      csv_file = max(glob.iglob('*.csv'), key=os.path.getctime)
    # #      os.rename(csv_file, 'foobar.csv')
        
    # # function to convert csv to excel
    # def close(self, reason):
    #      csv_file = max(glob.iglob('*.csv'), key=os.path.getctime)

    #      wb = Workbook()
    #      ws = wb.active

    #      with open(csv_file, 'r') as f:
    #           for row in csv.reader(f):
    #                ws.append(row)
    #      wb.save(csv_file.replace('.csv', '') + '.xlsx')

