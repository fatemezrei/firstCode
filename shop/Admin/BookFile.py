import sys

sys.path.append("Admin")
from Admin import MediaFile

class Book(MediaFile.Media):
    def __init__(self, name, realPrice, id, authorName, publisherName):
        super().__init__(name, realPrice, id)
        self.authorName = authorName
        self.publisherName = publisherName
        self.taxPrice = self.calculateTax(realPrice)

    def calculateTax(realPrice):
        return realPrice*1.1