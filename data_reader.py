# -*- coding: utf-8 -*-
from Objects.Advertise import Advertise
from Objects.App import App
from Objects.Position import Position
from Objects.User import User
from Objects.Advertise import AdManager
from Objects.App import AppManager
from Objects.Position import PosManager
from Objects.User import UserManager

import Config
import os
import pandas as pd

print 'read ad.csv'
ad_manager = AdManager(os.path.join(Config.DATA_DIR,Config.AD_FILE))

print 'read app_categories.csv'
app_manager = AppManager(os.path.join(Config.DATA_DIR,Config.APP_CATEGORIES))

print 'read position.csv'
pos_manager = PosManager(os.path.join(Config.DATA_DIR,Config.POSITION_PATH))

print 'read user.csv'
user_manager = UserManager(os.path.join(Config.DATA_DIR,Config.USER_FILE))

print 'read user_installed_apps.csv'
# df_user_install = pd.read_csv(os.path.join(Config.DATA_DIR,Config.USER_INSTALLED_APP))
# for val in df_user_install.values:
#     user_manager[val[0]].add_installed_app(app_map[val[1]])

print "???"