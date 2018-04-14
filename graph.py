import numpy as np
from matplotlib import pyplot as plt

class GraphMaker:
    def __init__(self,_data):#get Today's data
        self.data = _data

    def Graphize(self):
        _values = []
        for _data in self.data["datas"]:
            _values.append(float(_data["temp"]))

        print(_values)
        plt.ylim(-10,30)
        plt.xticks([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24])
        plt.plot(range(0,len(self.data["datas"])),_values)
        plt.savefig("./output.png")
