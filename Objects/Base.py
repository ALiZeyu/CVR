import pandas as pd
from draw_Util import draw_pic


class BaseObj(object):
    def __init__(self):
        self.total_click = 0
        self.download_click = 0

    def get_click_download_pro(self):
        return float(self.download_click)/self.total_click


class Manager(object):
    def __init__(self,filename,func):
        self.creator = func
        self.map = {}
        df_ad = pd.read_csv(filename)
        for val in df_ad.values:
            self.map[val[0]] = func(val)

    def get_by_id(self,id):
        return self.map[id]

    def addInst(self,id,label):
        obj = self.get_by_id(id)
        obj.total_click += 1
        if label == 1:
            obj.download_click += 1

    def draw_pic(self):
        lst = [val.get_click_download_pro() for val in self.map.values()]
        draw_pic(lst,self.name)



