import json
import pandas as pd

with open('views.json', 'r') as json_data:
	data = json.load(json_data)

for i in range(0, len(data)):
	print(data[i])
