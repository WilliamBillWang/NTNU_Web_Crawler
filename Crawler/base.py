from playwright.sync_api import sync_playwright

class BaseCrawler:

    url = None
    
    def __init__(self):
        self.headless = False

    def create_page(self):
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch(headless = self.headless)
        page = self.browser.new_page()
        return page
    
    def close(self):
        self.browser.close()
        self.playwright.stop()

    def get_the_latest_news(self):
            page = self.create_page()
    
            try:
                page.goto(self.url)
                # title = page.title()
                # print(page.title())
                # page.wait_for_timeout(5000)
                # links =  page.locator("a")
                return self.parse_news(page)
                
            finally:
                self.close() #if a value is returned, then this line(after "finally") will firstly executed