import requests
from bs4 import BeautifulSoup
from helper_function.datetime_func import *
from config_data import config, relations


def parser():
    response = requests.get(config.URL)
    soup = BeautifulSoup(response.text, 'html.parser')
    quotes = soup.find('div', class_="cal_sort_date").find_all("div")
    res = []
    for i in range(len(quotes)):
        quote1 = quotes[i].find_all("li")
        quote2 = quotes[i].find_all("a")
        res.append([i // config.COUNT_MATCHES_IN_TOUR + 1, relations.DATES_TOUR[i // config.COUNT_MATCHES_IN_TOUR + 1] + quote1[0].text, quote1[1].text, quote2[0].text])
    res.sort(key=lambda x: x[0])
    return res