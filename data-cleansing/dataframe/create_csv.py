import csv
# ここに解答を記述してください
with open("./4050_data_cleansing_data/csv0.csv", "w") as f:
    writer = csv.writer(f, lineterminator='\n')
    writer.writerow(["col1", "col2", "col3"])
    