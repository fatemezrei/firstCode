import sys

sys.path.append("Admin")
from Admin import BookFile, LibraryFile

class adminPelan():

    def showMenu():

        while True:
            print("you can choose one of this items: ")
            print("1- ADD")
            print("2- DELETE")
            print("3- SEARCH")
            print("4- SHOWCUSTOMERS")
            print("5- CHANGEPASS")
            print("6- EXIT")

            order = input()

            if order == "1":
                LibraryFile.Library.AddMedia()
            if order == "2":
                LibraryFile.library
                




