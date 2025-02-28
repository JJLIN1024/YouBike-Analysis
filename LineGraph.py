import json
import folium
import csv
from collections import defaultdict
from folium.plugins import Draw


def convert_float(array):
    return [[float(i[0]), float(i[1])] for i in array]


with open("D:\\大學課程\\大二上\\社會科學程式設計\\Youbike專題\\csv\\YouBikeStation.csv", "r") as file:
    data = {}
    csv_reader = csv.reader(file)
    next(csv_reader)
    for i in csv_reader:
        data[i[0]] = [i[3], i[4]]

with open("D:\\大學課程\\大二上\\社會科學程式設計\\Youbike專題\\201505紀錄.csv", "r", encoding="ANSI") as file:
    csv_reader = csv.reader(file)
    info = defaultdict(int)
    next(csv_reader)
    for i in csv_reader:
        trip = i[3] + ":" + i[7]
        reverse = i[7] + ":" + i[3]

        if reverse in info:
            info[reverse] += 1
        else:
            info[trip] += 1

myMap = folium.Map(location=[25.053, 121.575], zoom_start=12,
                   prefer_canvas=True, tiles="cartodbpositron")

group1 = folium.FeatureGroup(name="5 <= nums <= 100")
group2 = folium.FeatureGroup(name="101 <= nums <= 500")
group3 = folium.FeatureGroup(name="501 <= nums <= 1000")
group4 = folium.FeatureGroup(name="nums > 1000")

for k, v in info.items():
    Rent, Return = k.split(":")

    if v < 5:
        continue
    elif 5 <= v <= 100:
        group1.add_child(folium.ColorLine(convert_float([data[Rent], data[Return]]), colors=[
            0, 1], colormap=['#007799', '#007799'], opacity=0.4, weight=0.5))
    elif 101 <= v <= 500:
        group2.add_child(folium.ColorLine(convert_float([data[Rent], data[Return]]), colors=[
            0, 1], colormap=['#00AAAA', '#00AAAA'], weight=1.2))
    elif 501 <= v <= 1000:
        group3.add_child(folium.ColorLine(convert_float([data[Rent], data[Return]]), colors=[
            0, 1], colormap=['#00FFCC', '#00FFCC'], opacity=0.8, weight=1.8))
    else:
        group4.add_child(folium.ColorLine(convert_float([data[Rent], data[Return]]), colors=[
            0, 1], colormap=['#BBFF00', '#BBFF00'], weight=3))


myMap.add_child(group1)
myMap.add_child(group2)
myMap.add_child(group3)
myMap.add_child(group4)
folium.LayerControl().add_to(myMap)
Draw(export=True).add_to(myMap)

myMap.save("D:\\大學課程\\大二上\\社會科學程式設計\\Youbike專題\\White LineGraph.html")
