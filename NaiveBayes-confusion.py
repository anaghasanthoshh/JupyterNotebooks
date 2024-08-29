import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

mat=np.array([[344 , 13 , 32  , 0],
 [  6 ,364 , 24  , 0],
 [  1 ,  5 ,392 ,  0],
 [  4 , 12 ,187  ,48]])
target_names=['A','B','C','D']

plt.figure(figsize=(10, 8))
sns.heatmap(mat.T, square=True, annot=True, fmt='d', cbar=False,
                     xticklabels=target_names, yticklabels=target_names,
                     cmap='Blues')
plt.xlabel('true label')
plt.ylabel('predicted label')
plt.show()