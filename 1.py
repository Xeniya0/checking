# ============================>>> game

name_1 = input('имя 1 игрока')
name_2 = input('имя 2 игрока')

player = {
    'name' : name_1,
    'health' : 100,
    'damage' : 50,
    'armor': 1.2

}
enemy = {
    'name' : name_2,
    'health' : 100,
    'damage' : 50,
    'armor': 1.2

}

def attack(a, b):
    def armor(c, d):
        return(int(c['damage'] / d['armor']))
    global player
    global enemy
    b['health'] -= armor(a, b)
    print(f'игрок {a["name"]} ударил игрoка {b["name"]} на {armor(a, b)}')
    print(f'у игрока {b["name"]} осталось здоровья {b["health"]}')
    if b['health'] <= 0:
        print(b["name"], 'погиб')

attack(player, enemy)
attack(player, enemy)
attack(player, enemy)


# ============ расстояние  между точками >>>

import math

x1 = 10
y1 = 10
x2 = 50
y2 = 100

l = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
print(l)

# ====== фильтр списка чисел >>>>

def my_filter(numbers, functions):
    result = []
    for number in numbers:
        if functions(number):
            result.append(number)
    return result


numbers = [1, 2, 3, 4, 5, 6, 7, 8]

def is_even(number):
    return number % 2 == 0

def is_not_even(number):
    return number % 2 != 0

def big_4(number):
    return number > 4


print(my_filter(numbers, big_4))


# немного json >>>

import pickle
import json

my_favourite_group = {
    'name': 'Г.М.О.',
    'tracks': ['Последний месяц осени', 'Шапито'],
    'Albums': [{'name': 'Делать панк-рок','year': 2016},
    {'name': 'Шапито','year': 2014}]}

with open('group.txt', 'wb') as f:
    pickle.dump(my_favourite_group, f)
print('done')


with open('group.json', 'w', encoding='utf-8') as f:
    json.dump(my_favourite_group, f)
print('done')