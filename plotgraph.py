import csv
import json
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime
from YouBike_Data import read_json


def prepare_data(day=19, name="捷運科技大樓站"):
    station_list = []
    time_list = []
    info_list = read_json(day)[name]
    max_num = info_list[0].TotalSpace
    while info_list:
        tempt = info_list.popleft()
        station_list.append(tempt.BikeNum)
        time_list.append(tempt.Time.time())

    plt.style.use("ggplot")
    plt.rcParams["font.family"] = "Times New Roman"
    plt.fill_between(time_list, station_list, color="skyblue", alpha=0.1)
    plt.plot(time_list, station_list, color="skyblue")
    plt.title(f"10/{day}  {youbike_dict[name]}")
    plt.xlabel("Time")
    plt.xticks(fontsize=9)
    plt.yticks(fontsize=9)
    plt.xlim(("00:00", "23:59"))
    plt.ylim((0, max_num + 5))

    plt.show()


youbike_dict = dict()
with open("D:\\大學課程\\大二上\\社會科學程式設計\\Youbike專題\\csv\\台北市中英對照.csv", "r") as file:
    csv_reader = csv.reader(file)
    next(csv_reader)
    for i in csv_reader:
        youbike_dict[i[0]] = i[2]

    prepare_data(day=20, name="捷運科技大樓站")
