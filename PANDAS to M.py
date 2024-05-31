import pandas as pd

# Cargar el archivo Excel en un DataFrame
df = pd.read_excel(r"C:\Users\srodriguez\Downloads\Proyecto\Countries.xlsx")

def dicts_to_m_language(dicts):
    rows = []
    for record in dicts:
        row = "[" + ", ".join([f'{key} = "{value}"' if isinstance(value, str) else f'{key} = {value}' for key, value in record.items()]) + "]"
        rows.append(row)
    m_language_list = "{" + ", ".join(rows) + "}"
    return f"let\n    Source = {m_language_list},\n    Tabla = Table.FromRecords(Source)\nin\n    Tabla"

list_of_dicts = df.to_dict(orient='records')
m_language_code = dicts_to_m_language(list_of_dicts)
print(m_language_code)