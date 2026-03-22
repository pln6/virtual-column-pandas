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
    
class NewColumnLabelError(VirtualColumnError):
    """Raised when the new column label is invalid 
    (must contain only letters and underscores)."""

    def __init__(self, label: str):
        message = f"Invalid new column label: '{label}'."
        super().__init__(message)

class OperationError(VirtualColumnError):
    """Raised when an unsupported operation is used 
    in the virtual column expression."""

    def __init__(self, operation : str):
        message = f"Unsupported operation: '{operation}'."
        super().__init__(message)

class ColumnsLabelError(VirtualColumnError):
    """Raised when an input column label is invalid 
    (must contain only letters and underscores)."""
    
    def __init__(self, label : str):
        message = f"Invalid input column label: '{label}'."
        super().__init__(message)

class ColumnNotFoundError(VirtualColumnError):
    """Raised when a specified column does not exist in the DataFrame."""
    
    def __init__(self, label : str):
        message = f"Column not found: '{label}'."
        super().__init__(message)