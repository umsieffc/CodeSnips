
class RevisionRequest:
    """Class RevisionRequest
    """
    # Attributes:
    RevisionID = None  # (int) 
    PostID = None  # (int) 
    UserID = None  # (int) 
    RevisionDescription = None  # (String) 
    DateSent = None  # (String) 
    CodeRevision = None  # (String) 
    
    # Operations
    def SetRevisionDescription(self, RevisionDescription):
        """function SetRevisionDescription
        
        RevisionDescription: String
        
        returns void
        """
        return None # should raise NotImplementedError()
    
    def GetRevisionDescription(self):
        """function GetRevisionDescription
        
        returns String
        """
        return None # should raise NotImplementedError()
    
    def ApproveRevision(self):
        """function ApproveRevision
        
        returns void
        """
        return None # should raise NotImplementedError()
    
    def RejectRevision(self):
        """function RejectRevision
        
        returns void
        """
        return None # should raise NotImplementedError()
    
    def SetCodeRevision(self, CodeRevision):
        """function SetCodeRevision
        
        CodeRevision: String
        
        returns void
        """
        return None # should raise NotImplementedError()
    
    def GetCodeRevision(self):
        """function GetCodeRevision
        
        returns String
        """
        return None # should raise NotImplementedError()
    

