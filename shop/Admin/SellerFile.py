import re
import sys

sys.path.append("UtilsAndConst")
from UtilsAndConst import ConstFile

class Seller():
    def __init__(self, userName, passWord):
        self.userName = userName
        self.password = passWord

    def emailCheck(self):
        pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if re.match(pattern, self.userName) == None:
            return False
        else:
            return True

    def passwordCheck(self):
        if self.password == ConstFile.Const.AdminPassword:
            return True
        else:
            return False

