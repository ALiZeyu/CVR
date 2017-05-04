# -*- coding: utf-8 -*-
import pandas as pd
from Base import BaseObj
from Base import Manager
class Advertise(BaseObj):
    def __init__(self,list):
        BaseObj.__init__(self)
        self.creativeID = list[0]
        self.adID = list[1]
        self.camgaignID = list[2]
        self.advertiserID = list[3]
        self.appID = list[4]
        self.appPlatform = list[5]


#统计每个creative的点击下载率，
#ps 每个广告的点击下载率
class AdManager(Manager):
    def __init__(self,filename):
        super(AdManager, self).__init__(filename,Advertise)
        self.name = 'ad_manager'


    def add_instance(self,inst):
        creative = super(AdManager, self).get_by_id(inst.creativeID)
        inst.adID = creative.adID
        inst.appID = creative.appID
        super(AdManager, self).addInst(inst.creativeID,inst.label)





