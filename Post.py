from User import User
from SearchSort import SearchSort

class Post:
    """Abstract class Post
    """
    # Attributes:
    __PostID = None  # (int) 
    __UserID = None  # (int) 
    __UpVotes = None  # (int) 
    __DownVotes = None  # (int) 
    __LastChanged = None  # (String) 
    
    # Operations
    def Post(self, ):
        """function Post
        
        : 
        
        returns 
        """
        raise NotImplementedError()
    
    def Post(self, UserID):
        """function Post
        
        UserID: int
        
        returns 
        """
        raise NotImplementedError()
    
    def DeletePost(self, PostID):
        """function DeletePost
        
        PostID: int
        
        returns void
        """
        raise NotImplementedError()
    
    def UpVotePost(self, UserID):
        """function UpVotePost
        
        UserID: int
        
        returns void
        """
        raise NotImplementedError()
    
    def DownVotePost(self, UserID):
        """function DownVotePost
        
        UserID: int
        
        returns void
        """
        raise NotImplementedError()
    
    def GetUpVotes(self):
        """function GetUpVotes
        
        returns int
        """
        raise NotImplementedError()
    
    def GetDownVotes(self):
        """function GetDownVotes
        
        returns int
        """
        raise NotImplementedError()
    
    def GetLastChanged(self):
        """function GetLastChanged
        
        returns String
        """
        raise NotImplementedError()
    

