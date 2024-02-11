from enum import Enum
import random

class sex(Enum):
    male = 1
    female = 2

class Person:
    def __init__(self, Name, SSN, Field, Sex):
        self.Name = Name
        self.SSN = SSN
        self.Field = Field
        self.Sex = Sex

class Professor(Person):

    MinTRA = 0

    def __init__(self, Name, SSN, Field, Sex ,RoomNo):
        super().__init__(Name, SSN, Field, Sex)
        self.RoomNo = RoomNo
        self.ResearchAssistants = []

    def detectRoomNo(professorList, roomNo):
        for professor in professorList:
            if roomNo == professor.RoomNo:
                return False
            
        return True


class Student(Person):
    def __init__(self, Name, SSN, Field, Sex ,EnteringYear):
        super().__init__(Name, SSN, Field, Sex) 
        self.EnteringYear = EnteringYear

class TeacherAssistant(Student):
    def __init__(self, Name, SSN, Field, Sex, EnteringYear, UnitId):
        super().__init__(Name, SSN, Field, Sex, EnteringYear)
        self.UnitId = UnitId

class ResearchAssistant(Student):
    def __init__(self, Name, SSN, Field, Sex, EnteringYear, ProjectName,FreeTime ,ProfessorSSN):
        super().__init__(Name, SSN, Field, Sex, EnteringYear) 
        self.ProjectName = ProjectName
        self.FreeTime = FreeTime     
        self.ProfessorSSN = ProfessorSSN         

class Unit:

    Students = []
    ProfessorSSN = ""
    TeachingAssistants = ""
    def __init__(self ,UnitId ,Name ,Field ,MaxSize):        
        self.UnitId = UnitId
        self.Name = Name
        self.Field =Field
        self.MaxSize =MaxSize

if __name__ == "__main__":

    studentList = []
    professorList = []
    unitList = []

    while True:

        print("you can choose one of this items: ")
        print("1- register student")
        print("2- register professor")
        print("3- make unit")

        order = input() 

        if order == "1":
            print("please enter your name, ssn, enteringYear, field, sex")
            studentInfo = input()
            studentInfoList = studentInfo.split(",")

            isExist = False

            for student in studentInfoList:
                if studentInfoList[1] == student.SSN:
                    print("this student is already exist")
                    isExist = True
                    break

            if (isExist == True):
                continue

            student = Student(studentInfoList[0], studentInfoList[1], studentInfoList[4], studentInfoList[2], studentInfoList[3])

            studentList.append(student)
            
        if order == "2":
            print("please enter your name, ssn, field, sex")
            professorInfo = input()
            professorInfoList = professorInfo.split(",")

            isExist = False

            for professor in professorList:
                if professorInfoList[1] == professor.SSN:
                    print("this professor is already exist")
                    isExist = True
                    break

            if (isExist == True):
                continue

            roomNo = 0
            while (True):
                roomNo = random.randint(1, 1000)
                temp = Professor.detectRoomNo(professorList, roomNo)

                if (temp == False):
                    continue
                else:
                    break

            professor = Professor(professorInfoList[0], professorInfoList[1], professorInfoList[2], professorInfoList[3], roomNo)

            professorList.append(professor)

        if order == "3":
            print("please enter the unitId, name, field, MaxSize ")
            unitInfo = input()
            unitInfoList = unitInfo.split(",")

            isExist = False

            for unit in unitList:
                if unitInfoList[0] == unit.UnitId:
                    print("this unitId is already exist")
                    isExist = True
                    break

            if (isExist == True):
                continue

            if unitInfoList[3] < 10 or unitInfoList[3] > 180:
                print("the student maximum range is out of range")
                continue

            unit = Unit(unitInfo[0], unitInfo[1], unitInfo[2], unitInfo[3])

            unitList.append(unit)
            