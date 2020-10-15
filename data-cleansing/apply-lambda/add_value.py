from collections import defaultdict

# まとめたいデータ price...(名前, 値段)
price = [
    ("apple", 50),
    ("banana", 120),
    ("grape", 500),
    ("apple", 70),
    ("lemon", 150),
    ("grape", 1000)
]
# defaultdict を定義して下さい
prices = defaultdict(list)


# 上記の例と同様にvalue の要素に値段を追加して下さい
for p in price:
    prices[p[0]].append(p[1])


# 各value の平均値を計算し、配列にして出力して下さい
print([
        sum(p) / len(p)
            for p in prices.values()
    ])