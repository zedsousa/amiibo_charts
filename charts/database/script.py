import pandas as pd
import json
df = pd.read_csv('charts/database/amiibo.csv')

df2 = df.groupby('gameSeries').count()
df2 = df2.rename(columns={"amiiboSeries": "quantity"})
df2 = df2[['quantity']]
result2 = df2.to_json(orient="index")
parsed2 = json.loads(result2)
print(json.dumps(parsed2, indent=4))  

df3 = df.groupby('amiiboSeries').count()
df3 = df3.rename(columns={"gameSeries": "quantity"})
df3 = df3[['quantity']]
result3 = df3.to_json(orient="index")
parsed3 = json.loads(result3)
print(json.dumps(parsed3, indent=4)) 


