from datetime import date, datetime, time

data = date(2023, 7, 10)
print(data)
print(date.today())


data_hora = datetime(2023, 7, 10, 10, 30, 55)
print(data_hora)
print(datetime.today())


data_hora = datetime(2023, 7, 10)
print(data_hora)

hora = time(10, 20, 0)
print(hora)


hoje = (datetime.today())
print(hoje.time())
