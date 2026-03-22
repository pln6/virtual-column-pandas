from config.exceptions import NewColumnLabelError, OperationError, ColumnsLabelError, ColumnNotFoundError, RoleStringError
import pandas as pd

"""
Validation functions for the virtual column processing module.

Each function raises a specific custom exception if the validation fails:
- NewColumnLabelError for invalid new column names
- OperationError for unsupported operations
- ColumnsLabelError for invalid existing column names
- ColumnNotFoundError for columns missing in the DataFrame
"""

def validate_new_column_label(new_column_label : str) -> None:
    """Validate the new column label.

    Args:
        new_column_label: The name of the new column to be added.

    Raises:
        NewColumnLabelError: If the label contains invalid characters.
    """
    if not new_column_label.replace("_", "").isalpha():
        raise NewColumnLabelError(f"Invalid new column label: '{new_column_label}'.")

def validate_operation(operations : list) -> None:
    """Validate the list of operations.

    Args:
        operations: A list of operations as strings.

    Raises:
        OperationError: If any operation is not in ['+', '-', '*'].
    """
    for operation in operations:
        if not operation in ['+', '-', '*']:
            raise OperationError(f"Unsupported operation: '{operation}'.")
        
def validate_column_labels(column_labels : list) -> None:
    """Validate existing column labels.

    Args:
        column_labels: A list of existing DataFrame column labels.

    Raises:
        ColumnsLabelError: If any label contains invalid characters.
    """
    for  label in column_labels:
        if not label.replace("_", "").isalpha():
            raise ColumnsLabelError(f"Invalid input column label: '{label}'.")
        
def validate_columns_exist(df : pd.DataFrame, column_labels : list) -> None:
    """Check that all specified columns exist in the DataFrame.

    Args:
        df: The pandas DataFrame.
        column_labels: A list of column names to check.

    Raises:
        ColumnNotFoundError: If any column is missing in the DataFrame.
    """
    df_names = df.columns.values.tolist()
    for label in column_labels:
        if not label in df_names:
            raise ColumnNotFoundError(f"Column not found: '{label}'.")

def validate_role_is_not_empty(columns: list) -> None:
    """Check if the role string actually contains column names.

    Args:
        columns: List of columns extracted from the role.

    Raises:
        VirtualColumnError: If no columns were found.
    """
    if not columns or (len(columns) == 1 and not columns[0]):
        raise RoleStringError("The role expression is empty or invalid.")