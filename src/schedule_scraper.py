import asyncio
from bs4 import BeautifulSoup
from playwright.async_api import async_playwright


async def get_dynamic_soup(url: str) -> BeautifulSoup:
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto(url)
        await page.wait_for_selector("div#class-results")
        content = await page.content()
        soup = BeautifulSoup(content, "html.parser")
        await browser.close()
        return soup


async def extract_data(soup, class_name):
    elements = soup.find_all('div', class_=class_name)
    return [element.text.strip() for element in elements]


async def parse_classes(subject: str, course_number: int, term: int):
    url = f'https://catalog.apps.asu.edu/catalog/classes/classlist?campusOrOnlineSelection=A&catalogNbr={course_number}&honors=F&promod=F&searchType=all&subject={subject}&term={term}'
    soup = await get_dynamic_soup(url)
    class_name = await extract_data(soup, 'course')
    class_id = await extract_data(soup, 'number')
    instructors = await extract_data(soup, 'instructor')
    days = await extract_data(soup, 'days')
    start_times = await extract_data(soup, 'start')
    end_times = await extract_data(soup, 'end')
    locations = await extract_data(soup, 'location')
    dates = await extract_data(soup, 'dates')
    seats = await extract_data(soup, 'seats')
    seats = [seat.replace('\xa0open seats', '') for seat in seats]

    class_information = []
    for class_name, class_id, instructor, day, start_time, end_time, location, date, seat in zip(class_name, class_id,
                                                                                                 instructors, days,
                                                                                                 start_times, end_times,
                                                                                                 locations, dates,
                                                                                                 seats):
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

    # Remove the first element because it is the header
    class_information.pop(0)
    return class_information
