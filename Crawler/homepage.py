from Crawler.base import BaseCrawler
from models.news import News


class HomePageCrawler(BaseCrawler): #Inheritance

    # def __init__(self): #initiallize
    #     super().__init__()
    #     self.url = "https://www.ntnu.edu.tw"
    #     # print("build successfully")
    url = "https://www.ntnu.edu.tw"
    
    def parse_news(self,page):
        news =  page.locator(".index-news-list")
        count = news.count()

        all_news = []
        for i in range(count): # interate

            item = news.nth(i)
            title= item.text_content().strip()
            url = item.locator("a").get_attribute("href")

            pack_news = News(title,url)
            all_news.append(pack_news)

        return all_news
            


