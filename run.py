from playwright.sync_api import sync_playwright, Page


def run_browser() -> Page:
    print('Start context')
    playwright_context = sync_playwright().start()
    print('Launch browser')
    browser = playwright_context.chromium.launch()
    print('Open new page')
    page = browser.new_page()
    return playwright_context, browser, page

def start():
    try:
        playwright_context, browser, page = run_browser()
        print('Load page')
        page.goto("https://google.com")
        print("Now, trigger `KeyboardInterrupt` (e.g. via SIGTERM) during `page.goto()` execution:")
        while True:
            print('\tNOW')
            page.goto("https://microsoft.com")

    except KeyboardInterrupt:
        print("Handle exception")
    
    finally:
        print("Close page")
        page.close()
        print("Page closed")

        print("Close browser")
        browser.close()
        print("Browser closed")

        print("Stop context")
        playwright_context.stop()
        print("Context stopped")




if __name__ == '__main__':
    start()