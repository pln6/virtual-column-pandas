"""
Custom exceptions for the virtual column processing module.

Contains a hierarchy of exceptions to handle various validation
and operational errors when adding virtual columns to a pandas DataFrame.
"""

class VirtualColumnError(Exception):
    """Base class for all virtual column errors.

    Attributes:
        message -- explanation of the error
    """
    def __init__(self, message = "An error occurred in virtual column processing. Returning an empty DataFrame"):
        super().__init__(message)
    
class NewColumnLabelError(VirtualColumnError): pass
class OperationError(VirtualColumnError): pass
class ColumnsLabelError(VirtualColumnError): pass
class ColumnNotFoundError(VirtualColumnError): pass
class RoleStringError(VirtualColumnError): pass