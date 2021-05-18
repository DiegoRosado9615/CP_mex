from flask import Flask,jsonify,request,render_template
from flask_restful import Resource, Api
from datos import datos,est_json,mun_json,col_json
import json
import form
import sqlite3
app=Flask(__name__)

@app.route("/")
def busqueda():
    language = request.args.get('language')
    return render_template("home.html")

"""
Funcion que nos permite solicitar el codigo postal de los municipios
devuelve una coincidecia de d_cp que hayan pasado
en caso de no encontrarla devuelve un mensaje de "Dato no encontrado" 
"""
@app.route("/cp_municipio/<string:solicitud>",methods=["get"])
def cp_municipio(solicitud):
    conversion=json.loads(col_json)
    for estado in conversion:
      if (str (conversion[estado]["d_CP"]) ==solicitud):
          return jsonify(conversion[estado])
    return jsonify("Dato no encontrado")


"""
Funcion que nos permite buscar el nombre de un estado, nos devuelve un dato JSON
en caso de no encontrarlo devuelve un mensaje de "Dato no encontrado" 
"""

@app.route("/busca_nombre_estado/<string:solicitud>",methods=["get"])
def busca_nombre_estado(solicitud):
    lista_estado=json.loads(datos)
    n_estado=""
    for estado in lista_estado :
        n_estado=lista_estado[estado]["d_estado"]     
        if((solicitud==n_estado)):
            return jsonify(lista_estado[estado])
    return jsonify("Dato no encontrado")

"""
Funcion que nos permite buscar el nombre de un municipio, nos devuelve una lista de Json
en caso de no encontrarlo devuelve un mensaje de "Dato no encontrado" 
"""            
@app.route("/busca_nombre_municipio/<string:solicitud>",methods=["get"])
def busca_nombre_municipio(solicitud):
    lista_estado=json.loads(datos)
    municipio=""
    listas_municipio=[]
    for estado in lista_estado :    
        municipio=lista_estado[estado]["D_mnpio"]
        if((solicitud== municipio)):
            listas_municipio.append(lista_estado[estado])
    if(len(listas_municipio)!=0):
        return jsonify(listas_municipio) 
    return jsonify("Dato no encontrado")

"""
Funcion que nos permite buscar el nombre de una colonia, nos devuelve una lista de Json
en caso de no encontrarlo devuelve un mensaje de "Dato no encontrado" 
"""            
@app.route("/busca_nombre_colonia/<string:solicitud>",methods=["get"])
def busca_nombre_colonia(solicitud):
    lista_estado=json.loads(datos)
    colonia=""
    listas_colonias=[]
    for estado in lista_estado :    
        municipio=lista_estado[estado]["d_asenta"]
        if((solicitud== municipio)):
            listas_colonias.append(lista_estado[estado])
    if(len(listas_colonias)!=0):
        return jsonify(listas_colonias) 
    return jsonify("Dato no encontrado")

"""
Funcion que nos permite actualizar los datos que se guardaron en base de datos creado 
con sqlite3
"""
@app.route("/actualizar",methods=["get","post"])
def actualizar():
    conexion=sqlite3.connect("datos/BD_codigo_postal.sqlite")

    nuevo_dato=form.Nuevo_CP()
    title= "actualizacion"
    if (request.method=="POST"):
        d_codigo=request.form[d_codigo]
        d_asenta=request.form[d_asenta]
        d_tipo_asenta=request.form[d_tipo_asenta]
        d_municipio=request.form[d_municipio]
        d_estado=request.form[d_estado]
        d_CP=request.form[d_CP]
        c_estado=request.form[c_estado]
        d_asenta=request.form[d_asenta]
        c_oficina=request.form[c_oficina]
        c_CP=request.form[c_CP]
        c_tipo_asenta=request.form[c_tipo_asenta]
        c_mnpio=request.form[c_mnpio]
        id_asenta_cpcons=request.form[id_asenta_cpcons]
        d_zona=request.form[d_zona]
        c_cve_ciudad=request.form[c_cve_ciudad]
        query="insert into datos ()"
    return render_template("actualizar.html",title=title,form=nuevo_dato)
    


"""
Funciones donde podemos ver todos los estados, municipios y colonias que hay :V
"""

@app.route("/estados",methods=["get"])
def estados():
    return jsonify(est_json)

@app.route("/municipio",methods=["get"])
def municipios():
    return jsonify(mun_json)

@app.route("/colonia",methods=["get"])
def colonia():
    return jsonify(col_json)

#Main
if __name__ == "__main__":
    app.run(debug=True,port=8000) 
    