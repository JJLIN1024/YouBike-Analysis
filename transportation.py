import csv
import time
import pandas as pd
from datetime import datetime
from collections import defaultdict


def convert_time(string):
    clock = time.asctime(time.localtime(int(string)))
    return datetime.strptime(clock, "%a %b %d %H:%M:%S %Y")

file_location = "D:\\大學課程\\大二上\\社會科學程式設計\\Youbike專題\\csv\\201505 data.csv"
location = "D:\\大學課程\\大二上\\社會科學程式設計\\Youbike專題\\csv\\YouBikeStation.csv"

station_info = defaultdict(list)
with open(location, "r") as file:
    csv_reader = csv.DictReader(file)
    for i in csv_reader:
        station_info[i["ID"]] = [i["Name"], i["Total"],
                                 i["Latitude"], i["Longtitude"]]


transport_info = defaultdict(list)
with open(file_location, "r") as file:
    csv_reader = csv.DictReader(file)
    for i in csv_reader:
        transport_info[i["line_id"]] = [i[" rent_station_id"], i[" return_station_id"],
                                        convert_time(i[" rent_time"]), convert_time(i[" return_time"])]

array = []
for k, v in transport_info.items():
    tempt = [v[2], v[3], (v[3] - v[2]).seconds, v[0], station_info[v[0]][0], station_info[v[0]][2],
             station_info[v[0]][3], v[1], station_info[v[1]][0], station_info[v[1]][2], station_info[v[1]][3], v[2].hour]
    array.append(tempt)

headers = ['Rent Time', 'Return Time', 'Trip Duration', 'Rent Station ID', 'Rent Station Name', 'Rent Station Latitude',
           'Rent Station Longitude', 'Return Station ID', 'Return Station Name', 'Return Station Latitude',
           'Return Station Longitude', 'Hour']

df = pd.DataFrame(array, columns=headers)
df.to_csv("201505紀錄.csv")
