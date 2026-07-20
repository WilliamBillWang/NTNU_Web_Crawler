
from Crawler.homepage import HomePageCrawler

crawler = HomePageCrawler()
news = crawler.get_the_latest_news()
for n in news:
    print(f"Title : {n.title}" )
    print(f"Url : {n.url}" )
    print("-" * 50)

    

    
        # print(all_news)
        # print(title)
        # print(url)
        # print("-" * 50)

    # title = news.first.locator("span").text_content()
    # url = news.first.locator("a").get_attribute("href")
    # print(title,"\n", url)
    # print(links.count())
    # print("新聞數量" , news.count())
    