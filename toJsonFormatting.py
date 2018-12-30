import csv
import json
import datetime
from collections import defaultdict, namedtuple, deque


def csv_location(i):
    return f"D:\\大學課程\\大二上\\社會科學程式設計\\Youbike專題\\201812{i}.csv"


def json_location(i):
    return f"D:\\大學課程\\大二上\\社會科學程式設計\\Youbike專題\\csv\\201812{i}.json"


info = defaultdict(list)
for i in range(15, 24):
    try:
        with open(csv_location(i), 'r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for line in csv_reader:
                name = line['場站名稱']
                try:
                    delta = int(line["目前停車輛數"]) - int(info[name][-1][1])
                except:
                    delta = 0

                info[name].append([line["總停車格"], line["目前停車輛數"], line["資料更新時間"],
                                   line["空位數量"], delta])
    except:
        print("wrong file path!!!")


current = 15
write_data = defaultdict(list)
for i in range(9):
    for names in info:
        for element in info[names]:
            if int(element[2][6:8]) == current:
                write_data[names].append(element)
            elif int(element[2][6:8]) < current:
                continue
            else:
                break
    with open(json_location(current), "w+") as file:
        json.dump(write_data, file)
    write_data.clear()
    current += 1
