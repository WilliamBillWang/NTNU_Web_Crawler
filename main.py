from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless = False)
    page = browser.new_page()
    page.goto("https://www.ntnu.edu.tw")
    print(page.title())
    # page.wait_for_timeout(5000)
    # links =  page.locator("a")
    news =  page.locator(".index-news-list")
    title = news.first.locator("span").text_content()
    url = news.first.locator("a").get_attribute("href")
    print(title,"\n", url)
    # print(links.count())
    print("新聞數量" , news.count())
    browser.close()