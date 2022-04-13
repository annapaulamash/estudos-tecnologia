#Mostrar a data e hora atual, no formato dd/mm/aaaa hh:MM:ss.

from datetime import datetime
jls_extract_var = '%d-%m-%Y-%H:%M:%S'
print(datetime.today().strftime(jls_extract_var))