import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
data=pd.read_table('../data/hf_round2_train.txt', header=None,names=['id','年龄','性别','症状1','症状2','症状3'])
data['年龄'].value_counts().sort_values(ascending=False).plot(kind='bar')
plt.show()
print(data.shape)
#print(data['症状3'].value_counts())