# -*- coding: utf-8 -*-
import pandas as pd
from Base import BaseObj
from Base import Manager


class Position(BaseObj):
    def __init__(self,list):
        super(Position, self).__init__()
        self.positionID = list[0]
        self.sitesetID = list[1]
        self.positionType = list[2]

    def create_pos_feature(self):
        list = []
        for a in [self.sitesetID,self.positionType]:
            list.append(float(a))
        return list


class PosManager(Manager):
    def __init__(self, filename):
        super(PosManager, self).__init__(filename, Position)
        self.name = 'pos_manager'

    def add_instance(self,inst):
        super(PosManager, self).addInst(inst.positionID,inst.label)