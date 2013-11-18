from User import User
from UserHistory import UserHistory

class User:
    """Class User
    """
    # Attributes:
    __UserID = None  # (int) 
    __Name = None  # (String) 
    __Email = None  # (String) 
    __Password = None  # (String) 
    __DOB = None  # (String) 
    __Bio = None  # (String) 
    __Specialization = None  # (String) 
    __GravatarLink = None  # (String) 
    __UserHistory = None  # (UserHistory) 
    __Permissions = None  # (int) 
    __Favorites = None  # ([]) 
    
    # Operations
    def User(self):
        """function User
        
        returns 
        """
        return None # should raise NotImplementedError()
    
    def User(self, Name, Email, Password, DOB):
        """function User
        
        Name: String
        Email: String
        Password: String
        DOB: String
        
        returns 
        """
        return None # should raise NotImplementedError()
    
    def GetUserID(self, Email):
        """function GetUserID
        
        Email: String
        
        returns int
        """
        return None # should raise NotImplementedError()
    
    def GetName(self, UserID):
        """function GetName
        
        UserID: int
        
        returns String
        """
        return None # should raise NotImplementedError()
    
    def GetEmail(self, UserID):
        """function GetEmail
        
        UserID: int
        
        returns String
        """
        return None # should raise NotImplementedError()
    
    def GetDOB(self, UserID):
        """function GetDOB
        
        UserID: int
        
        returns String
        """
        return None # should raise NotImplementedError()
    
    def GetBio(self, UserID):
        """function GetBio
        
        UserID: int
        
        returns String
        """
        return None # should raise NotImplementedError()
    
    def GetSpecialization(self, UserID):
        """function GetSpecialization
        
        UserID: int
        
        returns String
        """
        return None # should raise NotImplementedError()
    
    def GetGravatar(self, UserID):
        """function GetGravatar
        
        UserID: int
        
        returns String
        """
        return None # should raise NotImplementedError()
    
    def GetPermissions(self, UserID):
        """function GetPermissions
        
        UserID: int
        
        returns int
        """
        return None # should raise NotImplementedError()
    
    def GetUserHistory(self, UserID):
        """function GetUserHistory
        
        UserID: int
        
        returns UserHistory
        """
        return None # should raise NotImplementedError()
    
    def GetFavorites(self, UserID):
        """function GetFavorites
        
        UserID: int
        
        returns []
        """
        return None # should raise NotImplementedError()
    
    def SetName(self, UserID, Name):
        """function SetName
        
        UserID: int
        Name: String
        
        returns void
        """
        return None # should raise NotImplementedError()
    
    def SetEmail(self, UserID, Email):
        """function SetEmail
        
        UserID: int
        Email: String
        
        returns void
        """
        return None # should raise NotImplementedError()
    
    def SetDOB(self, UserID, DOB):
        """function SetDOB
        
        UserID: int
        DOB: String
        
        returns void
        """
        return None # should raise NotImplementedError()
    
    def SetBio(self, UserID, Bio):
        """function SetBio
        
        UserID: int
        Bio: String
        
        returns void
        """
        return None # should raise NotImplementedError()
    
    def SetSpecialization(self, UserID, Specialization):
        """function SetSpecialization
        
        UserID: int
        Specialization: String
        
        returns void
        """
        return None # should raise NotImplementedError()
    
    def SetGravatar(self, UserID, GravatarLink):
        """function SetGravatar
        
        UserID: int
        GravatarLink: String
        
        returns void
        """
        return None # should raise NotImplementedError()
    
    def SetPermissions(self, UserID, Permissions):
        """function SetPermissions
        
        UserID: int
        Permissions: int
        
        returns void
        """
        return None # should raise NotImplementedError()
    
    def SetFavorites(self, UserID, Favorites):
        """function SetFavorites
        
        UserID: int
        Favorites: []
        
        returns void
        """
        return None # should raise NotImplementedError()
    
    def DeleteAcct(self, UserID):
        """function DeleteAcct
        
        UserID: int
        
        returns void
        """
        return None # should raise NotImplementedError()
    
    def __Login(self, Email, Password):
        """function Login
        
        Email: String
        Password: String
        
        returns int
        """
        return None # should raise NotImplementedError()
    
    def __StartSession(self, UserID):
        """function StartSession
        
        UserID: int
        
        returns void
        """
        return None # should raise NotImplementedError()
    
    def __EndSession(self, UserID):
        """function EndSession
        
        UserID: int
        
        returns void
        """
        return None # should raise NotImplementedError()
    
    def __Logout(self, UserID):
        """function Logout
        
        UserID: int
        
        returns void
        """
        return None # should raise NotImplementedError()
    
    def __UpdateAcct(self, UserID, User):
        """function UpdateAcct
        
        UserID: int
        User: User
        
        returns Boolean
        """
        return None # should raise NotImplementedError()
    

