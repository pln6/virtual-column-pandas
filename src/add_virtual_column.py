import pandas as pd
from operators import operations as op

def add_virtual_column(df: pd.DataFrame, role: str, new_column: str) -> pd.DataFrame:
    role_list = role.split()
    columns = [role_list[i] for i in range(0, len(role_list), 2)]
    operations = [role_list[i] for i in range(1, len(role_list), 2)]
    df_result = df.copy()
    for i in range(len(columns)-1):
        for operation in operations:
            df_result[new_column] = op[operation](df[columns[i]], df[columns[i+1]])
    return df_result