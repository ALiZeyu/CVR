# -*- coding: utf-8 -*-
import pandas as pd
from Base import BaseObj
from Base import Manager


class User(BaseObj):
    def __init__(self,list):
        super(User, self).__init__()
        self.userID = list[0]
        self.age = list[1]
        self.gender = list[2]
        self.education = list[3]
        self.marriageStatus = list[4]
        self.haveBaby = list[5]
        self.hometown = list[6]
        self.residence = list[7]
        self.app_list = []

    def add_installed_app(self,app):
        self.app_list.append(app)

    def add_app_action(self,app,time):
        app.set_install_time(time)
        self.app_list.append(app)

    # def add_click_action(self,label,creative,time):
    #     print '?'

    def create_user_feature(self):
        list = []
        for a in [self.age,self.gender,self.education,self.marriageStatus,self.haveBaby,self.hometown,self.residence]:
            list.append(float(a))
        return list


class UserManager(Manager):
    def __init__(self, filename):
        super(UserManager, self).__init__(filename,User)
        self.name = 'user_manager'

    def add_instance(self,inst):
        super(UserManager, self).addInst(inst.userID,inst.label)


