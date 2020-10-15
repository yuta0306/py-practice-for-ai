import re
# 配列time_list
time_list = [
    "2006/11/26_2:40",
    "2009/1/16_23:35",
    "2014/5/4_14:26",
    "2017/8/9_7:5",
    "2017/4/1_22:15"
]
# 文字列から"時"を取り出す関数を作成して下さい
def split_time(time):
    time = re.split('\/|_|:', time)
    return int(time[3])

# 上で作った関数を用いて各要素の"時"を取り出し、配列にして下さい
hours = list(map(split_time, time_list))

# 配列を出力して下さい
print(hours)