import sys 

sys.path.append("DBfolder")
from DBfolder import Database

sys.path.append("SongFolder")
from SongFolder import SongFile

sys.path.append("TimeFolder")
from TimeFolder import Timelib

if __name__ == "__main__":

    db = Database.DB()

    while True:
        print("Do you want to search or add song? ")
        print("1.search 2.add song")
        order = input()

        if order == "1":
            name = input()
            if db.sraech(name) == True:
                print('the artist exist')
            else:
                print('the artist not exist!')

        elif order == "2":
            numberOfSong = int(input("please enter the number of songs: "))
            orderList = []
            for i in range(numberOfSong):
                orderList.append(input())

            numberOfSongAdded = 0 
            for i in range(numberOfSong):
                templist = []
                templist = orderList[i].split(";")
                
                
                if len(templist) < 3:
                    print('invalid song!')
                    continue
                if len(templist[0]) < 3 or len(templist[0]) > 20:
                    print('invalid artist name!')
                    continue
                if len(templist[1]) < 3 or len(templist[1]) > 30 :
                    print('invalid song name')
                    continue
                timeTemp = templist[2].split(':')
                if len(timeTemp) == 3:
                    print('invalid time')
                    continue
                if int(timeTemp[0]) > 14 or int(timeTemp[1]) > 59:
                    print('invalid time')
                    continue
                        
                song = SongFile.Song(templist[0] ,templist[1] ,templist[2])

                db.addSong(song)
                print('song added')
                numberOfSongAdded += 1
                db.addToFile(orderList[i])

            print(f'songs added: {numberOfSongAdded}') 
            Timelib.Time.playlistLength(db.getSongList()) 

        else:
            print('your order is not true')     