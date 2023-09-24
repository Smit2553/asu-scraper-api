import schedule_scraper


def make_schedule(subject: str, course_number: int, term: int):
    course_information = schedule_scraper.parse_classes(subject, course_number, term)
    print(course_information)


def get_user_information():
    subject = input('Enter the subject: ').upper()
    course_number = int(input('Enter the course number: '))
    term = str(input('Enter the term: ')).lower()
    year = int(input('Enter the year: '))
    if term == 'spring':
        term_number = 1
    elif term == 'summer':
        term_number = 4
    elif term == 'fall':
        term_number = 7
    year = str(year)[-2:]
    final_term = int(f'2{year}{term_number}')
    make_schedule(subject, course_number, final_term)


get_user_information()
