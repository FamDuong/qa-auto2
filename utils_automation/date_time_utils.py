import dateutil.parser
import datetime


def parse_string_to_date(string_datetime):
    your_date = dateutil.parser.parse(string_datetime)
    return your_date.date()


def how_many_days_til_now(string_datetime):
    number_of_days = datetime.date.today() - parse_string_to_date(string_datetime)
    return number_of_days.days






