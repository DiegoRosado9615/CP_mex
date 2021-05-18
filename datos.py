import pandas as pd
import sqlite3
"""
Leemos los datos que descargamos de la pagina 
https://www.correosdemexico.gob.mx/SSLServicios/ConsultaCP/CodigoPostal_Exportar.aspx
"""
df = pd.read_csv('datos/CPdescarga.csv',sep="|", encoding='utf8')

"""
Separamos a df en 3 sub df diferentes que contendran los codigos de Cp
"""
estados=df[["d_codigo","d_CP","d_estado"]]
municipio=df[["d_codigo","d_CP","D_mnpio"]]
colonia=df[["d_codigo","d_CP","d_asenta"]]
"""
Los escribimos en 3 archicos csv diferentes
"""
estados.to_csv('datos/estados.csv', encoding='utf8')
municipio.to_csv('datos/municipio.csv' , encoding='utf8')
colonia.to_csv('datos/colonia.csv', encoding='utf8')

"""
Creamos los archivos json para la api
"""
datos=df.to_json(orient="index")
est_json=estados.to_json(orient="index")
mun_json=municipio.to_json(orient="index")
col_json=colonia.to_json(orient="index")

"""
Hacemos la BD con sqlite3
"""

conexion=sqlite3.connect("datos/BD_codigo_postal.sqlite")
#df.to_sql("datos",conexion)

x= "select * from datos"
y=pd.read_sql(x,conexion)
