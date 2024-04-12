import datetime
from dateutil.relativedelta import relativedelta
import csv

def read_data(filename, product_name):
    data = []
    today = datetime.date.today()
    last_month_date = today - relativedelta(months=1)
    
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for line in reader:
            product, date_str, price = line
            date = datetime.datetime.strptime(date_str, '%Y-%m-%d').date()
            if product.strip() == product_name and date >= last_month_date:
                data.append((date, float(price)))
                
    data.sort()
    return data

def analyze_price_changes(data):
    if not data:
        return "No data available for analysis."
    
    start_price = data[0][1]
    end_price = data[-1][1]
    price_change = end_price - start_price
    return {
        "start_price": start_price,
        "end_price": end_price,
        "price_change": price_change
    }
