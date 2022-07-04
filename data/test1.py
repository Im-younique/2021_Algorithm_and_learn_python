import pandas as pd
import numpy as np

df = pd.DataFrame(
    {'name': ['KIM', 'LEE', 'SMITH', 'BROWN', 'MILLER'],
     'age': [24, 32, 43, 24, np.nan],
     'height': [178, 168, 171, 185, 176],
     'sex': ['M', 'F', 'F', 'M', 'F']})

print(df[['age', 'height']].mean(axis=2))
print(df)
