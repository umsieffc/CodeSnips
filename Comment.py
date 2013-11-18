from Post import Post

class Comment(Post):
    """Class Comment
    """
    # Attributes:
    message = None  # (String) 
    LastChanged = None  # (String) 
    ParentPostID = None  # (int) 
    
    # Operations
    def GetMessage(self, ):
        """function GetMessage
        
        : 
        
        returns String
        """
        return None # should raise NotImplementedError()
    
    def SetMessage(self, Message):
        """function SetMessage
        
        Message: String
        
        returns Boolean
        """
        return None # should raise NotImplementedError()
    
    def SetLastChanged(self, LastChanged):
        """function SetLastChanged
        
        LastChanged: String
        
        returns void
        """
        return None # should raise NotImplementedError()
    
    def GetLastChanged(self):
        """function GetLastChanged
        
        returns String
        """
        return None # should raise NotImplementedError()
    

