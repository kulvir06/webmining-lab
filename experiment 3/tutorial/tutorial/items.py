
import scrapy

class ProductsItem(scrapy.Item):
    # define the fields for your item here like:
    product_name = scrapy.Field()
    product_price = scrapy.Field()
    product_discount = scrapy.Field()
    product_image = scrapy.Field()



