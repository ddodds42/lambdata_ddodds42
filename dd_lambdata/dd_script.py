'''
Executes functions defined in dd_mod.py
'''

# print('wow python')

# from dd_lambdata.dd_mod import km_to_mile

# print(km_to_mile(40))

from sklearn.model_selection import train_test_split
import pandas as pd
from dd_mod import t_val_t, MetricConvert


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

''' print(a) for explore set, print(b) for test set, c for val,
and d for train
'''
print(a)

class Length(MetricConvert):
        '''
        Metric Converter for inches and centimeters
        '''
        def __init__(self, intr=0, old_unit="inch", coeff=2.54,
        si_unit="centimeter"):
                super().__init__(intr, old_unit, coeff, si_unit)
                self.intr = intr
                self.old_unit = old_unit
                self.coeff = coeff
                self.si_unit = si_unit

inchworm = Length()

print(inchworm.si_to_old(30))