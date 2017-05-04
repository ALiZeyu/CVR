# -*- coding: utf-8 -*-
from __future__ import division
import matplotlib.pyplot as plt
import pandas as pd
import Config
import os

class Triple(object):
    def __init__(self,first,second,total):
        self.zeros = first
        self.ones = second
        self.total = total

    def add_zero(self,count):
        self.zeros += count
        self.total += count

    def add_one(self,count):
        self.ones += count
        self.total += count

    def click_pro(self):
        return self.ones/self.total

df_train = pd.read_csv(os.path.join(Config.DATA_DIR,Config.MINI_TRAIN_FILE))
df_ad = pd.read_csv(os.path.join(Config.DATA_DIR,Config.AD_FILE),usecols=[0,1])
df_ad = df_ad[['creativeID','adID']]
df_ad['all_count'] = 0
df_ad['click_count'] = 0
df_train = df_train[['label','creativeID']]
print df_train.shape[0]
#print df_train.head(20)
df_tr_0 = df_train[df_train['label'] == 0]
print df_tr_0.shape[0]
#df_tr_0 = df_tr_0['creativeID'].value_counts()
df_tr_1 = df_train[df_train['label'] == 1]
print df_tr_1.shape[0]
#df_tr_1 = df_tr_1['creativeID'].value_counts()

df_tr_0 = df_tr_0.groupby(['creativeID'],as_index=False).count()
df_tr_1 = df_tr_1.groupby(['creativeID'],as_index=False).count()

map = {}

for val in df_tr_0.values:
    creativeID = val[0]
    count = val[1]
    if creativeID in map:
        map[creativeID].add_zero(count)
    else:
        map[creativeID] = Triple(count,0,count)

for val in df_tr_1.values:
    creativeID = val[0]
    count = val[1]
    if creativeID in map:
        map[creativeID].add_one(count)
    else:
        map[creativeID] = Triple(0,count,count)
x = []
y = []
for key,val in map.iteritems():
    print key,val.zeros,val.ones,val.total,val.click_pro()
    x.append(key)
    y.append(val.click_pro())

import numpy as np

#x = np.array(x)
#y = np.array(y)

x=np.random.randn(100)
y=np.random.randn(100)
color=np.random.rand(100)
size=100*np.random.rand(100)
plt.scatter(x,y,c=color,s=size)
plt.show()

#d = df_train.groupby(['adID'],as_index=False)
#d = df_ad.groupby(['adID'],as_index=False) 分组 .count()统计每个组的个数，.sum()分组求和，.mean()分组求平均



