import datetime


def days_in_year(start_date):
    '''determine the list of days left in the year from start_date
    '''

    one_day = datetime.timedelta(days=1)
    next_day = start_date
    result = []
    while next_day.year == start_date.year:
        result.append(next_day)
        next_day += one_day
    return result


def days_in_year_generator(start_date):
    '''determine the list of days left in the year from start_date
    '''

    one_day = datetime.timedelta(days=1)
    next_day = start_date
    while next_day.year == start_date.year:
        yield next_day
        next_day += one_day

if __name__ == '__main__':
    print(days_in_year(datetime.date(2015, 12, 1)))
    print(days_in_year_generator(datetime.date(2015, 12, 1)))
    for d in days_in_year_generator(datetime.date(2015, 12, 1)):
        print(d)
