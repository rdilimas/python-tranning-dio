from datetime import datetime

data_hora_atual = datetime.now()
data_hora_str = "2023-10-20 10:20"
mascara_ptbr = "%d/%m/%Y %a"
mascara_en = "%Y-%m-%d %H:%M"

#imprimindo um datetime
print(data_hora_atual)
#aplicando uma máscara a u  datetime
print(data_hora_atual.strftime(mascara_ptbr))

#Convertendo uma string para um datetime
data_convertida = datetime.strptime(data_hora_str, mascara_en)
print(data_convertida)
print(type(data_convertida))