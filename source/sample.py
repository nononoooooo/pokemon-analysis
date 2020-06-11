#!/bin/python
import csv
import numpy as np

with open("./dataset/pokemon_status.csv", encoding='utf-8') as csv_file:
    csv_data =[(row["図鑑番号"], row["ポケモン名"], row["タイプ１"], row["タイプ２"], row["合計"]) 
        for row in csv.DictReader(csv_file) if not "-" in row["図鑑番号"] and row["合計"].isdigit()]

max_total_index = np.argmax([col[4] for col in csv_data])
print("最大:{}".format(csv_data[max_total_index][1]))

min_total_index = np.argmin([col[4] for col in csv_data])
print("最小:{}".format(csv_data[min_total_index][1]))

# get unique type
type1 = [col[2] for col in csv_data]
type2 = [col[3] for col in csv_data]
unique_type = set(set(type1) & set(type2))
print(unique_type)

type_count = {}
for type_name in unique_type:
    type_count[type_name] = type1.count(type_name) + type2.count(type_name)
print(type_count)
