import json
import pandas as pd

normalized_data=[]

with open('views.json, 'r') as f:
    data=json.load(f)

for i in data.items():
    normalized_data.append(i[0])

df = pd.DataFrame(normalized_data)

print(df)

