import pandas as pd
from pandas import DataFrame

dupli_data = DataFrame({"col1":[1, 1, 2, 3, 4, 4, 6, 6, 7, 7, 7, 8, 9, 9]
                       ,"col2":["a", "b", "b", "b", "c", "c", "b", "b", "d", "d", "c", "b", "c", "c"]})
# ここに解答を記述してください
dupli_data.drop_duplicates()