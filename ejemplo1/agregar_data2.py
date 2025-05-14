import pandas as pd

from sqlalchemy.orm import sessionmaker
from crear_base import Saludo2
from configuracion import engine

# Crear sesión
Session = sessionmaker(bind=engine)
session = Session()

# Leer el CSV con separador '|'
df = pd.read_csv('/home/edisson/Documentos/web/sem06/clase06-1bim-edisson2407/ejemplo1/data/saludos_mundo.csv', sep='|')

# Insertar los datos en la base
for _, fila in df.iterrows():
    saludo = Saludo2()
    saludo.mensaje = fila['saludo']
    saludo.tipo = fila['tipo']
    saludo.origen = fila['origen']
    session.add(saludo)

# Confirmar
session.commit()

