from config import NewColumnLabelError, OperationError, ColumnsLabelError, ColumnNotFoundError
import pandas as pd

def validate_new_column_label(new_column_label : str) -> None:
    if not new_column_label.replace("_", "").isalpha():
        raise NewColumnLabelError(new_column_label)

def validate_operation(operations : list) -> None:
    for operation in operations:
        if not operation in ['+', '-', '*']:
            raise OperationError(operation)
        
def validate_column_labels(column_labels : list) -> None:
    for  label in column_labels:
        if not label.replace("_", "").isalpha():
            raise ColumnsLabelError(label)
        
def validate_column_existence(df : pd.DataFrame, column_labels : list) -> None:
    df_names = df.columns.values.tolist()
    for label in column_labels:
        if not label in df_names:
            raise ColumnNotFoundError(label)
    