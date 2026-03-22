from config import NewColumnLabelError, OperationError, ColumnsLabelError, ColumnNotFoundError
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
        raise NewColumnLabelError(new_column_label)

def validate_operation(operations : list) -> None:
    """Validate the list of operations.

    Args:
        operations: A list of operations as strings.

    Raises:
        OperationError: If any operation is not in ['+', '-', '*'].
    """
    for operation in operations:
        if not operation in ['+', '-', '*']:
            raise OperationError(operation)
        
def validate_column_labels(column_labels : list) -> None:
    """Validate existing column labels.

    Args:
        column_labels: A list of existing DataFrame column labels.

    Raises:
        ColumnsLabelError: If any label contains invalid characters.
    """
    for  label in column_labels:
        if not label.replace("_", "").isalpha():
            raise ColumnsLabelError(label)
        
def validate_column_existence(df : pd.DataFrame, column_labels : list) -> None:
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
            raise ColumnNotFoundError(label)
    