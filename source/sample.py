#!/bin/python
import csv
import numpy as np

with open("./dataset/pokemon_status.csv", encoding='utf-8') as csv_file:
    csv_data =[(row["図鑑番号"], row["ポケモン名"], row["タイプ１"], row["タイプ２"], row["合計"]) 
        for row in csv.DictReader(csv_file) if not "-" in row["図鑑番号"] and row["合計"].isdigit()]

max_total_index = np.argmax([col[4] for col in csv_data])
print("最大:{}",csv_data[max_total_index][1])

min_total_index = np.argmin([col[4] for col in csv_data])
print("最小:{}",csv_data[min_total_index][1])

# get unique type
type_ = set(set([col[2] for col in csv_data]) & set([col[3] for col in csv_data]))
print(type_)
