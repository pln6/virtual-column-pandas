import pandas as pd
import re
from config.exceptions import VirtualColumnError
from config import validators as val

def add_virtual_column(df: pd.DataFrame, role: str, new_column: str) -> pd.DataFrame:
    """
    Adds a new calculated column to a DataFrame based on a string expression.

    Args:
        df: The source pandas DataFrame.
        role: A string expression (e.g., "col_a + col_b * col_c").
        new_column: The name for the newly created column.

    Returns:
        pd.DataFrame: A copy of the DataFrame with the new column added, 
                      or an empty DataFrame if any validation or calculation fails.
    """
    # 1. Parsing the expression using regex to extract column names and operators
    role_clean = role.replace(" ", "")
    role_list = re.split(r'([+\-*])', role_clean)    
    columns = [r for r in role_list[0::2] if r]
    operations = role_list[1::2]

    try:
        # 2. Validation layer
        val.validate_role_is_not_empty(columns)
        val.validate_columns_exist(df, columns)
        val.validate_column_labels(columns)
        val.validate_new_column_label(new_column)
        val.validate_operation(operations)

        df_result = df.copy()

        # 3. Vectorized calculation using pandas eval
        df_result[new_column] = df_result.eval(role)

        return df_result
    
    except VirtualColumnError:
        # Expected business logic errors (handled by validators)
        return pd.DataFrame()
    
    except Exception:
        # Unexpected errors during eval (e.g., incompatible data types)
        return pd.DataFrame()

