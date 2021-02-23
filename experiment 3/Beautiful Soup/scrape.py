!pip install requests
!pip install bs4

import requests
from bs4 import BeautifulSoup

webpageurl = "https://www.flipkart.com/hp-pavilion-gaming-ryzen-5-quad-core-3550h-8-gb-1-tb-hdd-windows-10-home-4-gb-graphics-nvidia-geforce-gtx-1650-15-ec0101ax-laptop/p/itma1af6bf593dc8?pid=COMFSFNVDXG74QXR&lid=LSTCOMFSFNVDXG74QXRY8FRH2&marketplace=FLIPKART&srno=b_1_22&otracker=hp_rich_navigation_6_1.navigationCard.RICH_NAVIGATION_Electronics~Gaming_PK7I48M403OR&fm=organic&iid=a4a75fb6-a7c4-406f-8829-6f0897fc37fc.COMFSFNVDXG74QXR.SEARCH&ppt=browse&ppn=browse&ssid=tri79mziu80000001614107514263"
data = requests.get(webpageurl) #gets all content of webpage

# print(data.text[:1000])

soup = BeautifulSoup(data.text, 'html.parser')
# print(soup.prettify()[:1000]) #prettify() used to make html readable

# print(soup.head)#head of html document

# print(soup.body)
# print(soup.title)

product_name = soup.find('span', {'class': 'B_NuCI'})
product_price = soup.find('div', {'class': '_30jeq3 _16Jk6d'})
product_discount = soup.find('div', {'class': '_3Ay6Sb _31Dcoz'})
product_image = soup.find('div', {'class': 'CXW8mj _3nMexc'})

print("\n\n***********OUTPUT***********")
print("Product Name = "+product_name.text)
print("Product Price = "+product_price.text)
print("Product Discount = "+product_discount.span.text)
print("Product Image = "+str(product_image.img))
