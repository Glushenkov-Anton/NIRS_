import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def read_column():
    result_list = []
    while True:
        x = input("Введите параметр для сортировки (введите end, если параметры выбраны): ")
        if x == "end":
            break
        else:
            result_list.append(x)
    return result_list


def heatmap(x, y, z):
    pivot = excel_data.pivot_table(index=[x], columns=[y], values=z, aggfunc=np.average)

    heatmap = sns.heatmap(pivot)
    heatmap.set_title('Correlation Heatmap', fontdict={'fontsize': 18}, pad=12)

    plt.savefig('heatmap.png', dpi=300, bbox_inches='tight')


def sort(sort_list, result_name):
    result = excel_data.sort_values(by=sort_list)
    result.to_excel(result_name, index=False)


def select_option(cmd):
    if cmd == "heatmap":
        first_value = input("Введите исследуемый элемент: ")
        second_value = input("Введите второе значение: ")
        gradient = input("Градиент распределения: ")
        heatmap(first_value, second_value, gradient)
    elif cmd == "sort":
        sort_file_name = input("Введите название файла для сохранения: ")
        sort_file_name = sort_file_name + '.xlsx'
        sort(read_column(), sort_file_name)
        print("Успешно!")
    elif cmd == "group":
        item = input("Введите атрибут: ")
        parameter = input("Введите параметр для группировки: ")
        group_file_name = input("Введите название файла для сохранения: ")
        result_item = excel_data.loc[excel_data[item] == parameter]
        result_item.to_excel(group_file_name + '.xlsx', index=False)
        print("Успешно!")
    else:
        print("Не найдено, попробуйте еще\n")


while True:
    try:
        file = input("Выберите файл: ")
        excel_data = pd.read_excel(file + '.xlsx')
        command = input("Выберите действие: ")
        select_option(command)
    except KeyError:
        print("Ошибка: один из атрибутов, введенный вами, не найден, попробуйте ещё.\n")
        continue
    except TypeError:
        print("Ошибка: Неверный тип данных.\n")
