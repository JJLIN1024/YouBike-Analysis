import time
import json
import pickle
import requests


def download_file(youbike_data=[]):
    json_data = []
    url = "http://data.taipei/youbike"
    results = requests.get(url)
    data = json.loads(results.text, encoding="utf-8")
    json_data.append(data)

    for k, v in json_data[0]["retVal"].items():
        youbike_data.append(v)

    write_file(youbike_data)
    return


def write_file(youbike_data):
    file_location = "ubike.pkl"
    with open(file_location, "wb") as file:
        pickle.dump(youbike_data, file)

    with open(file_location, "rb") as file:
        file = pickle.load(file)
        print(file)


while True:
    print("start\n")
    download_file()
    print("\nFinish!!!\n")
    time.sleep(300)
