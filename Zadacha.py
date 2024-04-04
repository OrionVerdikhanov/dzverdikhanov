import pandas as pd
import random

lst = ['robot'] * 10 + ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

data['robot'] = data['whoAmI'].map(lambda x: 1 if x == 'robot' else 0)
data['human'] = data['whoAmI'].map(lambda x: 1 if x == 'human' else 0)

data.head()
