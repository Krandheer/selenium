"""
script portion of div has the link for all details named as url,
useful_url = https://www.magicbricks.com/property-for-sale/residential-real-estate?bedroom=2,3&proptype=Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment,Residential-House,Villa&cityName=New-Delhi&page=1

99acres works same as appending page number in ending
has url for details in main title of tile itself
to get mobile number you need to enter personal details like phone number and email
"""
import re

import requests
from bs4 import BeautifulSoup


def extract():
    url = 'https://www.magicbricks.com/property-for-sale/residential-real-estate?bedroom=2,' \
          '3&proptype=Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment,Residential-House,' \
          'Villa&cityName=New-Delhi&page=1'
    response = requests.get(url=url).content
    soup = BeautifulSoup(response, 'html.parser')
    required_div = soup.find_all("div", class_="mb-srp__card")
    # divs = soup.find_all(".mb-srp__card__container ")
    # print(required_div[0])
    script_tag = required_div[0].find("script").string
    if script_tag:
        price = ""
        property_detail = ""
        all_pic = []
        bed_park_bath = {}
        sqft = ""
        price_per_sqft = ""
        script_content = script_tag.string
        match = re.search(r'"url":"(.*?)"', script_content)
        if match:
            url_detail = match.group(1)
            # print(f"detail url: {url_detail}")
            detail = requests.get(url=url_detail).content
            inner_soup = BeautifulSoup(detail, 'html.parser')
            property_info = inner_soup.find_all("div", class_="mb-ldp__dtls")
            price = inner_soup.select('.mb-ldp__dtls__price')[0].get_text()
            property_detail = inner_soup.select('.mb-ldp__dtls__title--text1')[0].find('span').get_text()
            pictures_right = inner_soup.select(".mb-ldp__premium-dtls__photo__left")
            pictures = inner_soup.select(".mb-ldp__premium-dtls__photo__fig ")
            for pic in pictures_right:
                all_pic.append(pic.find("img")['src'])
            for pic in pictures:
                all_pic.append(pic.find("img")['src'])
            more_detail = inner_soup.select(".mb-ldp__premium-dtls__ameneties")
            beds = ''
            baths = ''
            parkings = ''
            more_detail_sumarry = more_detail[0].select(".mb-ldp__dtls__body__summary--item")
            for item in more_detail_sumarry:
                icon = item.get('data-icon')
                text = item.text.strip()
                if icon == 'beds':
                    if "beds" not in bed_park_bath:
                        bed_park_bath['beds'] = text
                elif icon == 'baths':
                    if "baths" not in bed_park_bath:
                        bed_park_bath['baths'] = text
                elif icon == 'covered-parking':
                    if "parking" not in bed_park_bath:
                        bed_park_bath['parking'] = text
            lis = inner_soup.select('div.mb-ldp__premium-dtls__info ul li')
            sqft = lis[0].find('div', class_='mb-ldp__dtls__body__list').contents[0]
            price_per_sqft = inner_soup.select_one('.mb-ldp__dtls__body__list--size').get_text()
            print(sqft, price)



extract()
