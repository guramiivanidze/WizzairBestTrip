from datetime import date
from calendar import monthrange
from datetime import datetime, timedelta
import requests
from datetime import date
from datetime import datetime
from datetime import timedelta
import pandas as pd
from tqdm import tqdm


# FROM = 'KUT'
# TO = 'AUH'
# INTERVAL = 7
# USER_PRICE = 123

def get_dates_first_and_last():
    current_date = date.today()
    current_month = current_date.month
    current_year = current_date.year

    last_day_of_current_month = monthrange(current_year, current_month)[1]

    next_dates = [
        (date((current_month + i - 1) // 12 + current_year, (current_month + i - 1) % 12 + 1, 1),
         date((current_month + i - 1) // 12 + current_year, (current_month + i - 1) % 12 + 1, monthrange((current_month + i - 1) // 12 + current_year, (current_month + i - 1) % 12 + 1)[1]))
        for i in range(1, 10)
    ]

    date_ranges_for_request = {
        f"{current_date}": f"{date(current_year, current_month, last_day_of_current_month)}",
        **{f"{start_date}": f"{end_date}" for start_date, end_date in next_dates}
    }

    # print('Dates generated successfully')
    return date_ranges_for_request


# # აქ მზადდება ის თარიღები რომლებიც უნდა გავაყოლოთ რექვესთს. თვის დასაწყისი და თვის დასასრული
# # ანუ საიდან სადამდეც გვინდა ფრენები(მეტ რეინჯზე აერორებს)


first_last_dates = get_dates_first_and_last()
first_last_dates


def dates_and_price(flights):
    requested_dates_and_prices = {}
    for n in flights:
        price_type = n.get('priceType')
        departure_date = str(n['departureDate'])[:10]
        requested_dates_and_prices[departure_date] = {
            "price": n['price']['amount'] if price_type == 'price' else 1000000,
            "currencyCode": n['price']['currencyCode'] if price_type == 'price' else 'Not Visible'
        }
    return requested_dates_and_prices
# # ეს ფუნქცია აბრუნებს საიდან სად მიდიხარ ყველა რეისს და ფასებს;
# # პარამეტრები:
# # saidan - გაფრენის ლოკაციის კოდი
# # sad - ჩასვლის ლოკაციის კოდი
# # direct - ვინაიდან აპიში ბრუნდება ორივე გაფრენის დაგამოფრენის ფრენებიც მოცემულ პარამეტრში გადაეცემა შესაბამისი
# #           outboundFlights ან returnFlights  და თუ არ გავატანთ ამ პარამეტრს ორივე ერთად დაბრუნდება
# #
# # ესეთ ფორმატს  აბრუნებბ :
# # {'2023-07-16': {'price': 419.0, 'currencyCode': 'GEL'},
# #  '2023-07-17': {'price': 379.0, 'currencyCode': 'GEL'},}


def get_dates_and_price(saidan, sad, direct):
    headers = {
        'authority': 'be.wizzair.com',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9,ka;q=0.8,la;q=0.7,ru;q=0.6',
        'content-type': 'application/json;charset=UTF-8',
        'origin': 'https://wizzair.com',
        'referer': 'https://wizzair.com/ka-ge/flights/fare-finder/%E1%83%A5%E1%83%A3%E1%83%97%E1%83%90%E1%83%98%E1%83%A1%E1%83%98/%E1%83%90%E1%83%91%E1%83%A3%E1%83%93%E1%83%90%E1%83%91%E1%83%98',
        'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    }

    outboundflights_dates_and_prices = []
    returnFlights_dates_and_prices = []

    # progress_bar_1 = tqdm(total=len(first_last_dates))
    for key, value in get_dates_first_and_last().items():
        json_data = {
            'flightList': [
                {
                    'departureStation': saidan,
                    'arrivalStation': sad,
                    'from': key,
                    'to': value,
                },
                {
                    'departureStation': sad,
                    'arrivalStation': saidan,
                    'from': key,
                    'to': value,
                },
            ],
            'priceType': 'regular',
            'adultCount': 1,
            'childCount': 0,
            'infantCount': 0,
        }

        url = 'https://be.wizzair.com/17.8.0/Api/search/timetable'

        try:
            response = requests.post(url, headers=headers, json=json_data)
            response.raise_for_status()  # Raise an exception for any failed request
            response_json = response.json()
            outboundflights_dates_and_prices.extend(
                response_json.get('outboundFlights', []))
            returnFlights_dates_and_prices.extend(
                response_json.get('returnFlights', []))
        except requests.exceptions.RequestException as e:
            print(f"Error occurred during the request: {e}")
            # You can handle the error as per your requirements

    if direct == 'outboundFlights':
        # print('Outbound flights dates and prices successfully loaded')
        return dates_and_price(outboundflights_dates_and_prices)

    if direct == 'returnFlights':
        # print('Return flights dates and prices successfully loaded')
        return dates_and_price(returnFlights_dates_and_prices)

    # print('Return and outbound flights dates and prices successfully loaded')
    return dates_and_price(outboundflights_dates_and_prices), dates_and_price(returnFlights_dates_and_prices)


# outboundflights = get_dates_and_price(
#     saidan=FROM, sad=TO, direct='outboundFlights')
# returnFlights = get_dates_and_price(
#     saidan=FROM, sad=TO, direct='returnFlights')

# ყველაზე დაბალი ფასი და ის თარიღები როცა ეს ფასია პარამეტრად იღებს ფრენების თარიღებს და ფასებს
# იღებს შემდეგი ფორმატით დატას:
# {'2023-07-16': {'price': 419.0, 'currencyCode': 'GEL'},
# '2023-07-17': {'price': 379.0, 'currencyCode': 'GEL'},}
# მიღებულ დატაში პოულობს ყველაზე დაბალ ფასს
# პოულობს იმ თარიღებს რომელსაც ყველაზე დაბალი ფასი
# აბრუნებს როგორც დაბალ ფასს ასევე თარიღების ლისტს
# დაბრუნებული შედეგის ფორმატი:
# lowest_price - float
# lowest_price_dates - list - -['2023-08-13', '2023-08-14', '2023-08-18', '2023-08-21',]


def find_best_price_range(flight, price_or_dates):
    lowest_price = float('inf')
    lowest_price_dates = []

    for date, data in flight.items():
        price = data['price']
        if price < lowest_price:
            lowest_price = price
            lowest_price_dates = [date]

        elif price == lowest_price:
            lowest_price_dates.append(date)

    if price_or_dates == 'price':
        return str(lowest_price) + 'gel'
    elif price_or_dates == 'dates':
        return lowest_price_dates


# ყველაზე დაბალი ფასი გაფრენის და თარიღები როცა ეს ფასია
# best_price_for_gafrena, best_dates_for_gafrena = find_best_price_range(
#     outboundflights)

# # დაბრუნების საუკეთესო ფასი და თარიღები როცა ეს ფასია
# best_price_for_dabruneba, best_dates_for_dabruneba = find_best_price_range(
#     returnFlights)


# 3 მოვძებნოთ ამ ფასებიდან დავადგინოთ საუკეთესო მგზავრობის ხანგრძლივობა (ფასის მიხედვით როდის გაფრენა და დაბრუნება ჯობია)
def get_Best_dates_for_rest(departure_dates, return_dates, interval, price_for_gafrena, price_for_dabruneba):
    return_flights = []
    for departure_date in departure_dates:
        departure_datetime = datetime.strptime(departure_date, "%Y-%m-%d")
        for return_date in return_dates:
            return_datetime = datetime.strptime(return_date, "%Y-%m-%d")
            if (return_datetime - departure_datetime) == timedelta(days=interval):
                return_flights.append({'გაფრენა': departure_date,
                                       'გაფრენის ფასი': price_for_gafrena,
                                       'დაბრუნება': return_date,
                                       'დაბრუნების ფასი': price_for_dabruneba,
                                       'STATUS': "ACTIVE"
                                       })

    if len(return_flights) == 0:
        return_flights = [{
            'გაფრენა': departure_dates,
            # 'გაფრენის ფასი': 'empty',
            'დაბრუნება': return_dates,
            # 'დაბრუნების ფასი': 'empty',
            'STATUS': "ERROR ცოტა ფრენაა დაბალი ფასით "
        }]

    return return_flights


def get_only_uniq_prices_for_flights(outboundflights, returnflights):
    prices = []
    for i in outboundflights:
        prices.append(outboundflights[i]['price'])
    for i in returnflights:
        prices.append(returnflights[i]['price'])
    prices.sort()
    uniq_prices = list(set(prices))
    uniq_prices.sort()

    return uniq_prices


# just_prices = get_only_uniq_prices_for_flights(outboundflights)


# აქ რა ფასზეც გვინდა რომ მოვიძიოთ ფრენები იმას ვაბრუნებთ

def user_requested_price_flights(user_price, flights):
    user_price_dates = [
        key for key, value in flights.items() if value['price'] == user_price]
    # print('Dates for the price requested by the user successfully loaded')
    return user_price_dates


