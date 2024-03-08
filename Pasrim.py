from bs4 import BeautifulSoup # импортируем библиотеку BeautifulSoup
import requests # импортируем библиотеку requests

def pars():
    url = 'https://www.chitai-gorod.ru/' # передаем необходимы URL адрес
    page = requests.get(url) # отправляем запрос методом Get на данный адрес и получаем ответ в переменную
    print(page.status_code) # смотрим ответ
    soup = BeautifulSoup(page.text, "html.parser") # передаем страницу в bs4

    block = soup.findAll('div', class_='slider__item') # находим  контейнер с нужным классом

    description = { 'Name':['book'], 'Writer':['writer'], 'Price':['book prise']}
    for data in block: # проходим циклом по содержимому контейнера
        description['Name'].append(data.find('div', class_='product-title__head').text.replace("\n", ""))
        description['Writer'].append(data.find('div', class_='product-title__author').text.replace("\n", ""))
        description['Price'].append(data.find('div', class_='product-price__value product-price__value--discount').text)
    return description