

from datetime import datetime

#pip install pytz

import pytz

data = datetime.now(pytz.timezone("Europe/Oslo"))
data2 = datetime.now(pytz.timezone("America/Sao_Paulo"))

print(data)
print(data2)

#se error:
    #executar os comandos
        #python -m venv .env
        #source .env/bin/activate
        #pip install pytz
        #CRTL + Shift + P, buscar pelo interpretador e setar o da pasta .env