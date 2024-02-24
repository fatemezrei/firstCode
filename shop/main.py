import sys

sys.path.append("Admin")
sys.path.append("UtilsAndConst")
sys.path.append("Manager")

from Admin import SellerFile, adminPanelFile
from UtilsAndConst import UtilsFile, ConstFile
from Manager import FileManagerFile, ManagerFile


if __name__ == "__main__":
    
    manager = ManagerFile.Manager()
    fileManager = FileManagerFile.FileManager(ConstFile.Const.FilePath)

    while True:

        print("wellcome to shop")

        print("who are you?")
        print("1-admin 2-user")
        access = int(input())

        if access == UtilsFile.AccessLevel.Admin:
            print("please enter your email address and password")
            emailAddress = input()
            password = input()
            
            admin = SellerFile.Seller(emailAddress, password)

            if (admin.emailCheck() == True and admin.passwordCheck() == True):
                adminPanel = adminPanelFile.adminPelan()
                adminPanel.showMenu()

        if access == UtilsFile.AccessLevel.User:
            print("who are you?")
            print("1.cutomer 2.student 3.teacher")
            userType = int(input())

            if userType == UtilsFile.User.Customer:
                print("please enter your userName and id")
                userName = input("name: ")
                id = input("id: ")
                if UtilsFile.Checkpassword.CheckCustomerId(id) == False:
                    print("id is not valid!")
                    continue
                
                if fileManager.searchUserName(userName) == True:
                    if fileManager.checkPassword(userName, id) == False:
                        print("password is not valid")
                        continue
                    else:
                        pass #ورود کاربر به سامانه
                else:
                    fileManager.addUserToFile(userName, id)  
                    # ورود کاربر به سامانه
            
            if userType == UtilsFile.User.Student:
                print("please enter your userName and password")
                userName = input("name: ")
                studentId = input("studentId(8): ")
                if UtilsFile.Checkpassword.CheckStudentId(studentId) == False:
                    print("id is not valid!")
                    continue

                if fileManager.searchUserName(userName) == True:
                    if fileManager.checkPassword(userName, studentId) == False:
                        print("studentId is not valid")
                        continue
                    else:
                        pass #ورود کاربر به سامانه
                else:
                    fileManager.addUserToFile(userName, studentId)  
                    # ورود کاربر به سامانه
            

            if userType == UtilsFile.User.Teacher:
                print("please enter your userName and place")
                userName = input("name: ")
                place = input("place: ")

                if fileManager.searchUserName(userName) == True:
                    if fileManager.checkPassword(userName, place) == False:
                        print("place is not valid")
                        continue
                    else:
                        pass #ورود کاربر به سامانه
                else:
                    fileManager.addUserToFile(userName, place)  
                    # ورود کاربر به سامانه

                
