class VirtualColumnError(Exception):
    """Base class for all virtual column errors"""
    def __init__(self, message = "An error occurred in virtual column processing. Returning an empty DataFrame"):
        super().__init__(message)
    
class NewColumnLabelError(VirtualColumnError):
    def __init__(self, label: str):
        message = f"Invalid new column label: '{label}'."
        super().__init__(message)

class OperationError(VirtualColumnError):
    def __init__(self, operation : str):
        message = f"Unsupported operation: '{operation}'."
        super().__init__(message)

class ColumnsLabelError(VirtualColumnError):
    def __init__(self, label : str):
        message = f"Invalid input column label: '{label}'."
        super().__init__(message)

class ColumnNotFoundError(VirtualColumnError):
    def __init__(self, label : str):
        message = f"Column not found: '{label}'."
        super().__init__(message)