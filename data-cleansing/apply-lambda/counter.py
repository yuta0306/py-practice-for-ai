from collections import Counter

# 文字列 description
description = \
"Artificial intelligence (AI, also machine intelligence, MI) is " + \
"intelligence exhibited by machines, rather than " + \
"humans or other animals (natural intelligence, NI)."

# Counterを定義して下さい
c = Counter(description)

# ソートし、上位10要素を出力して下さい
print(sorted(c.items(), key=lambda x:x[1], reverse=True)[:10])