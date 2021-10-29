from django import template

import requests
from bs4 import BeautifulSoup as bs

register = template.Library()


@register.simple_tag
def get_date():

    res = requests.get('https://www.muftyat.kz/kk/login/')

    parser = bs(res.text, 'html.parser')

    time_g = parser.find('p', {'class': 'i-grig'}).text
    time_h = parser.find('span', {'class': 'chauil'}).text

    time = {'gr': time_g, 'hj': time_h}

    return time