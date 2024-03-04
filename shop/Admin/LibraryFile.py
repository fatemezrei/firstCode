import sys

sys.path.append("Admin")
from Admin import BookFile, LibraryFile, MagazineFile, VideoFile

sys.path.append("Manager")
from Manager import FileManagerFile

sys.path.append("UtilsAndConst")
from UtilsAndConst import UtilsFile

class Library():

    BookList = []
    VideoList = []
    MagazineList = []

    def AddMedia():

        print("please select one of these : ")
        print("1- Book 2- Magazine 3- Video")

        ord = input()

        if ord == '1':
            print("enter these one line by one line:")

            name = input("name: ")
            realPrice = input("realPrice: ")
            id = input("id: ")
            authorName = input("authorName: ")
            publisherName = input("publisherName: ")

            book = BookFile.Book(name, realPrice, id, authorName, publisherName)
            Library.BookList.append(book)

            tempList1 = [name, realPrice, id, authorName, publisherName, book.taxPrice]

            FileManagerFile.FileManager.addMediaToFile(UtilsFile.MediaType.EBook, tempList1)

        if ord == "2":
            print("enter these one line by one line:")

            name = input("name: ")
            realPrice = input("realPrice: ")
            id = input("id: ")
            publisherName = input("publisherName: ")
            pageNum = input("pageNum: ")
            magazine = MagazineFile.Magazine(name, realPrice, id, publisherName, pageNum)
            Library.MagazineList.append(magazine)

            tempList2 = [name, realPrice, id, publisherName, pageNum]
            FileManagerFile.FileManager.addMediaToFile(UtilsFile.MediaType.EMagazine, tempList2)
        
        if ord == "3":
            print("enter these one line by one line:")

            name = input("name: ")
            realPrice = input("realPrice: ")
            id = input("id: ")
            time = input("time: ")
            CDNum = input("CDNum: ")
            video = VideoFile.Video(name, realPrice, id, time, CDNum)
            Library.VideoList.append(video)

            tempList3 = [name, realPrice, id, time, CDNum]
            FileManagerFile.FileManager.addMediaToFile(UtilsFile.MediaType.EVideo, tempList3)

        def DelMedia():
            print("please select one of these : ")
            print("1- Book 2- Magazine 3- Video")

            ord = input()

            if ord == '1':
                id = input("id: ")

                for book in Library.BookList:
                    if book.id == id:
                        Library.BookList.remove(book)

                FileManagerFile.FileManager.DeleteMedia(UtilsFile.MediaType.EBook, id)