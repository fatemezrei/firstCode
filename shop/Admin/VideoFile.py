import sys

sys.path.append("Admin")
from Admin import MediaFile

class Video(MediaFile.Media):
    def __init__(self, name, realPrice, id, time, CDNum):
        super().__init__(name, realPrice, id)
        self.time = time
        self.CDNum = CDNum
        self.taxPrice = self.calculateTax(realPrice)

    def calculateTax(realPrice, CDNum, time):
        return realPrice * ((CDNum * 1.03) + ((time // 60) * 1.05))
