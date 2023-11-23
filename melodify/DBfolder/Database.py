class DB:
    def __init__(self):
        self.__songList = []

    def getSongList(self):
        return self.__songList

    def addSong(self, song):
        self.__songList.append(song)


    def sraech(self ,name):
        exist = False
        for song in self.__songList:
            if name == song.artistName:
                exist = True
                break
        if exist == True:
            return True
        else:
            return False
        
    def addToFile(self, result):
        f = open("melodify.txt", 'a')
        f.writelines(result+"\n")
        f.close()  