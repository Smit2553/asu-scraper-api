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


def extract_data(soup, class_name):
    elements = soup.find_all('div', class_=class_name)
    return [element.text.strip() for element in elements]


def parse_classes():
    url = 'https://catalog.apps.asu.edu/catalog/classes/classlist?campusOrOnlineSelection=A&catalogNbr=230&honors=F&promod=F&searchType=all&subject=CSE&term=2241'
    soup = get_dynamic_soup(url)
    class_name = extract_data(soup, 'course')
    class_id = extract_data(soup, 'number')
    instructors = extract_data(soup, 'instructor')
    days = extract_data(soup, 'days')
    start_times = extract_data(soup, 'start')
    end_times = extract_data(soup, 'end')
    locations = extract_data(soup, 'location')
    dates = extract_data(soup, 'dates')
    seats = extract_data(soup, 'seats')
    seats = [seat.replace('\xa0open seats', '') for seat in seats]

    class_information = []
    for class_name,class_id , instructor, day, start_time, end_time, location, date, seat in zip(class_name, class_id, instructors, days, start_times, end_times, locations, dates, seats):
        class_information.append({
            'class_name': class_name,
            'class_id': class_id,
            'instructor': instructor,
            'day': day,
            'start_time': start_time,
            'end_time': end_time,
            'location': location,
            'date': date,
            'seat': seat,
        })
    print(class_information)

parse_classes()
