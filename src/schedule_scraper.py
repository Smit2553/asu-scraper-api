from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright


def get_dynamic_soup(url: str) -> BeautifulSoup:
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(url)
        page.wait_for_selector("div#class-results")
        soup = BeautifulSoup(page.content(), "html.parser")
        browser.close()
        return soup


url = 'https://catalog.apps.asu.edu/catalog/classes/classlist?campusOrOnlineSelection=A&catalogNbr=230&honors=F&promod=F&searchType=all&subject=CSE&term=2241'

soup = get_dynamic_soup(url)

print(soup.prettify())
