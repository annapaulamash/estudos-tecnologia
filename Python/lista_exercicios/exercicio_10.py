#Mostrar o calendário de um dado mês e ano.
import calendar

ano = int(input("Informe o ano: "))
mes = int(input("Informe o mês: "))

print(calendar.month(ano, mes))