
def convertTime(time_int):
    DD = time_int/10000
    HH = (DD%10000)/100
    MM = time_int%100
    ret = (DD-17)*24*60 + HH * 60 + MM
    return ret