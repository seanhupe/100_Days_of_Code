import time
from playwright.sync_api import sync_playwright

playwright = sync_playwright().start()
browser = playwright.chromium.launch(headless=False, slow_mo=1000)
page = browser.new_page()
page.goto("https://bootswatch.com/default/")

time.sleep(3)
