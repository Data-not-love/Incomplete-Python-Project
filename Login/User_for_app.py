class User:
    def __init__(self,Id,UserName,PassWord,Email,DOB,Address):
        self.__UserID = Id
        self.__UserName = UserName
        self.__PassWord = PassWord
        self.__Email = Email
        self.__BirthDay = DOB
        self.__Address = Address
    @property
    def BirthDay(self):
        return self.__BirthDay
    @BirthDay.setter
    def sBirthDay(self,value):
        self.__BirthDay = value
    @property
    def UserID(self):
        return self.__UserID

    @UserID.setter
    def sUserId(self,value):
        self.__UserID = value
    @property
    def UserName(self):
        return self.__UserName
    @UserName.setter
    def sUserName(self,value):
        self.__UserName = value

    @property
    def PassWord(self):
        return self.__PassWord
    @PassWord.setter
    def sPassWord(self,value):
        self.__PassWord = value

    @property
    def Email(self):
        return self.__Email
    @Email.setter
    def sEmail(self, value):
        self.__Email = value

    @property
    def Address(self):
        return self.__Address
    @Address.setter
    def sAddress(self, value):
        self.__Address = value
    def LayInfo (self):
        return self.UserID + self.UserName + self.PassWord + self.Email + self.Address