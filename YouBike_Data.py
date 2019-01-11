import json
from datetime import datetime
from collections import deque, namedtuple, defaultdict

# 把字串轉換成datetime object
def datetimeConverter(datestring):
    return datetime.strptime(datestring, '%Y%m%d%H%M%S')

# 讀取幾月幾號的YouBike站資料,並將其轉換成有效率和方便存取的資料結構
def read_json(day=19, month=10):
    station_dict = defaultdict(deque)
    YouBike = namedtuple(
        'YouBike', 'TotalSpace BikeNum Time EmptySpace Delta')
    for i in range(day, day + 1):
        with open(f'2018{month}{i}.json', 'r') as f:
            file = json.load(f)
            for k, v in file.items():
                for i in range(len(v)):
                    station_dict[k].append(YouBike(TotalSpace=int(v[i][0]), BikeNum=int(v[i][1]),
                                                   Time=datetimeConverter(v[i][2]), EmptySpace=int(v[i][3]),
                                                   Delta=int(v[i][4])))
    return dict(station_dict)
