'''
Executes functions defined in dd_mod.py
'''

# print('wow python')

# from dd_lambdata.dd_mod import km_to_mile

# print(km_to_mile(40))

from sklearn.model_selection import train_test_split
import pandas as pd
from dd_lambdata.dd_mod import t_val_t


df = pd.DataFrame({
    'year': [32,32,32,32,32,32,32,32,32,32,32,32,32,32,32],
    'month': [1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2],
    'day': [25, 26, 27, 28, 29, 30, 31, 1, 2, 3, 4, 5, 6, 7, 8],
    'state': ['FL', 'FL', 'FL', 'GA', 'GA', 'AL', 'AL', 'MS', 'MS',
            'AR', 'AR', 'OK', 'TX', 'TX', 'TX'],
    'camo': ['urban', 'summer', 'urban', 'autumn', 'urban', 'autumn',
            'urban', 'autumn', 'urban', 'autumn', 'urban', 'winter',
            'winter', 'urban', 'arid']
    })

a,b,c,d = t_val_t(df)

print(a)