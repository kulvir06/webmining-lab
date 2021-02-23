!pip install requests
!pip install bs4

import requests
from bs4 import BeautifulSoup

webpageurl = "https://www.flipkart.com/trola-black-shark-running-shoes-men/p/itmf83965073227c?pid=SHOFZP5FFT6RYTYW&lid=LSTSHOFZP5FFT6RYTYWS2GISP&marketplace=FLIPKART&srno=b_1_1&otracker=hp_omu_Deals%2Bof%2Bthe%2BDay_2_4.dealCard.OMU_MMNKD68VVV74_3&otracker1=hp_omu_SECTIONED_neo%2Fmerchandising_Deals%2Bof%2Bthe%2BDay_NA_dealCard_cc_2_NA_view-all_3&fm=neo%2Fmerchandising&iid=en_XO3g%2BpRUWhED9M2F6cGTSLsJBNWZJpMWgvJ4%2FvxQwqCxbRRVNlN5FOUVmFewJX4hpgJzqDbAfQrRBxTZe0OGIw%3D%3D&ppt=browse&ppn=browse&ssid=yycab9wyrk0000001614082214374"
data = requests.get(webpageurl) #gets all content of webpage

# print(data.text[:1000])

soup = BeautifulSoup(data.text, 'html.parser')
# print(soup.prettify()[:1000]) #prettify() used to make html readable

# print(soup.head)#head of html document

# print(soup.body)
# print(soup.title)

product_name = soup.find('span', {'class': 'B_NuCI'})
product_price = soup.find('div', {'class': '_30jeq3 _16Jk6d'})
product_discount = soup.find('div', {'class': '_3Ay6Sb _31Dcoz pZkvcx'})
product_image = soup.find('div', {'class': '_312yBx SFzpgZ'})

print(product_name.text)
print(product_price.text)
print(product_discount.span.text)
print(product_image.img)
