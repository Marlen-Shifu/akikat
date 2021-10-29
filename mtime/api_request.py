import requests

import datetime

from .models import City


def request_api(city_name='Алматы'):
    city = City.objects.get(name=city_name)
    current_date = datetime.date.today()
    response = requests.get(f'https://namaz.muftyat.kz/kk/api/times/{current_date.year}/{city.shirota}/{city.dolgota}')
    json_data = response.json()
    data_to_return = get_today_from_json_data(json_data['result'], current_date.strftime('%d-%m-%Y'))
    return data_to_return


def get_today_from_json_data(results, today):
    for result in results:
        if result['date'] == today:
            return result
