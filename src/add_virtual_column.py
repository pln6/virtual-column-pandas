import pandas as pd
from operators import operations as op

def add_virtual_column(df: pd.DataFrame, role: str, new_column: str) -> pd.DataFrame:
    role_list = role.split()
    columns = [role_list[i] for i in range(0, len(role_list), 2)]
    operations = [role_list[i] for i in range(1, len(role_list), 2)]
    df_result = df.copy()

    columns_final = columns.copy()
    operations_final = []

    for i in range(len(operations)):
        if operations[i] == "*" :
            df_result[f'tmp{i}'] = op[operations[i]](df_result[columns[i]], df_result[columns[i+1]])
            idx = columns_final.index(columns[i])
            cols_to_remove = [columns[i], columns[i+1]]     
            for col in cols_to_remove:
                if col in columns_final:
                    columns_final.remove(col) 
            columns_final.insert(idx, f'tmp{i}')
        else :
            operations_final.append(operations[i])

    result = df_result[columns_final[0]]

    for i, operation in enumerate(operations_final):
        result = op[operation](result, df_result[columns_final[i+1]])
    
    df_result[new_column] = result
    
    return df_result.loc[:, df.columns.values.tolist() + [new_column]]



