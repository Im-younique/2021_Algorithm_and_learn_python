from matplotlib.pyplot import axis
import pandas as pd
import numpy as np

def avg(data):
    res = round(data.mean(axis=1),2)
    return res

def sinmax(data):
    res = data.apply(np.sin)
    res = res.apply(max, axis=1)
    return res

def outlier(data):
    res = (data-data.mean()).abs()>=data.std()
    return res

if __name__ == '__main__':
    mypd = [[5,6,2],[7,3,10]]
    mypd = pd.DataFrame(mypd)
    anpd = [[4, 1 ,10],[4.2, 1.2, 14],[3.8, 0, 1000],[-4, 0.9, 9]]
    anpd = pd.DataFrame(anpd)
    testpd = {"a":{"가":1, "나":4}, "b":{"가":2, "나": 5}, "c":{"가":3, "나":6}}
    testpd = pd.DataFrame(testpd)
    testpd = testpd.drop("가")
    print(avg(mypd))
    print(sinmax(mypd))
    print(outlier(anpd))
    print(testpd)