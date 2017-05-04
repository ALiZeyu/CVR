# -*- coding: utf-8 -*-
import pandas as pd
from Base import BaseObj
from Base import Manager


class App(BaseObj):
    def __init__(self,list):
        super(App, self).__init__()
        self.appID = list[0]
        self.appCategory = list[1]
        self.install_time = 0

    def set_install_time(self,time):
        self.install_time = time


class AppManager(Manager):
    def __init__(self,filename):
        super(AppManager, self).__init__(filename,App)
        self.name = 'app_manager'

    def add_instance(self, inst):
        super(AppManager, self).addInst(inst.appID,inst.label)
