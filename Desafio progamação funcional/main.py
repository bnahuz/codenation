from datetime import datetime as date
import math

records = [
    {'source': '48-996355555', 'destination': '48-666666666', 'end': 1564610974, 'start': 1564610674},
    {'source': '41-885633788', 'destination': '41-886383097', 'end': 1564506121, 'start': 1564504821},
    {'source': '48-996383697', 'destination': '41-886383097', 'end': 1564630198, 'start': 1564629838},
    {'source': '48-999999999', 'destination': '41-885633788', 'end': 1564697158, 'start': 1564696258},
    {'source': '41-833333333', 'destination': '41-885633788', 'end': 1564707276, 'start': 1564704317},
    {'source': '41-886383097', 'destination': '48-996384099', 'end': 1564505621, 'start': 1564504821},
    {'source': '48-999999999', 'destination': '48-996383697', 'end': 1564505721, 'start': 1564504821},
    {'source': '41-885633788', 'destination': '48-996384099', 'end': 1564505721, 'start': 1564504821},
    {'source': '48-996355555', 'destination': '48-996383697', 'end': 1564505821, 'start': 1564504821},
    {'source': '48-999999999', 'destination': '41-886383097', 'end': 1564610750, 'start': 1564610150},
    {'source': '48-996383697', 'destination': '41-885633788', 'end': 1564505021, 'start': 1564504821},
    {'source': '48-996383697', 'destination': '41-885633788', 'end': 1564627800, 'start': 1564626000}
]

def evaluate_price(start, end):
    PERMANENT_TAX = 0.36
    DAYTIME_TAX = 0.09

    if start.hour >= 22 or end.hour < 6:
        return 0.36

    elif end.hour >= 22 and end.minute > 0:
        end = date(end.year, end.month, end.day, 22, 1)

    elif start.hour < 6:
        start = date(start.year, start.month, start.day, 6)

    diference = math.floor((end - start).seconds / 60)
    return ((diference * DAYTIME_TAX) + PERMANENT_TAX)
    
def organize(unsorted_records):
    for record in unsorted_records:
        record['total'] = round(record['total'],2)
    records_sorted = sorted(unsorted_records, key=lambda record: record['total'], reverse = True)
    return records_sorted

def classify_by_phone_number(records):
    resumes = []
    for record in records:
        in_resume = False
        start = date.fromtimestamp(record['start'])
        end = date.fromtimestamp(record['end'])
        total = round(evaluate_price(start,end),2)

        for resume in resumes:
            if record['source'] == resume['source']:
                in_resume = True
                resume['total'] += total

        if not in_resume:
            resumes.append({'source': record['source'], 'total':total})

    return organize(resumes)

    


classify_by_phone_number(records)