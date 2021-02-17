
import scrapy
from ..items import ProductsItem
class pro(scrapy.Spider):
 name = "pro"
 start_urls = ["https://www.flipkart.com/samsung-galaxy-m21-midnight-blue-128-gb/p/itm0cec19c31b3cb?pid=MOBFSF85ZMVH3ZMG&lid=LSTMOBFSF85ZMVH3ZMGHVRMDR&marketplace=FLIPKART&fm=neo%2Fmerchandising&iid=M_ab883bcf-9673-4bf2-adc9-fccdcf6198a4_1_1BUWY8OBA8L9_MC.MOBFSF85ZMVH3ZMG&ppt=clp&ppn=samsung-mobile-store&ssid=0lzd5i7qgw0000001596104962790&otracker=clp_pmu_v2_Latest%2BSamsung%2Bmobiles%2B_1_1.productCard.PMU_V2_Latest%2BSamsung%2Bmobiles%2B_samsung-mobile-store_MOBFSF85ZMVH3ZMG_neo%2Fmerchandising_0&otracker1=clp_pmu_v2_PINNED_neo%2Fmerchandising_Latest%2BSamsung%2Bmobiles%2B_LIST_productCard_cc_1_NA_view-all&cid=MOBFSF85ZMVH3ZMG"]
 def parse(self,response):
  product_name=response.css("span.B_NuCI::text").extract()
  product_price=response.css("div._30jeq3._16Jk6d::text").extract()
  product_discount=response.css("div._3Ay6Sb._31Dcoz").css("span::text").extract()
  product_image=response.css("div.q6DClP::attr(style)").extract()
  items=ProductsItem()
  items["product_name"]=product_name
  items["product_price"]=product_price
  items["product_discount"]=product_discount
  items["product_image"]=product_image
  yield items