import pandas as pd
# ここに解答を記述してください
df = pd.read_csv('./4050_data_cleansing_data/iris.csv', header=None)

df.columns = ["sepal length", "sepal width", "petal length", "petal width", "class"]

df