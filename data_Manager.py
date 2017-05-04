# -*- coding: utf-8 -*-
from Objects.Advertise import AdManager
from Objects.App import AppManager
from Objects.Position import PosManager
from Objects.User import UserManager
from Objects.Instance import Instance
from Util import convertTime
import Config
import os
import pandas as pd




class data_Manager(object):
    def __init__(self):
        print 'read ad.csv'
        self.ad_manager = AdManager(os.path.join(Config.DATA_DIR, Config.AD_FILE))

        print 'read app_categories.csv'
        self.app_manager = AppManager(os.path.join(Config.DATA_DIR, Config.APP_CATEGORIES))

        print 'read position.csv'
        self.pos_manager = PosManager(os.path.join(Config.DATA_DIR, Config.POSITION_PATH))

        print 'read user.csv'
        self.user_manager = UserManager(os.path.join(Config.DATA_DIR, Config.USER_FILE))

        print 'read user_installed_apps.csv'
        self.read_user_insalled_apps()

        self.inst_list = []

    def read_user_insalled_apps(self):
        df = pd.read_csv(os.path.join(Config.DATA_DIR, Config.USER_INSTALLED_APP))
        for val in df.values:
            user = self.user_manager.get_by_id(val[0])
            app = self.app_manager.get_by_id(val[1])
            user.add_installed_app(app)

    def read_user_app_actions(self):
        df = pd.read_csv(os.path.join(Config.DATA_DIR, Config.USER_APP_ACTIONS))
        for val in df.values:
            user = self.user_manager.get_by_id(val[0])
            time = convertTime(val[1])
            app = self.app_manager.get_by_id(val[2])
            user.add_app_action(app,time)

    def read_train_file(self):
        df = pd.read_csv(os.path.join(Config.DATA_DIR, Config.TRAIN_FILE))
        for val in df.values:
            inst = Instance(val)
            self.inst_list.append(inst)
            self.user_manager.add_instance(inst)
            self.ad_manager.add_instance(inst)
            self.app_manager.add_instance(inst)
            self.pos_manager.add_instance(inst)

m = data_Manager()