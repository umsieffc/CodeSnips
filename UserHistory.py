
class UserHistory:
    """Class UserHistory
    """
    # Attributes:
    __UserID = None  # (int) 
    __Posts = None  # ([]) 
    __Comments = None  # ([]) 
    __RecentlyViewed = None  # ([]) 
    __TimeFrame = None  # (int) 
    __TimeFromNow = None  # (String) 
    
    # Operations
    def UserHistory(self, UserID):
        """function UserHistory
        
        UserID: int
        
        returns 
        """
        return None # should raise NotImplementedError()
    
    def GetPosts(self, UserID, TimeFromNow):
        """function GetPosts
        
        UserID: int
        TimeFromNow: String
        
        returns []
        """
        return None # should raise NotImplementedError()
    
    def GetPosts(self, UserID):
        """function GetPosts
        
        UserID: int
        
        returns []
        """
        return None # should raise NotImplementedError()
    
    def GetComments(self, UserID, TimeFromNow):
        """function GetComments
        
        UserID: int
        TimeFromNow: String
        
        returns []
        """
        return None # should raise NotImplementedError()
    
    def GetComments(self, UserID):
        """function GetComments
        
        UserID: int
        
        returns []
        """
        return None # should raise NotImplementedError()
    
    def GetRecentlyViewed(self, UserID, TimeFromNow):
        """function GetRecentlyViewed
        
        UserID: int
        TimeFromNow: String
        
        returns []
        """
        return None # should raise NotImplementedError()
    
    def __CalculateTimeFromNow(self, TimeFrame):
        """function CalculateTimeFromNow
        
        TimeFrame: int
        
        returns String
        """
        return None # should raise NotImplementedError()
    

