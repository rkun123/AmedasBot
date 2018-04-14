import json
import os

class Pyon:
    def __init__(self,_filePath):
        self.filePath = _filePath
        print(self.filePath)

    def write(self,_data):
        if _data:
            _stringData = json.dumps(_data)
            open(self.filePath,'w').write(_stringData)
        else:
            return 0
    def read(self):
        if os.path.exists(self.filePath):
            _f = open(self.filePath,'r')
            _resultData = json.load(_f)
            return _resultData
        else:
            return 0
