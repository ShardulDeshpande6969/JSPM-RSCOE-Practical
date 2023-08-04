import pandas as pd 
import io
data = pd.read_csv(io.BytesIO(uploaded['selected-services-march-2023-quarter-csv (1).csv']))
print(data)
