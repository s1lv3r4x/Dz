import random
import pandas as pd

lst = ['robot'] * 10
lst += ['human'] * 10
# print(lst)
random.shuffle(lst)
# print(lst)
data = pd.DataFrame({'whoAmI': lst})
data.head()
print(data)
clmn_name = data['whoAmI'].unique()
# print(clmn_name)
on_hot = pd.DataFrame(0, index=data.index, columns=clmn_name)
print(on_hot)
for numb in clmn_name:
    on_hot.loc[data['whoAmI'] == numb, numb] = 1
print(on_hot)
