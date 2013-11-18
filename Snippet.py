from RevisionRequest import RevisionRequest
from Post import Post

class Snippet(Post):
    """Class Snippet
    """
    # Attributes:
    RevisionRequests = None  # ([]) 
    __Title = None  # (String) 
    __Description = None  # (String) 
    __Code = None  # (String) 
    __Language = None  # (String) 
    
    # Operations
    def GetTitle(self):
        """function GetTitle
        
        returns String
        """
        return None # should raise NotImplementedError()
    
    def GetDescription(self):
        """function GetDescription
        
        returns String
        """
        return None # should raise NotImplementedError()
    
    def GetCode(self):
        """function GetCode
        
        returns String
        """
        return None # should raise NotImplementedError()
    
    def GetLanguage(self):
        """function GetLanguage
        
        returns String
        """
        return None # should raise NotImplementedError()
    
    def GetRevisionRequests(self):
        """function GetRevisionRequests
        
        returns []
        """
        return None # should raise NotImplementedError()
    
    def SetTitle(self, Title):
        """function SetTitle
        
        Title: String
        
        returns Boolean
        """
        return None # should raise NotImplementedError()
    
    def SetDescription(self, Description):
        """function SetDescription
        
        Description: String
        
        returns Boolean
        """
        return None # should raise NotImplementedError()
    
    def SetCode(self, Code):
        """function SetCode
        
        Code: String
        
        returns Boolean
        """
        return None # should raise NotImplementedError()
    
    def SetLanguage(self, Language):
        """function SetLanguage
        
        Language: String
        
        returns Boolean
        """
        return None # should raise NotImplementedError()
    
    def RequestRevision(self, Revision):
        """function RequestRevision
        
        Revision: String
        
        returns void
        """
        return None # should raise NotImplementedError()
    

