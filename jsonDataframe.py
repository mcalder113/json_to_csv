import json
import pandas as pd

with open('data.json', 'r') as json_data:
    data = json.load(json_data)

#normalize json
normalized_data = pd.json_normalize(data['views'])

df = pd.DataFrame(normalized_data)

print(df)
