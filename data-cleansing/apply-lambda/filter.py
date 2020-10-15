import re
# time_list..."年/月/日_時:分"
time_list = [
    "2006/11/26_2:40",
    "2009/1/16_23:35",
    "2014/5/4_14:26",
    "2017/8/9_7:5",
    "2017/4/1_22:15"
]
# 文字列の"月"が条件を満たすときにTrueを返す関数を作成して下さい
def is_month(time):
    time = re.split('\/|_|:', time)
    return True if int(time[1]) < 7 else False

# 上で作った関数を用いて条件を満たす要素を抜き出し、配列にして下さい
months = list(filter(is_month, time_list))

# 配列を出力して下さい
print(months)