from enum import Enum
import sys

sys.path.append("UtilsAndConst")
from UtilsAndConst import ConstFile

class AccessLevel(Enum):
    Admin = 1
    User = 2

class User(Enum):
    Customer = 1
    Student = 2
    Teacher = 3

class MediaType():
    EBook = 1
    EMagazine = 2
    EVideo = 3

class Checkpassword():
    
    def CheckCustomerId(id):
        if len(id) != ConstFile.Const.CustomerIdLen:
            return False

        for i in range(0,len(id)):
            for j in range(1,len(id)):
                if id[i] != id[j]:
                    return False

        a = int(id[-1])
        b = int(id[0])*10 + int(id[1])*9 + int(id[2])*8 + int(id[3])*7 + int(id[4])*6 + int(id[5])*5 + int(id[6])*4 + int(id[7])*3 + int(id[8])*2 
        c = b%11
        
        if c == 0 and a == c :
            return True
        elif c == 1 and a == 1 :
            return True
        elif c > 1 and a == abs(c-11) :
            return True
        else:
            return False
        
    def CheckStudentId(id):
        if len(id) != ConstFile.Const.StudentIdLen:
            return False
        if id[0] != 9:
            return False
        return True