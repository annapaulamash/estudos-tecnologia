#Calcular o número de dias entre duas datas.
from datetime import date
data_um = date(2020, 11, 16)
data_dois = date(2021, 11, 16)
dias = data_dois - data_um
print(dias.days)