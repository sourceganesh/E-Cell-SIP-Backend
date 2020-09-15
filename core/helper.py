from datetime import datetime

#converts string type date to datetime type
def parse_date(string_date):
    date = datetime.strptime(string_date, '%Y-%m-%d')
    return date