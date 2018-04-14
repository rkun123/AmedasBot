from pyon import Pyon
import datetime

class YesterdayUtil:
    def __init__(self):
        self.FILEPATH = "./yesterdayData.json"
        self.pyonObj = Pyon(self.FILEPATH)
        self.existsData = self.pyonObj.read()

    #今日の日付をオブジェクトとして返す
    def todayDate(self):
        _today = datetime.datetime.today()
        _res = {}
        _res["month"] = _today.month
        _res["day"] = _today.day
        return _res

    #今回の観測データをjsonへ書き込む
    def update(self,_newData):
        _idx = int(_newData["time"])
        _existsData = self.existsData
        if _existsData["data"][-1]["date"] == self.todayDate():
            _existsData["data"][-1]["datas"].append(_newData)
            self.pyonObj.write(_existsData)
        else:
            _existsData["data"].append({"date":self.todayDate()})
            _existsData["data"][-1]["datas"] = [_newData]
            self.pyonObj.write(_existsData)
    def read(self):
        return self.pyonObj.read()["data"]


if __name__ == "__main__":
    yu = YesterdayUtil()
    yu.update({"time":"2"})
