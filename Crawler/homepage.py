from playwright.sync_api import sync_playwright
from models.news import News

class HomePageCrawler:

    def __init__(self): #initiallize
        self.url = "https://www.ntnu.edu.tw"
        # print("build successfully")

    def get_the_latest_news(self):
        with sync_playwright() as p:
            browser = p.chromium.launch(headless = False)
            page = browser.new_page()
            page.goto(self.url)
            # title = page.title()
            # print(page.title())

            # page.wait_for_timeout(5000)
            # links =  page.locator("a")
            news =  page.locator(".index-news-list")
            count = news.count()

            all_news = []
            for i in range(count): # interate

                item = news.nth(i)
                title= item.text_content().strip()
                url = item.locator("a").get_attribute("href")

                pack_news = News(title,url)
                all_news.append(pack_news)

            browser.close()
            return all_news