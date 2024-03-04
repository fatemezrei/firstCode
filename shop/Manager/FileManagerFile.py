import pandas as pd
import sys

sys.path.append("UtilsAndConst")
from UtilsAndConst import ConstFile, UtilsFile

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


    def addMediaToFile(mediaType, mediaInfo):
        if (mediaType == UtilsFile.MediaType.EBook):
            df = pd.read_excel(ConstFile.Const.BookFilePath)
            new_data = {ConstFile.Const.nameColumn: [mediaInfo[0]], ConstFile.Const.idColumn: [mediaInfo[1]], ConstFile.Const.realPriceColumn: [mediaInfo[2]], ConstFile.Const.authorNameColumn : [mediaInfo[3]], ConstFile.Const.publisherNameColumn: [mediaInfo[4]], ConstFile.Const.taxPriceColumn: [mediaInfo[5]]}
            new_df = pd.DataFrame(new_data)
            df = df.append(new_df, ignore_index=True)
            df.to_excel(ConstFile.Const.BookFilePath, index=False)

        elif (mediaType == UtilsFile.MediaType.EMagazine):
            df = pd.read_excel(ConstFile.Const.MagazineFilePath)
            new_data = {ConstFile.Const.nameColumn: [mediaInfo[0]], ConstFile.Const.idColumn: [mediaInfo[1]], ConstFile.Const.realPriceColumn: [mediaInfo[2]], ConstFile.Const.publisherNameColumn : [mediaInfo[3]], ConstFile.Const.pageNumColumn: [mediaInfo[4]], ConstFile.Const.taxPriceColumn: [mediaInfo[5]]}
            new_df = pd.DataFrame(new_data)
            df = df.append(new_df, ignore_index=True)
            df.to_excel(ConstFile.Const.MagazineFilePath, index=False)

        elif (mediaType == UtilsFile.MediaType.EVideo):
            df = pd.read_excel(ConstFile.Const.VideoFilePath)
            new_data = {ConstFile.Const.nameColumn: [mediaInfo[0]], ConstFile.Const.idColumn: [mediaInfo[1]], ConstFile.Const.realPriceColumn: [mediaInfo[2]], ConstFile.Const.timeColumn : [mediaInfo[3]], ConstFile.Const.CDNumColumn: [mediaInfo[4]], ConstFile.Const.taxPriceColumn: [mediaInfo[5]]}
            new_df = pd.DataFrame(new_data)
            df = df.append(new_df, ignore_index=True)
            df.to_excel(ConstFile.Const.VideoFilePath, index=False)

    def DeleteMedia(mediaType, id):
        if (mediaType == UtilsFile.MediaType.EBook):
            df = pd.read_excel(ConstFile.Const.BookFilePath)
            df = df[df['ID'] != id]
            df.to_excel(ConstFile.Const.BookFilePath, index=False)

        elif (mediaType == UtilsFile.MediaType.EMagazine):
            df = pd.read_excel(ConstFile.Const.MagazineFilePath)
            df = df[df['ID'] != id]
            df.to_excel(ConstFile.Const.MagazineFilePath, index=False)

        elif (mediaType == UtilsFile.MediaType.EVideo):
            df = pd.read_excel(ConstFile.Const.VideoFilePath)
            df = df[df['ID'] != id]
            df.to_excel(ConstFile.Const.VideoFilePath, index=False)





    



   

