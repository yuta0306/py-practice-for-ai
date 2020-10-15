import pandas as pd

data = {"OS": ["Machintosh", "Windows", "Linux"],
        "release": [1984, 1985, 1991],
        "country": ["US", "US", ""]}
# ここに解答を記述してください
df = pd.DataFrame(data)
csv = df.to_csv(df, "OSlist.csv")