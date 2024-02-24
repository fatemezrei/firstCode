import pandas as pd
import sys

sys.path.append("UtilsAndConst")
from UtilsAndConst import ConstFile

class FileManager():
    def __init__(self, filePath):
        self.filePath = filePath

    def searchUserName(userName):
        df = pd.read_excel(ConstFile.Const.FilePath)
        if df[ConstFile.Const.userNameColumn].eq(userName) == True:
            return True  
        else:
            return False
            
    def checkPassword(userName, passWord):
        df = pd.read_excel(ConstFile.Const.FilePath)
        index = df[ConstFile.Const.userNameColumn].eq(userName).idxmax() 
        passWordExcel = df.loc[index, ConstFile.Const.passWordColumn]
        if passWordExcel == passWord:
            return True
        else:
            return False
        
    def addUserToFile(userName, passWord):
        df = pd.read_excel(ConstFile.Const.FilePath)
        new_data = {ConstFile.Const.userNameColumn: [userName], ConstFile.Const.passWordColumn: [passWord]}
        new_df = pd.DataFrame(new_data)
        df = df.append(new_df, ignore_index=True)
        df.to_excel(ConstFile.Const.FilePath, index=False)

   

