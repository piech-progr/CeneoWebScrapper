from app.models.opinion import Opinion
import requests
from bs4 import BeautifulSoup

class Product:
    def __init__(self, productId, product_name = None, opinions = []):
        self.productId = productId
        self.product_name = product_name
        self.opinions = opinions
    
    def extract_product(self):
        next_page = "https://www.ceneo.pl/{}#tab=reviews".format(self.productId)
        while next_page:
            respons = requests.get(next_page)
            page_dom = BeautifulSoup(respons.text, "html.parser")
            opinions = page_dom.select("div.js_product-review")
            for opinion in opinions:
                self.opinions.append(Opinion().extract_opinion(opinion))
            try:
                next_page = "https://www.ceneo.pl" + \
                    page_dom.select("a.pagination__next").pop()["href"]
            except IndexError:
                next_page = None
            print(next_page)

    def __str__(self):
        pass

    def __dict__(self):
        pass




















# class Product:
#     def __init__(self,productId,rating,opinionCount):
#         self.productId=productId
#         self.rating=rating
#         self.opinionCount=opinionCount

#     def __repr__(self):
#             print(f"""
#             Id produktu: {self.productId}
#             Ocena produktu: {self.rating}
#             Ilość opinii: {self.opinionCount} """ )