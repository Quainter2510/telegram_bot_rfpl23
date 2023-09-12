import requests
from bs4 import BeautifulSoup
from helper_function.datetime_func import *
from config_data import config

def parser():
    response = requests.get(config.URL)
    soup = BeautifulSoup(response.text, 'html.parser')
    quotes = soup.find('div', class_="cal_sort_tour").find_all("div")
    res = []
    for i in range(len(quotes)):
        quote1 = quotes[i].find_all("li")
        quote2 = quotes[i].find_all("a")
        dt = datetime_transform(quote1[0].text)
        res.append([dt, quote1[1].text, quote2[0].text])
    res.sort(key=lambda x: x[0])
    for i in range(len(res)):
        res[i].insert(0, i // config.COUNT_MATCHES_IN_TOUR + 1)
    print(res)
    # res = list(filter(lambda x: x[0] == tour, q))
    return res