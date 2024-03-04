import sys

sys.path.append("Admin")
from Admin import MediaFile

class Magazine(MediaFile.Media):
    def __init__(self, name, realPrice, id, publisherName, pageNum):
        super().__init__(name, realPrice, id)
        self.publisherName = publisherName
        self.pageNum = pageNum
        self.taxPrice = self.calculateTax(realPrice, pageNum)

    def calculateTax(realPrice, pageNum):
        if 1 <= pageNum <= 20:
            return realPrice * 1.02
        elif 21 <= pageNum <= 50:
            return realPrice * 1.03
        else:
            return realPrice * 1.05
        