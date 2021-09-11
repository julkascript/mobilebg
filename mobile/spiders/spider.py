import scrapy
import json

CRAWL_LINK = "https://www.mobile.bg/pcgi/mobile.cgi?act=3&slink=lgh691&f1=1"

class CarSpider(scrapy.Spider):
    name = "cars"
    start_urls = [
        CRAWL_LINK
    ]

    def parse(self, response):
        old_car_list = []
        new_car_list = []

        with open("db.json", 'r') as f:
            db = json.load(f)

        for link_obj in db["links"]:
            old_car_list.append(link_obj)

        for car in response.css('table.tablereset'):
            try:
                elem = car.css('tr td.valgtop a.mmm::attr(href)').get()
                if elem is not None:
                    full_link = "https:" + elem
                    if full_link not in new_car_list: 
                        new_car_list.append(full_link)
            except Exception as e:
                print(e)
                continue
        
        for link in new_car_list:
            if link not in old_car_list:
                print(f"NEW AD: {link}")

        formatted_new_car_list = {"links": new_car_list}

        with open("db.json", 'w') as f:
            json.dump(formatted_new_car_list, f)
