# 時間データhour, 分データminute
hour = [0, 2, 3, 1, 0, 1, 1]
minute = [30, 35, 0, 14, 11, 0, 22]

# 時, 分を引数に、分に換算する関数を作成して下さい
def alter(hour, minute):
    return hour * 60 + minute

# リスト内包表記を用いて所定の配列を作成してください
times = [alter(h, m) for h, m in zip(hour, minute)]

# 出力して下さい
print(times)