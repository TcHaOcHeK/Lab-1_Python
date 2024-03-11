from bs4 import BeautifulSoup # импортируем библиотеку BeautifulSoup
import requests # импортируем библиотеку requests
import math

def pars():
    count = 0
    end = []
    description = { 'Name':[], 'Writer':[], 'Price':[]}
    url = 'https://www.chitai-gorod.ru/search?phrase=python&page={}'# передаем необходимы URL адрес
    while True:
        count += 1
        page = requests.get(url.format(count)) # отправляем запрос методом Get на данный адрес и получаем ответ в переменную
        print(page.status_code) # смотрим ответ
        if page.status_code != 200:
            break

        soup = BeautifulSoup(page.text, "html.parser") # передаем страницу в bs4
        block = soup.findAll('article') # находим  контейнер с нужным классом
        for data in block: # проходим циклом по содержимому контейнера
            description['Name'].append(data.find('div', class_='product-title__head').text.replace("\n", ""))
            description['Writer'].append(data.find('div', class_='product-title__author').text.replace("\n", ""))
            if data.find('div', class_='product-price__value product-price__value--discount'):
                description['Price'].append(data.find('div', class_='product-price__value product-price__value--discount').text.replace("\n", ""))
            else:
                description['Price'].append("no prise")


    return description