import pandas as pd
import re
from config.exceptions import VirtualColumnError
from config import validators as val

def add_virtual_column(df: pd.DataFrame, role: str, new_column: str) -> pd.DataFrame:
    role_clean = role.replace(" ", "")
    role_list = re.split(r'([+\-*])', role_clean)    
    columns = [r for r in role_list[0::2] if r]
    operations = role_list[1::2]

    try:
        val.validate_role_is_not_empty(columns)
        val.validate_columns_exist(df, columns)
        val.validate_column_labels(columns)
        val.validate_new_column_label(new_column)
        val.validate_operation(operations)

        df_result = df.copy()

        df_result[new_column] = df_result.eval(role)

        return df_result
    
    except VirtualColumnError:
        return pd.DataFrame()
    
    except Exception:
        return pd.DataFrame()

