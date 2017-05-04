import Config
import os
#sample 30000 data from train data
num_sample = 50
with open(os.path.join(Config.DATA_DIR,Config.AD_FILE), 'rb') as fi:
    with open(os.path.join(Config.DATA_DIR,Config.MINI_AD_FILE), 'wb') as fo:
        for i in range(num_sample):
            fo.write(fi.readline())