# -*- coding: utf-8 -*-
from Util import convertTime
class Instance(object):
    def __init__(self,list):
        self.label = list[0]
        self.clickTime = convertTime(list[1])
        self.conversionTime = convertTime(list[2])
        self.creativeID = list[3]
        self.userID = list[4]
        self.positionID = list[5]
        self.connectionType = list[6]
        self.telecomsOperator = list[7]



