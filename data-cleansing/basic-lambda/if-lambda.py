# 代入する引数a1, a2
a1 = 13
a2 = 32

# lambdaを用いてfunc5を作成して下さい
func5 = lambda a: a**2 - 40*a + 350 if 10 <= a < 30 else 50

# 返り値の出力
print(func5(a1))
print(func5(a2))