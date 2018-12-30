import csv
import numpy as np
from six.moves import cPickle as pickle


def main(path_pickle, path_csv):
    with open(path_pickle, 'rb') as f:
        x = pickle.load(f)

    with open(path_csv, 'w', encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(info)
        for line in x:
            writer.writerow(list(line.values()))

info = ['場站代號', '場站名稱', '總停車格', '目前停車輛數', '場站區域', '資料更新時間',
        '經度', '緯度', '地址', '場站區域英文名稱', '場站英文名稱', '英文地址', '空位數量', '禁用狀態']

# change the file location and run
for i in range(15, 24):
    pickle_file_location = f"D:\\大學課程\\大二上\\社會科學程式設計\\Youbike專題\\pickle\\ubike201812{i}.pkl"
    csv_file_location = f"D:\\大學課程\\大二上\\社會科學程式設計\\Youbike專題\\csv\\201812{i}.csv"
    try:
        main(pickle_file_location, csv_file_location)
    except:
        print("You should change the file location!!!")
