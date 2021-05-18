from wtforms import Form,StringField,IntegerField

class Nuevo_CP(Form):
    d_codigo=StringField("d_codigo")
    d_asenta=StringField("d_asenta")
    d_tipo_asenta=StringField("d_tipo_asenta")
    d_municipio=StringField("d_municipio")
    d_estado=StringField("d_estado")
    d_ciudad=StringField("d_ciudad")
    d_CP=IntegerField("d_cp")
    c_estado=StringField("d_estado")
    c_oficina=StringField("c_oficina")
    c_CP=IntegerField("c_Cp")
    c_tipo_asenta=IntegerField("d_cp")
    c_mnpio=IntegerField("c_mnpio")
    id_asenta_cpcons=StringField("id_asenta_cpcons")
    d_zona=StringField("d_zona")
    c_cve_ciudad=IntegerField("c_cve_ciudad")
    