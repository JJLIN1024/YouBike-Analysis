import folium
import json
from folium.plugins import Draw

mapbox = "https://api.mapbox.com/v4/mapbox.streets/{z}/{x}/{y}.png?access_token=pk.eyJ1IjoiYWFyb24wMjIxIiwiYSI6ImNqcTBiNHJlZDBqODQ0Mm11aWpqejk4ZWgifQ.ZXaiQzs7b3iwntK9_Nv-0w"

with open("D:\\大學課程\\大二上\\社會科學程式設計\\Youbike專題\\json\\YouBike.json", "r") as f:
    data = (json.load(f))["features"]

with open("D:\\大學課程\\大二上\\社會科學程式設計\\Youbike專題\\json\\MRT.json", "r") as f:
    data1 = (json.load(f))["features"]


myMap = folium.Map(location=[25.03, 121.55], zoom_start=12,
                   prefer_canvas=True, tiles=mapbox, attr="Mapbox attribution")

fg1 = folium.FeatureGroup(name="YouBike")
for i in range(len(data)):
    place = data[i]["geometry"]["coordinates"]
    place = [place[1], place[0]]
    fg1.add_child(folium.Circle(location=place, radius=2, weight=4))

fg2 = folium.FeatureGroup(name="MRT")
for i in range(len(data1)):
    place = data1[i]["geometry"]["coordinates"]
    place = [place[1], place[0]]
    line, name = data1[i]["properties"]["Line"], data1[i]["properties"]["Name"]

    if line == "BR":        # 文湖
        fg2.add_child(folium.Marker(location=place, popup=folium.Popup(name),
                                    icon=folium.Icon(color="gray", icon="subway", prefix="fa")))
    elif line == "G":       # 松山
        fg2.add_child(folium.Marker(location=place, popup=folium.Popup(name),
                                    icon=folium.Icon(color="green", icon="subway", prefix="fa")))
    elif line == "O":       # 蘆洲
        fg2.add_child(folium.Marker(location=place, popup=folium.Popup(name),
                                    icon=folium.Icon(color="orange", icon="subway", prefix="fa")))
    elif line == "R":       # 淡水
        fg2.add_child(folium.Marker(location=place, popup=folium.Popup(name),
                                    icon=folium.Icon(color="red", icon="subway", prefix="fa")))
    elif line == "BL":      # 板南
        fg2.add_child(folium.Marker(location=place, popup=folium.Popup(name),
                                    icon=folium.Icon(color="darkblue", icon="subway", prefix="fa")))
myMap.add_child(fg1)
myMap.add_child(fg2)
folium.LayerControl().add_to(myMap)
Draw(export=True).add_to(myMap)

# myMap.save("C:\\Users\\Aaron\\Desktop\\TaipeiMap.html")
myMap.save("D:\\大學課程\\大二上\\社會科學程式設計\\Youbike專題\\TaipeiMap.html")


# black: tiles="CartoDB dark_matter"
# white: tiles="cartodbpositron"
# tiles="https://api.mapbox.com/v4/mapbox.streets/{z}/{x}/{y}.png?access_token=pk.eyJ1IjoiYWFyb24wMjIxIiwiYSI6ImNqcHBqdGJjZDAzb3AzeG16c3dwNXBydTUifQ.Hz7cZOihH12HwjrFxEDSsw",attr="Mapbox"
