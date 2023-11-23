import sys
sys.path.append("../TimeFolder")
from TimeFolder import Timelib

class Song:
    def __init__(self ,artistName ,songName , time):
        self.songName = songName
        self.artistName = artistName
        tempList = self.detectTime(time)
        self.time = Timelib.Time(0,tempList[0],tempList[1])    

    def detectTime(self,time):
        timeList = []
        timeList = time.split(':')
        return timeList