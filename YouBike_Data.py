import json
from datetime import datetime
from collections import deque, namedtuple, defaultdict


def datetimeConverter(datestring):
    return datetime.strptime(datestring, '%Y%m%d%H%M%S')


def read_json(day=19):
    station_dict = defaultdict(deque)
    YouBike = namedtuple(
        'YouBike', 'TotalSpace BikeNum Time EmptySpace Delta')
    for i in range(day, day + 1):
        with open(f'D:\\大學課程\\大二上\\社會科學程式設計\\Youbike專題\\json\\201810{i}.json', 'r') as f:
            file = json.load(f)
            for k, v in file.items():
                for i in range(len(v)):
                    station_dict[k].append(YouBike(TotalSpace=int(v[i][0]), BikeNum=int(v[i][1]),
                                                   Time=datetimeConverter(v[i][2]), EmptySpace=int(v[i][3]),
                                                   Delta=int(v[i][4])))
    return dict(station_dict)
