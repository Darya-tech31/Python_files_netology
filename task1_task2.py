import os
import time
from pprint import pprint

def read_cookbook():
    file_path = os.path.join(os.getcwd(), 'рецепты.txt')
    menu = {}
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            dish_name = line[:-1]
            count = f.readline().strip()
            ing_list = []
            for i in range(int(count)):
                dish_items = dict.fromkeys(['ingredient_name', 'quantity', 'measure'])    # - временный словарь с ингридиетом
                ingridient = f.readline().strip().split(' | ')    # - вот так перемещаемся по файлу
                for item in ingridient:
                    dish_items['ingredient_name'] = ingridient[0]
                    dish_items['quantity'] = ingridient[1]
                    dish_items['measure'] = ingridient[2]
                ing_list.append(dish_items)
                cook_book = {dish_name: ing_list}
                menu.update(cook_book)
            f.readline()
    return menu

def get_shop_list_by_dishes(dishes, person_count):
    ingr_list = dict()
    for dish_name in dishes:  # итерируем список полученных блюд
        if dish_name in menu:
            for ings in menu[dish_name]:  # итерируем ингридиенты в блюде
                meas_quan_list = dict()
                if ings['ingredient_name'] not in ingr_list:
                    meas_quan_list['measure'] = ings['measure']
                    meas_quan_list['quantity'] = ings['quantity'] * person_count
                    ingr_list[ings['ingredient_name']] = meas_quan_list
                else:
                    ingr_list[ings['ingredient_name']]['quantity'] = ingr_list[ings['ingredient_name']]['quantity'] + \
                                                                     ings['quantity'] * person_count

        else:
            print(f'\n"Такого блюда нет в списке!"\n')
    return ingr_list

if __name__ == '__main__':
    filename = "рецепты.txt"
    menu = read_cookbook()
    print('Задача 1')
    time.sleep(1)
    print(menu)
    print('Задача 2')
    pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))
