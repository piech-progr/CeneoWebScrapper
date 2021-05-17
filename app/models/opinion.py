from app.utils import extract_element

class Opinion:
    
    selectors = {
        "author": ["span.user-post__author-name"],
        "recommendation": ["span.user-post__author-recomendation > em"],
        "stars": ["span.user-post__score-count"],
        "content": ["div.user-post__text"],
        "pros": ["div.review-feature__col:has(> div[class*=\"positives\"]) > div.review-feature__item", 1],
        "cons": ["div.review-feature__col:has(> div[class*=\"negatives\"]) > div.review-feature__item", 1],
        "purchased": ["div.review-pz"],
        "submit_date": ["span.user-post__published > time:nth-child(1)", "datetime"],
        "purchase_date": ["span.user-post__published > time:nth-child(2)", "datetime"],
        "useful": ["span[id^='votes-yes']"],
        "useless": ["span[id^='votes-no']"]
    }

    def __init__(self, opinionId = None, author = None, recommendation = None, stars = None, content = None, pros = [], cons = [], purchased = None, submit_date = None, 
                purchase_date = None, useful = None, useless = None):
        self.opinionId = opinionId
        self.author = author
        self.recommendation = recommendation
        self.stars = stars
        self.content = content
        self.pros = pros
        self.cons = cons
        self.purchased = purchased
        self.submit_date = submit_date
        self.purchase_date = purchase_date
        self.useful = useful
        self.useless = useless
    
    def extract_opinion(self, opinion):                         
        for key, args in self.selectors.items():
            setattr(self, key, extract_element(opinion, *args))
        self.opinionId = opinion["data-entry-id"]

        opinion_elements["recommendation"] = True if opinion_elements[
            "recommendation"] == "Polecam" else False if opinion_elements["recommendation"] == "Nie polecam" else None
        opinion_elements["stars"] = float(
            opinion_elements["stars"].split("/")[0].replace(",", "."))
        opinion_elements["purchased"] = bool(
            opinion_elements["purchased"])
        opinion_elements["useful"] = int(opinion_elements["useful"])
        opinion_elements["useless"] = int(opinion_elements["useless"])
    
    def __str__(self):
        pass

    def __dict__(self):
        pass


















# class Opinion:
#     def __init__(self,idOpinion,author,recommendation,stars,confirmed,publishDate,dateOfPurchase,useful,useless,text,pros,cons):
#         self.idOpinion=idOpinion
#         self.author=author
#         self.recommendation=recommendation
#         self.stars=stars
#         self.confirmed=confirmed
#         self.publishDate=publishDate
#         self.dateOfPurchase=dateOfPurchase
#         self.useful=useful
#         self.useless=useless
#         self.text=text
#         self.pros=pros
#         self.cons=cons

#     def __repr__(self):
#         print(f"""
#         Author: {self.author}
#         Recommendation: {self.recommendation}
#         Number of stars: {self.stars}
#         Confirmed by purchase: {self.confirmed}
#         Date of submission: {self.publishDate}
#         Date of purchase: {self.dateOfPurchase}
#         Number of people who thought the review was useful: {self.useful}
#         Number of people who thought the review was useless: {self.useless}
#         Content of the review: {self.text}
#         Pros: {self.pros}
#         Cons: {self.cons}
#         """
#         )
