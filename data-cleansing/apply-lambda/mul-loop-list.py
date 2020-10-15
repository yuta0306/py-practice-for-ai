# 二進数の桁
fours_place = [0, 1]
twos_place  = [0, 1]
ones_place  = [0, 1]

# リスト内包表記の多重ループを用いて0から7までの整数を計算し、配列にして下さい
data = [
        fours*4 + twos*2 + ones
            for fours in fours_place
                for twos in twos_place
                    for ones in ones_place
    ]

# 出力して下さい
print(data)
