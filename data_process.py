# -*- coding: utf-8 -*-
import pandas as pd
import Config
import os
# first version
# do not use the app information
df_train = pd.read_csv(os.path.join(Config.DATA_DIR,Config.MINI_TRAIN_FILE))
df_user = pd.read_csv(os.path.join(Config.DATA_DIR,Config.USER_FILE))
df_user_appaction = pd.read_csv(os.path.join(Config.DATA_DIR,Config.USER_APP_ACTIONS))
df_ad = pd.read_csv(os.path.join(Config.DATA_DIR,Config.AD_FILE))
df_position = pd.read_csv(os.path.join(Config.DATA_DIR,Config.POSITION_PATH))
df_app_cat = pd.read_csv(os.path.join(Config.DATA_DIR,Config.APP_CATEGORIES))
df_user_install = pd.read_csv(os.path.join(Config.DATA_DIR,Config.USER_INSTALLED_APP))



print df_user.head(10)
print df_user_appaction.head(10)
print df_ad.head(10)
print df_position.head(10)
print df_app_cat.head(10)
print df_user_install.head(10)
print "???"