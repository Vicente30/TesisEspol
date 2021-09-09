import math
import tkinter as tk
from tkinter import ttk
from tkinter.constants import RIGHT
from typing import Text
import functools

# Create a new window
window = tk.Tk()
window.title("Poyecto")
nb = ttk.Notebook(window)
nb.pack(fill="both", expand="yes")

# Crear Pestanas
p1 = tk.Frame(nb)
p2 = tk.Frame(nb)
p3 = tk.Frame(nb)
p4 = tk.Frame(nb)
p5 = tk.Frame(nb)
p6 = tk.Frame(nb)
p7 = tk.Frame(nb)
p8 = tk.Frame(nb)
p9 = tk.Frame(nb)

# Agregar pestanas creadas
nb.add(p1, text="Datos \nGenerales")
nb.add(p2, text="Fondo y \ntecho")
nb.add(p3, text="Diametros y \nespesores")
nb.add(p4, text="Alturas, \nespesores y juntas")
nb.add(p5, text="Volumen \nmuerto")
nb.add(p6, text="Correciones para \nla circunferencia")
nb.add(p7, text="Calculo para\n anillos")
nb.add(p8, text="Calculo de \nvolumenes muertos")
nb.add(p9, text="Altura \nvs. Volumen")


def creacionFrames(nombre, labels, unidades, fr=window):
    frame_general = tk.Frame(master=fr, relief=tk.GROOVE,
                             borderwidth=3, width=200, height=100)
    frame_titulo = tk.Frame(master=frame_general,
                            width=200, height=100, borderwidth=3)
    frame_titulo.pack()
    label = tk.Label(master=frame_titulo, text=nombre)
    label.pack()
    frame_form = tk.Frame(master=frame_general, borderwidth=3)
    frame_form.pack()
    for idx, text in enumerate(labels):
        number2 = tk.StringVar()
        label = tk.Label(master=frame_form, text=text)
        entry = tk.Entry(master=frame_form, textvariable=number2, width=10)
        unity = tk.Label(master=frame_form, text=unidades[idx])
        label.grid(row=idx, column=0, sticky="e")
        entry.grid(row=idx, column=1)
        unity.grid(row=idx, column=2)
    return frame_general


# Informacion general
frm_titulo = tk.Frame(master=p1, borderwidth=3)
frm_titulo.pack()
label = tk.Label(master=frm_titulo, text="Informacion General")
label.pack()

# Creacion de formulario que contenga informacion general
frm_form = tk.Frame(master=p1, relief=tk.GROOVE, borderwidth=3)
frm_form.pack()

# Creando labels y entradas para obtener informacion
lbl_fecha_calibracion = tk.Label(
    master=frm_form, text="Fecha de ultima calibracion:")
ent_fecha_calibracion = tk.Entry(master=frm_form, width=40)
lbl_fecha_calibracion.grid(row=0, column=0, sticky="e")
ent_fecha_calibracion.grid(row=0, column=1)

lbl_propietario = tk.Label(master=frm_form, text="Propietario:")
ent_propietario = tk.Entry(master=frm_form, width=40)
lbl_propietario.grid(row=1, column=0, sticky="e")
ent_propietario.grid(row=1, column=1)

lbl_nombre_campo = tk.Label(master=frm_form, text="Nombre del Campo:")
ent_nombre_campo = tk.Entry(master=frm_form, width=40)
lbl_nombre_campo.grid(row=2, column=0, sticky="e")
ent_nombre_campo.grid(row=2, column=1)

lbl_localizacion = tk.Label(master=frm_form, text="Localizacion:")
ent_localizacion = tk.Entry(master=frm_form, width=40)
lbl_localizacion.grid(row=3, column=0, sticky=tk.E)
ent_localizacion.grid(row=3, column=1)

lbl_material_tanque = tk.Label(master=frm_form, text="Material del Tanque:")
ent_material_tanque = tk.Entry(master=frm_form, width=40)
lbl_material_tanque.grid(row=4, column=0, sticky=tk.E)
ent_material_tanque.grid(row=4, column=1)

lbl_capacidad_nominal = tk.Label(master=frm_form, text="Capacidad Nominal:")
ent_capacidad_nominal = tk.Entry(master=frm_form, width=40)
lbl_capacidad_nominal.grid(row=5, column=0, sticky=tk.E)
ent_capacidad_nominal.grid(row=5, column=1)

lbl_codigo_tanque = tk.Label(master=frm_form, text="Codigo del tanque:")
ent_codigo_tanque = tk.Entry(master=frm_form, width=40)
lbl_codigo_tanque.grid(row=6, column=0, sticky=tk.E)
ent_codigo_tanque.grid(row=6, column=1)

lbl_tipo_del_tanque = tk.Label(master=frm_form, text="Tipo del tanque:")
ent_tipo_del_tanque = tk.Entry(master=frm_form, width=40)
lbl_tipo_del_tanque.grid(row=7, column=0, sticky=tk.E)
ent_tipo_del_tanque.grid(row=7, column=1)

# Creacion de formulario de datos
frm_form_2 = tk.Frame(master=p2, relief=tk.GROOVE,
                      width=200, height=100, borderwidth=3)
frm_form_2.pack(side=tk.LEFT, padx=20, pady=10)
frm_titulo_dato = tk.Frame(master=frm_form_2, borderwidth=3)
frm_titulo_dato.pack()
label = tk.Label(master=frm_titulo_dato, text="Datos")
label.pack()
frm_datos = tk.Frame(master=frm_form_2, width=200, height=100, borderwidth=3)
frm_datos.pack(side=tk.LEFT, padx=20, pady=10)

# Creando labels y entradas para obtener informacion de datos
lbl_diametro_nominal = tk.Label(master=frm_datos, text="Diametro nominal:")
ent_diametro_nominal = tk.Entry(master=frm_datos, width=10)
unit_diametro_nominal = tk.Label(master=frm_datos, text="in")
lbl_diametro_nominal.grid(row=0, column=0, sticky="e")
ent_diametro_nominal.grid(row=0, column=1)
unit_diametro_nominal.grid(row=0, column=2)

lbl_altura_liquido = tk.Label(master=frm_datos, text="*Altura del Liquido:")
ent_altura_liquido = tk.Entry(master=frm_datos, width=10)
unt_altura_liquido = tk.Label(master=frm_datos, text="ft")
lbl_altura_liquido.grid(row=1, column=0, sticky="e")
ent_altura_liquido.grid(row=1, column=1)
unt_altura_liquido.grid(row=1, column=2)

lbl_temp_liquido = tk.Label(master=frm_datos, text="*Temp. del Liquido:")
ent_temp_liquido = tk.Entry(master=frm_datos, width=10)
unt_temp_liquido = tk.Label(master=frm_datos, text="°F")
lbl_temp_liquido.grid(row=2, column=0, sticky="e")
ent_temp_liquido.grid(row=2, column=1)
unt_temp_liquido.grid(row=2, column=2)

lbl_temp_ambiente = tk.Label(master=frm_datos, text="Temp. del Ambiente:")
ent_temp_ambiente = tk.Entry(master=frm_datos, width=10)
unt_temp_ambiente = tk.Label(master=frm_datos, text="°F")
lbl_temp_ambiente.grid(row=3, column=0, sticky=tk.E)
ent_temp_ambiente.grid(row=3, column=1)
unt_temp_ambiente.grid(row=3, column=2)

lbl_grados_api = tk.Label(master=frm_datos, text="Grados API a 60°F:")
ent_grados_api = tk.Entry(master=frm_datos, width=10)
lbl_grados_api.grid(row=4, column=0, sticky=tk.E)
ent_grados_api.grid(row=4, column=1)

lbl_altura_platina = tk.Label(
    master=frm_datos, text="Altura platina de Aforo:")
ent_altura_platina = tk.Entry(master=frm_datos, width=10)
unt_altura_platina = tk.Label(master=frm_datos, text="mm")
lbl_altura_platina.grid(row=5, column=0, sticky=tk.E)
ent_altura_platina.grid(row=5, column=1)
unt_altura_platina.grid(row=5, column=2)

lbl_inclinacion_tanque = tk.Label(master=frm_datos, text="*Inclinación Mayor:")
ent_inclinacion_tanque = tk.Entry(master=frm_datos, width=10)
unt_inclinacion_tanque = tk.Label(master=frm_datos, text="cm")
lbl_inclinacion_tanque.grid(row=6, column=0, sticky=tk.E)
ent_inclinacion_tanque.grid(row=6, column=1)
unt_inclinacion_tanque.grid(row=6, column=2)

lbl_correccion_cinta = tk.Label(
    master=frm_datos, text="Correción de la cinta master:")
ent_correccion_cinta = tk.Entry(master=frm_datos, width=10)
lbl_correccion_cinta.grid(row=7, column=0, sticky=tk.E)
ent_correccion_cinta.grid(row=7, column=1)

lbl_temp_acero = tk.Label(master=frm_datos, text="*Temp. del Acero:")
ent_temp_acero = tk.Entry(master=frm_datos, width=10)
unt_temp_acero = tk.Label(master=frm_datos, text="°F")
lbl_temp_acero.grid(row=8, column=0, sticky=tk.E)
ent_temp_acero.grid(row=8, column=1)
unt_temp_acero.grid(row=8, column=2)

lbl_altura_tanque = tk.Label(master=frm_datos, text="*Altura Tanque:")
ent_altura_tanque = tk.Entry(master=frm_datos, width=10)
unt_altura_tanque = tk.Label(master=frm_datos, text="cm")
lbl_altura_tanque.grid(row=9, column=0, sticky=tk.E)
ent_altura_tanque.grid(row=9, column=1)
unt_altura_tanque.grid(row=9, column=2)

lbl_altura_base_inicial_cm0 = tk.Label(
    master=frm_datos, text="*Base inicial (Altura 0cm):")
ent_altura_base_inicial_cm0 = tk.Entry(master=frm_datos, width=10)
unt_altura_base_inicial_cm0 = tk.Label(master=frm_datos, text="Litros/cm")
lbl_altura_base_inicial_cm0.grid(row=10, column=0, sticky=tk.E)
ent_altura_base_inicial_cm0.grid(row=10, column=1)
unt_altura_base_inicial_cm0.grid(row=10, column=2)

# Creacion de formulario de fondo del tanque
frm_form_22 = tk.Frame(master=p2, relief=tk.GROOVE,
                       width=200, height=100, borderwidth=3)
frm_form_22.pack(side=tk.LEFT, padx=20, pady=10)
frm_titulo_fondo = tk.Frame(master=frm_form_22, borderwidth=3)
frm_titulo_fondo.pack()
label = tk.Label(master=frm_titulo_fondo, text="Fondo del Tanque")
label.pack()
frm_fondo_tanque = tk.Frame(
    master=frm_form_22, width=200, height=100, borderwidth=3)
frm_fondo_tanque.pack(side=tk.LEFT, padx=20, pady=10)

# Creando labels y entradas para obtener informacion de fondo del tanque
lbl_tipo_fondo = tk.Label(master=frm_fondo_tanque, text="Tipo de Fondo:")
ent_tipo_fondo = tk.Entry(master=frm_fondo_tanque, width=10)
lbl_tipo_fondo.grid(row=0, column=0, sticky="e")
ent_tipo_fondo.grid(row=0, column=1)

lbl_altura_cono = tk.Label(master=frm_fondo_tanque, text="Altura del cono:")
ent_altura_cono = tk.Entry(master=frm_fondo_tanque, width=10)
unt_altura_cono = tk.Label(master=frm_fondo_tanque, text="m")
lbl_altura_cono.grid(row=1, column=0, sticky="e")
ent_altura_cono.grid(row=1, column=1)
unt_altura_cono.grid(row=1, column=2)

lbl_prd = tk.Label(master=frm_fondo_tanque, text="*Producto del tanque:")
ent_prd = tk.Entry(master=frm_fondo_tanque, width=10)
lbl_prd.grid(row=2, column=0, sticky="e")
ent_prd.grid(row=2, column=1)

lbl_est = tk.Label(master=frm_fondo_tanque, text="*G.E. Estacionaria:")
ent_est = tk.Entry(master=frm_fondo_tanque, width=10)
lbl_est.grid(row=3, column=0, sticky="e")
ent_est.grid(row=3, column=1)


# Creacion de formulario de fondo del tanque
frm_form_23 = tk.Frame(master=p2, relief=tk.GROOVE,
                       width=200, height=100, borderwidth=3)
frm_form_23.pack(side=tk.LEFT, padx=20, pady=10)
frm_titulo_techo = tk.Frame(master=frm_form_23, borderwidth=3)
frm_titulo_techo.pack()
label = tk.Label(master=frm_titulo_techo, text="Techo del Tanque")
label.pack()
frm_techo_tanque = tk.Frame(
    master=frm_form_23, width=200, height=100, borderwidth=3)
frm_techo_tanque.pack(side=tk.LEFT, padx=20, pady=10)

# Creando labels y entradas para obtener informacion de fondo del tanque
lbl_tipo_techo = tk.Label(master=frm_techo_tanque, text="Tipo de Techo:")
ent_tipo_techo = tk.Entry(master=frm_techo_tanque, width=10)
lbl_tipo_techo.grid(row=0, column=0, sticky="e")
ent_tipo_techo.grid(row=0, column=1)

lbl_peso_techo = tk.Label(master=frm_techo_tanque, text="Peso del Techo:")
ent_peso_techo = tk.Entry(master=frm_techo_tanque, width=10)
unt_peso_techo = tk.Label(master=frm_techo_tanque, text="lb")
lbl_peso_techo.grid(row=1, column=0, sticky="e")
ent_peso_techo.grid(row=1, column=1)
unt_peso_techo.grid(row=1, column=2)

lbl_altura_crt_inf = tk.Label(
    master=frm_techo_tanque, text="Altura Critica Inferior:")
ent_altura_crt_inf = tk.Entry(master=frm_techo_tanque, width=10)
unt_altura_crt_inf = tk.Label(master=frm_techo_tanque, text="cm")
lbl_altura_crt_inf.grid(row=2, column=0, sticky="e")
ent_altura_crt_inf.grid(row=2, column=1)
unt_altura_crt_inf.grid(row=2, column=2)

lbl_altura_crt_sup = tk.Label(
    master=frm_techo_tanque, text="Altura Critica Superior:")
ent_altura_crt_sup = tk.Entry(master=frm_techo_tanque, width=10)
unt_altura_crt_sup = tk.Label(master=frm_techo_tanque, text="cm")
lbl_altura_crt_sup.grid(row=3, column=0, sticky="e")
ent_altura_crt_sup.grid(row=3, column=1)
unt_altura_crt_sup.grid(row=3, column=2)

lbl_densidad_fluido = tk.Label(
    master=frm_techo_tanque, text="Densidad del fluido:")
ent_densidad_fluido = tk.Entry(master=frm_techo_tanque, width=10)
unt_densidad_fluido = tk.Label(master=frm_techo_tanque, text="lb/gal")
lbl_densidad_fluido.grid(row=4, column=0, sticky="e")
ent_densidad_fluido.grid(row=4, column=1)
unt_densidad_fluido.grid(row=4, column=2)

# Datos de circunferencias
frm_titulo_cir = tk.Frame(master=p3, borderwidth=3)
frm_titulo_cir.pack()
label = tk.Label(master=frm_titulo_cir, text="Datos de circunferencias")
label.pack()
# Diametro promedio
# frm_form_3= tk.Frame(master=p3, relief=tk.GROOVE,width=200, height=100,borderwidth=3)
# frm_form_3.pack(side=tk.LEFT,padx=20, pady=10)
# frm_titulo_diametro = tk.Frame(master=frm_form_3,borderwidth=3)
# frm_titulo_diametro.pack()
# label = tk.Label(master=frm_titulo_diametro, text="Diametro promedio")
# label.pack()
# frm_diametro_promedio = tk.Frame(master=frm_form_3, width=200, height=100,borderwidth=3)
# frm_diametro_promedio.pack(side=tk.LEFT,padx=20, pady=10)
# #Datos de anillos
# lbl_dp_a1 = tk.Label(master=frm_diametro_promedio, text="Anillo 1")
# ent_dp_a1 = tk.Entry(master=frm_diametro_promedio, width=10)
# unt_dp_a1 = tk.Label(master=frm_diametro_promedio, text="m")
# lbl_dp_a1.grid(row=0, column=0, sticky="e")
# ent_dp_a1.grid(row=0, column=1)
# unt_dp_a1.grid(row=0,column=2)

# lbl_dp_a2 = tk.Label(master=frm_diametro_promedio, text="Anillo 2")
# ent_dp_a2 = tk.Entry(master=frm_diametro_promedio, width=10)
# unt_dp_a2 = tk.Label(master=frm_diametro_promedio, text="m")
# lbl_dp_a2.grid(row=1, column=0, sticky="e")
# ent_dp_a2.grid(row=1, column=1)
# unt_dp_a2.grid(row=1,column=2)

# lbl_dp_a3 = tk.Label(master=frm_diametro_promedio, text="Anillo 3")
# ent_dp_a3 = tk.Entry(master=frm_diametro_promedio, width=10)
# unt_dp_a3 = tk.Label(master=frm_diametro_promedio, text="m")
# lbl_dp_a3.grid(row=2, column=0, sticky="e")
# ent_dp_a3.grid(row=2, column=1)
# unt_dp_a3.grid(row=2,column=2)

# lbl_dp_a4 = tk.Label(master=frm_diametro_promedio, text="Anillo 4")
# ent_dp_a4 = tk.Entry(master=frm_diametro_promedio, width=10)
# unt_dp_a4 = tk.Label(master=frm_diametro_promedio, text="m")
# lbl_dp_a4.grid(row=3, column=0, sticky="e")
# ent_dp_a4.grid(row=3, column=1)
# unt_dp_a4.grid(row=3,column=2)

# lbl_dp_a5 = tk.Label(master=frm_diametro_promedio, text="Anillo 5")
# ent_dp_a5 = tk.Entry(master=frm_diametro_promedio, width=10)
# unt_dp_a5 = tk.Label(master=frm_diametro_promedio, text="m")
# lbl_dp_a5.grid(row=4, column=0, sticky="e")
# ent_dp_a5.grid(row=4, column=1)
# unt_dp_a5.grid(row=4,column=2)

# lbl_dp_a6 = tk.Label(master=frm_diametro_promedio, text="Anillo 6")
# ent_dp_a6 = tk.Entry(master=frm_diametro_promedio, width=10)
# unt_dp_a6 = tk.Label(master=frm_diametro_promedio, text="m")
# lbl_dp_a6.grid(row=5, column=0, sticky="e")
# ent_dp_a6.grid(row=5, column=1)
# unt_dp_a6.grid(row=5,column=2)

# lbl_dp_a7 = tk.Label(master=frm_diametro_promedio, text="Anillo 7")
# ent_dp_a7 = tk.Entry(master=frm_diametro_promedio, width=10)
# unt_dp_a7 = tk.Label(master=frm_diametro_promedio, text="m")
# lbl_dp_a7.grid(row=6, column=0, sticky="e")
# ent_dp_a7.grid(row=6, column=1)
# unt_dp_a7.grid(row=6,column=2)

# lbl_dp_a8 = tk.Label(master=frm_diametro_promedio, text="Anillo 8")
# ent_dp_a8 = tk.Entry(master=frm_diametro_promedio, width=10)
# unt_dp_a8 = tk.Label(master=frm_diametro_promedio, text="m")
# lbl_dp_a8.grid(row=7, column=0, sticky="e")
# ent_dp_a8.grid(row=7, column=1)
# unt_dp_a8.grid(row=7,column=2)

# lbl_dp_a9 = tk.Label(master=frm_diametro_promedio, text="Anillo 9")
# ent_dp_a9 = tk.Entry(master=frm_diametro_promedio, width=10)
# unt_dp_a9 = tk.Label(master=frm_diametro_promedio, text="m")
# lbl_dp_a9.grid(row=8, column=0, sticky="e")
# ent_dp_a9.grid(row=8, column=1)
# unt_dp_a9.grid(row=8,column=2)

# lbl_dp_a10 = tk.Label(master=frm_diametro_promedio, text="Anillo 10")
# ent_dp_a10 = tk.Entry(master=frm_diametro_promedio, width=10)
# unt_dp_a10 = tk.Label(master=frm_diametro_promedio, text="m")
# lbl_dp_a10.grid(row=9, column=0, sticky="e")
# ent_dp_a10.grid(row=9, column=1)
# unt_dp_a10.grid(row=9,column=2)

# Circunferencia promedio
frm_form_32 = tk.Frame(master=p3, relief=tk.GROOVE,
                       width=200, height=100, borderwidth=3)
frm_form_32.pack(side=tk.LEFT, padx=20, pady=10)
frm_titulo_circunferencia = tk.Frame(master=frm_form_32, borderwidth=3)
frm_titulo_circunferencia.pack()
label = tk.Label(master=frm_titulo_circunferencia,
                 text="Circunferencia promedio al \n20% y 80%")
label.pack()
frm_circunferencia_promedio = tk.Frame(
    master=frm_form_32, width=200, height=100, borderwidth=3)
frm_circunferencia_promedio.pack(side=tk.LEFT, padx=20, pady=10)
# Datos de anillos
lbl_cp_c1 = tk.Label(master=frm_circunferencia_promedio,
                     text="Circunferencia 1")
ent_cp_c1 = tk.Entry(master=frm_circunferencia_promedio, width=10)
unt_cp_c1 = tk.Label(master=frm_circunferencia_promedio, text="ft")
ent_cp_c1_80 = tk.Entry(master=frm_circunferencia_promedio, width=10)
unt_cp_c1_80 = tk.Label(master=frm_circunferencia_promedio, text="ft")
result_cp1 = tk.Label(master=frm_circunferencia_promedio)
lbl_cp_c1.grid(row=0, column=0, sticky="e")
ent_cp_c1.grid(row=0, column=1)
unt_cp_c1.grid(row=0, column=2)
ent_cp_c1_80.grid(row=0, column=3)
unt_cp_c1_80.grid(row=0, column=4)
result_cp1.grid(row=0, column=5)

lbl_cp_c2 = tk.Label(master=frm_circunferencia_promedio,
                     text="Circunferencia 2")
ent_cp_c2 = tk.Entry(master=frm_circunferencia_promedio, width=10)
unt_cp_c2 = tk.Label(master=frm_circunferencia_promedio, text="ft")
ent_cp_c2_80 = tk.Entry(master=frm_circunferencia_promedio, width=10)
unt_cp_c2_80 = tk.Label(master=frm_circunferencia_promedio, text="ft")
result_cp2 = tk.Label(master=frm_circunferencia_promedio)
lbl_cp_c2.grid(row=1, column=0, sticky="e")
ent_cp_c2.grid(row=1, column=1)
unt_cp_c2.grid(row=1, column=2)
ent_cp_c2_80.grid(row=1, column=3)
unt_cp_c2_80.grid(row=1, column=4)
result_cp2.grid(row=1, column=5)

lbl_cp_c3 = tk.Label(master=frm_circunferencia_promedio,
                     text="Circunferencia 3")
ent_cp_c3 = tk.Entry(master=frm_circunferencia_promedio, width=10)
unt_cp_c3 = tk.Label(master=frm_circunferencia_promedio, text="ft")
ent_cp_c3_80 = tk.Entry(master=frm_circunferencia_promedio, width=10)
unt_cp_c3_80 = tk.Label(master=frm_circunferencia_promedio, text="ft")
result_cp3 = tk.Label(master=frm_circunferencia_promedio)
lbl_cp_c3.grid(row=2, column=0, sticky="e")
ent_cp_c3.grid(row=2, column=1)
unt_cp_c3.grid(row=2, column=2)
ent_cp_c3_80.grid(row=2, column=3)
unt_cp_c3_80.grid(row=2, column=4)
result_cp3.grid(row=2, column=5)

lbl_cp_c4 = tk.Label(master=frm_circunferencia_promedio,
                     text="Circunferencia 4")
ent_cp_c4 = tk.Entry(master=frm_circunferencia_promedio, width=10)
unt_cp_c4 = tk.Label(master=frm_circunferencia_promedio, text="ft")
ent_cp_c4_80 = tk.Entry(master=frm_circunferencia_promedio, width=10)
unt_cp_c4_80 = tk.Label(master=frm_circunferencia_promedio, text="ft")
result_cp4 = tk.Label(master=frm_circunferencia_promedio)
lbl_cp_c4.grid(row=3, column=0, sticky="e")
ent_cp_c4.grid(row=3, column=1)
unt_cp_c4.grid(row=3, column=2)
ent_cp_c4_80.grid(row=3, column=3)
unt_cp_c4_80.grid(row=3, column=4)
result_cp4.grid(row=3, column=5)

lbl_cp_c5 = tk.Label(master=frm_circunferencia_promedio,
                     text="Circunferencia 5")
ent_cp_c5 = tk.Entry(master=frm_circunferencia_promedio, width=10)
unt_cp_c5 = tk.Label(master=frm_circunferencia_promedio, text="ft")
ent_cp_c5_80 = tk.Entry(master=frm_circunferencia_promedio, width=10)
unt_cp_c5_80 = tk.Label(master=frm_circunferencia_promedio, text="ft")
result_cp5 = tk.Label(master=frm_circunferencia_promedio)
lbl_cp_c5.grid(row=4, column=0, sticky="e")
ent_cp_c5.grid(row=4, column=1)
unt_cp_c5.grid(row=4, column=2)
ent_cp_c5_80.grid(row=4, column=3)
unt_cp_c5_80.grid(row=4, column=4)
result_cp5.grid(row=4, column=5)


lbl_dp_c6 = tk.Label(master=frm_circunferencia_promedio,
                     text="Circunferencia 6")
ent_dp_c6 = tk.Entry(master=frm_circunferencia_promedio, width=10)
unt_dp_c6 = tk.Label(master=frm_circunferencia_promedio, text="ft")
ent_cp_c6_80 = tk.Entry(master=frm_circunferencia_promedio, width=10)
unt_cp_c6_80 = tk.Label(master=frm_circunferencia_promedio, text="ft")
result_cp6 = tk.Label(master=frm_circunferencia_promedio)
lbl_dp_c6.grid(row=5, column=0, sticky="e")
ent_dp_c6.grid(row=5, column=1)
unt_dp_c6.grid(row=5, column=2)
ent_cp_c6_80.grid(row=5, column=3)
unt_cp_c6_80.grid(row=5, column=4)
result_cp6.grid(row=5, column=5)

lbl_dp_c7 = tk.Label(master=frm_circunferencia_promedio,
                     text="Circunferencia 7")
ent_dp_c7 = tk.Entry(master=frm_circunferencia_promedio, width=10)
unt_dp_c7 = tk.Label(master=frm_circunferencia_promedio, text="ft")
ent_cp_c7_80 = tk.Entry(master=frm_circunferencia_promedio, width=10)
unt_cp_c7_80 = tk.Label(master=frm_circunferencia_promedio, text="ft")
result_cp7 = tk.Label(master=frm_circunferencia_promedio)
lbl_dp_c7.grid(row=6, column=0, sticky="e")
ent_dp_c7.grid(row=6, column=1)
unt_dp_c7.grid(row=6, column=2)
ent_cp_c7_80.grid(row=6, column=3)
unt_cp_c7_80.grid(row=6, column=4)
result_cp7.grid(row=6, column=5)

lbl_dp_c8 = tk.Label(master=frm_circunferencia_promedio,
                     text="Circunferencia 8")
ent_dp_c8 = tk.Entry(master=frm_circunferencia_promedio, width=10)
unt_dp_c8 = tk.Label(master=frm_circunferencia_promedio, text="ft")
ent_cp_c8_80 = tk.Entry(master=frm_circunferencia_promedio, width=10)
unt_cp_c8_80 = tk.Label(master=frm_circunferencia_promedio, text="ft")
result_cp8 = tk.Label(master=frm_circunferencia_promedio)
lbl_dp_c8.grid(row=7, column=0, sticky="e")
ent_dp_c8.grid(row=7, column=1)
unt_dp_c8.grid(row=7, column=2)
ent_cp_c8_80.grid(row=7, column=3)
unt_cp_c8_80.grid(row=7, column=4)
result_cp8.grid(row=7, column=5)

lbl_dp_c9 = tk.Label(master=frm_circunferencia_promedio,
                     text="Circunferencia 9")
ent_dp_c9 = tk.Entry(master=frm_circunferencia_promedio, width=10)
unt_dp_c9 = tk.Label(master=frm_circunferencia_promedio, text="ft")
ent_cp_c9_80 = tk.Entry(master=frm_circunferencia_promedio, width=10)
unt_cp_c9_80 = tk.Label(master=frm_circunferencia_promedio, text="ft")
result_cp9 = tk.Label(master=frm_circunferencia_promedio)
lbl_dp_c9.grid(row=8, column=0, sticky="e")
ent_dp_c9.grid(row=8, column=1)
unt_dp_c9.grid(row=8, column=2)
ent_cp_c9_80.grid(row=8, column=3)
unt_cp_c9_80.grid(row=8, column=4)
result_cp9.grid(row=8, column=5)

lbl_dp_c10 = tk.Label(master=frm_circunferencia_promedio,
                      text="Circunferencia 10")
ent_dp_c10 = tk.Entry(master=frm_circunferencia_promedio, width=10)
unt_dp_c10 = tk.Label(master=frm_circunferencia_promedio, text="ft")
ent_cp_c10_80 = tk.Entry(master=frm_circunferencia_promedio, width=10)
unt_cp_c10_80 = tk.Label(master=frm_circunferencia_promedio, text="ft")
result_cp10 = tk.Label(master=frm_circunferencia_promedio)
lbl_dp_c10.grid(row=9, column=0, sticky="e")
ent_dp_c10.grid(row=9, column=1)
unt_dp_c10.grid(row=9, column=2)
ent_cp_c10_80.grid(row=9, column=3)
unt_cp_c10_80.grid(row=9, column=4)
result_cp10.grid(row=9, column=5)

# Espesor promedio
# frm_form_33= tk.Frame(master=p3, relief=tk.GROOVE,width=200, height=100,borderwidth=3)
# frm_form_33.pack(side=tk.LEFT,padx=20, pady=10)
# frm_titulo_espesor = tk.Frame(master=frm_form_33,borderwidth=3)
# frm_titulo_espesor.pack()
# label = tk.Label(master=frm_titulo_espesor, text="Espesor promedio al \n20% y 80%")
# label.pack()
# frm_espesor_promedio = tk.Frame(master=frm_form_33, width=200, height=100,borderwidth=3)
# frm_espesor_promedio.pack(side=tk.LEFT,padx=20, pady=10)
# Datos de anillos para espesores
# lbl_ep_a1 = tk.Label(master=frm_espesor_promedio, text="Anillo x1")
# ent_ep_a1 = tk.Entry(master=frm_espesor_promedio, width=10)
# unt_ep_a1 = tk.Label(master=frm_espesor_promedio, text="in")
# ent_ep_a1_80 = tk.Entry(master=frm_espesor_promedio, width=10)
# unt_ep_a1_80 = tk.Label(master=frm_espesor_promedio, text="in")
# result_esp1 = tk.Label(master=frm_espesor_promedio)
# lbl_ep_a1.grid(row=0, column=0, sticky="e")
# ent_ep_a1.grid(row=0, column=1)
# unt_ep_a1.grid(row=0,column=2)
# ent_ep_a1_80.grid(row=0, column=3)
# unt_ep_a1_80.grid(row=0,column=4)
# result_esp1.grid(row=0,column=5)

# lbl_ep_a2 = tk.Label(master=frm_espesor_promedio, text="Anillo x2")
# ent_ep_a2 = tk.Entry(master=frm_espesor_promedio, width=10)
# unt_ep_a2 = tk.Label(master=frm_espesor_promedio, text="in")
# ent_ep_a2_80 = tk.Entry(master=frm_espesor_promedio, width=10)
# unt_ep_a2_80 = tk.Label(master=frm_espesor_promedio, text="in")
# result_esp2 = tk.Label(master=frm_espesor_promedio)
# lbl_ep_a2.grid(row=1, column=0, sticky="e")
# ent_ep_a2.grid(row=1, column=1)
# unt_ep_a2.grid(row=1,column=2)
# ent_ep_a2_80.grid(row=1, column=3)
# unt_ep_a2_80.grid(row=1,column=4)
# result_esp2.grid(row=1,column=5)

# lbl_ep_a3 = tk.Label(master=frm_espesor_promedio, text="Anillo x3")
# ent_ep_a3 = tk.Entry(master=frm_espesor_promedio, width=10)
# unt_ep_a3 = tk.Label(master=frm_espesor_promedio, text="in")
# ent_ep_a3_80 = tk.Entry(master=frm_espesor_promedio, width=10)
# unt_ep_a3_80 = tk.Label(master=frm_espesor_promedio, text="in")
# result_esp3 = tk.Label(master=frm_espesor_promedio)
# lbl_ep_a3.grid(row=2, column=0, sticky="e")
# ent_ep_a3.grid(row=2, column=1)
# unt_ep_a3.grid(row=2,column=2)
# ent_ep_a3_80.grid(row=2, column=3)
# unt_ep_a3_80.grid(row=2,column=4)
# result_esp3.grid(row=2,column=5)

# lbl_ep_a4 = tk.Label(master=frm_espesor_promedio, text="Anillo x4")
# ent_ep_a4 = tk.Entry(master=frm_espesor_promedio, width=10)
# unt_ep_a4 = tk.Label(master=frm_espesor_promedio, text="in")
# ent_ep_a4_80 = tk.Entry(master=frm_espesor_promedio, width=10)
# unt_ep_a4_80 = tk.Label(master=frm_espesor_promedio, text="in")
# result_esp4 = tk.Label(master=frm_espesor_promedio)
# lbl_ep_a3.grid(row=2, column=0, sticky="e")
# lbl_ep_a4.grid(row=3, column=0, sticky="e")
# ent_ep_a4.grid(row=3, column=1)
# unt_ep_a4.grid(row=3,column=2)
# ent_ep_a4_80.grid(row=3, column=3)
# unt_ep_a4_80.grid(row=3,column=4)
# result_esp4.grid(row=3,column=5)

# lbl_ep_a5 = tk.Label(master=frm_espesor_promedio, text="Anillo x5")
# ent_ep_a5 = tk.Entry(master=frm_espesor_promedio, width=10)
# unt_ep_a5 = tk.Label(master=frm_espesor_promedio, text="in")
# ent_ep_a5_80 = tk.Entry(master=frm_espesor_promedio, width=10)
# unt_ep_a5_80 = tk.Label(master=frm_espesor_promedio, text="in")
# result_esp5 = tk.Label(master=frm_espesor_promedio)
# lbl_ep_a5.grid(row=4, column=0, sticky="e")
# ent_ep_a5.grid(row=4, column=1)
# unt_ep_a5.grid(row=4,column=2)
# ent_ep_a5_80.grid(row=4, column=3)
# unt_ep_a5_80.grid(row=4,column=4)
# result_esp5.grid(row=4,column=5)

# lbl_ep_a6 = tk.Label(master=frm_espesor_promedio, text="Anillo x6")
# ent_ep_a6 = tk.Entry(master=frm_espesor_promedio, width=10)
# unt_ep_a6 = tk.Label(master=frm_espesor_promedio, text="in")
# ent_ep_a6_80 = tk.Entry(master=frm_espesor_promedio, width=10)
# unt_ep_a6_80 = tk.Label(master=frm_espesor_promedio, text="in")
# result_esp6 = tk.Label(master=frm_espesor_promedio)
# lbl_ep_a6.grid(row=5, column=0, sticky="e")
# ent_ep_a6.grid(row=5, column=1)
# unt_ep_a6.grid(row=5,column=2)
# ent_ep_a6_80.grid(row=5, column=3)
# unt_ep_a6_80.grid(row=5,column=4)
# result_esp6.grid(row=5,column=5)

# lbl_ep_a7 = tk.Label(master=frm_espesor_promedio, text="Anillo x7")
# ent_ep_a7 = tk.Entry(master=frm_espesor_promedio, width=10)
# unt_ep_a7 = tk.Label(master=frm_espesor_promedio, text="in")
# ent_ep_a7_80 = tk.Entry(master=frm_espesor_promedio, width=10)
# unt_ep_a7_80 = tk.Label(master=frm_espesor_promedio, text="in")
# result_esp7 = tk.Label(master=frm_espesor_promedio)
# lbl_ep_a7.grid(row=6, column=0, sticky="e")
# ent_ep_a7.grid(row=6, column=1)
# unt_ep_a7.grid(row=6,column=2)
# ent_ep_a7_80.grid(row=6, column=3)
# unt_ep_a7_80.grid(row=6,column=4)
# result_esp7.grid(row=6,column=5)

# lbl_ep_a8 = tk.Label(master=frm_espesor_promedio, text="Anillo x8")
# ent_ep_a8 = tk.Entry(master=frm_espesor_promedio, width=10)
# unt_ep_a8 = tk.Label(master=frm_espesor_promedio, text="in")
# ent_ep_a8_80 = tk.Entry(master=frm_espesor_promedio, width=10)
# unt_ep_a8_80 = tk.Label(master=frm_espesor_promedio, text="in")
# result_esp8 = tk.Label(master=frm_espesor_promedio)
# lbl_ep_a8.grid(row=7, column=0, sticky="e")
# ent_ep_a8.grid(row=7, column=1)
# unt_ep_a8.grid(row=7,column=2)
# ent_ep_a8_80.grid(row=7, column=3)
# unt_ep_a8_80.grid(row=7,column=4)
# result_esp8.grid(row=7,column=5)

# lbl_ep_a9 = tk.Label(master=frm_espesor_promedio, text="Anillo x9")
# ent_ep_a9 = tk.Entry(master=frm_espesor_promedio, width=10)
# unt_ep_a9 = tk.Label(master=frm_espesor_promedio, text="in")
# ent_ep_a9_80 = tk.Entry(master=frm_espesor_promedio, width=10)
# unt_ep_a9_80 = tk.Label(master=frm_espesor_promedio, text="in")
# result_esp9 = tk.Label(master=frm_espesor_promedio)
# lbl_ep_a9.grid(row=8, column=0, sticky="e")
# ent_ep_a9.grid(row=8, column=1)
# unt_ep_a9.grid(row=8,column=2)
# ent_ep_a9_80.grid(row=8, column=3)
# unt_ep_a9_80.grid(row=8,column=4)
# result_esp9.grid(row=8,column=5)

# lbl_ep_a10 = tk.Label(master=frm_espesor_promedio, text="Anillo x10")
# ent_ep_a10 = tk.Entry(master=frm_espesor_promedio, width=10)
# unt_ep_a10 = tk.Label(master=frm_espesor_promedio, text="in")
# ent_ep_a10_80 = tk.Entry(master=frm_espesor_promedio, width=10)
# unt_ep_a10_80 = tk.Label(master=frm_espesor_promedio, text="in")
# result_esp10 = tk.Label(master=frm_espesor_promedio)
# lbl_ep_a10.grid(row=9, column=0, sticky="e")
# ent_ep_a10.grid(row=9, column=1)
# unt_ep_a10.grid(row=9,column=2)
# ent_ep_a10_80.grid(row=9, column=3)
# unt_ep_a10_80.grid(row=9,column=4)
# result_esp10.grid(row=9,column=5)

# Promedio circunferencia y espesor al 20 y 80


def promedioCirc():
    value = float(ent_cp_c1.get())
    value2 = float(ent_cp_c1_80.get())
    result_cp1["text"] = f"{(value+value2)/2}" + " ft"
    v21 = float(ent_cp_c2.get())
    v22 = float(ent_cp_c2_80.get())
    result_cp2["text"] = f"{(v21+v22)/2}" + " ft"
    v31 = float(ent_cp_c3.get())
    v32 = float(ent_cp_c3_80.get())
    result_cp3["text"] = f"{(v31+v32)/2}" + " ft"
    v41 = float(ent_cp_c4.get())
    v42 = float(ent_cp_c4_80.get())
    result_cp4["text"] = f"{(v41+v42)/2}" + " ft"
    v51 = float(ent_cp_c5.get())
    v52 = float(ent_cp_c5_80.get())
    result_cp5["text"] = f"{(v51+v52)/2}" + " ft"
    v61 = float(ent_dp_c6.get())
    v62 = float(ent_cp_c6_80.get())
    result_cp6["text"] = f"{(v61+v62)/2}" + " ft"
    v71 = float(ent_dp_c7.get())
    v72 = float(ent_cp_c7_80.get())
    result_cp7["text"] = f"{(v71+v72)/2}" + " ft"
    v81 = float(ent_dp_c8.get())
    v82 = float(ent_cp_c8_80.get())
    result_cp8["text"] = f"{(v81+v82)/2}" + " ft"
    v91 = float(ent_dp_c9.get())
    v92 = float(ent_cp_c9_80.get())
    result_cp9["text"] = f"{(v91+v92)/2}" + " ft"
    v101 = float(ent_dp_c10.get())
    v102 = float(ent_cp_c10_80.get())
    result_cp10["text"] = f"{(v101+v102)/2}" + " ft"
    e11 = float(ent_ep_a1.get())
    e12 = float(ent_ep_a1_80.get())
    result_esp1["text"] = f"{(e11+e12)/2}" + " in"
    e21 = float(ent_ep_a2.get())
    e22 = float(ent_ep_a2_80.get())
    result_esp2["text"] = f"{(e21+e22)/2}" + " in"
    e31 = float(ent_ep_a3.get())
    e32 = float(ent_ep_a3_80.get())
    result_esp3["text"] = f"{(e31+e32)/2}" + " in"
    e41 = float(ent_ep_a4.get())
    e42 = float(ent_ep_a4_80.get())
    result_esp4["text"] = f"{(e41+e42)/2}" + " in"
    e51 = float(ent_ep_a5.get())
    e52 = float(ent_ep_a5_80.get())
    result_esp5["text"] = f"{(e51+e52)/2}" + " in"
    e61 = float(ent_ep_a6.get())
    e62 = float(ent_ep_a6_80.get())
    result_esp6["text"] = f"{(e61+e62)/2}" + " in"
    e71 = float(ent_ep_a7.get())
    e72 = float(ent_ep_a7_80.get())
    result_esp7["text"] = f"{(e71+e72)/2}" + " in"
    e81 = float(ent_ep_a8.get())
    e82 = float(ent_ep_a8_80.get())
    result_esp8["text"] = f"{(e81+e82)/2}" + " in"
    e91 = float(ent_ep_a9.get())
    e92 = float(ent_ep_a9_80.get())
    result_esp9["text"] = f"{(e91+e92)/2}" + " in"
    e101 = float(ent_ep_a10.get())
    e102 = float(ent_ep_a10_80.get())
    result_esp10["text"] = f"{(e101+e102)/2}" + " in"


# Alturas, espesores y juntas
frm_titulo_alt = tk.Frame(master=p4, borderwidth=3)
frm_titulo_alt.pack()
label_juntas = tk.Label(master=frm_titulo_alt,
                        text="Datos de juntas\n TIPO: Soldada")
label_juntas.pack()
# Datos de alturas
frm_form_4 = tk.Frame(master=p4, relief=tk.GROOVE,
                      width=200, height=100, borderwidth=3)
frm_form_4.pack(side=tk.LEFT, padx=20, pady=10)
frm_titulo_altura = tk.Frame(master=frm_form_4, borderwidth=3)
frm_titulo_altura.pack()
label_altura = tk.Label(master=frm_titulo_altura,
                        text="Datos de Alturas\t\t\t\t\t Altura Stress")
label_altura.pack()
frm_alturas = tk.Frame(master=frm_form_4, width=200, height=100, borderwidth=3)
frm_alturas.pack(side=tk.LEFT, padx=20, pady=10)
# Datos de anillos para espesores
lbl_da_a1 = tk.Label(master=frm_alturas, text="Anillo h1")
ent_da_a1 = tk.Entry(master=frm_alturas, width=10)
unt_da_a1 = tk.Label(master=frm_alturas, text="cm")
lbl_ce_a1 = tk.Label(master=frm_alturas, text="Cir. ext.")
ent_ce_a1 = tk.Entry(master=frm_alturas, width=10)
unt_ce_a1 = tk.Label(master=frm_alturas, text="cm")
result_ce_a1 = tk.Label(master=frm_alturas)
lbl_da_a1.grid(row=0, column=0, sticky="e")
ent_da_a1.grid(row=0, column=1)
unt_da_a1.grid(row=0, column=2)
lbl_ce_a1.grid(row=0, column=3, sticky="e")
ent_ce_a1.grid(row=0, column=4)
unt_ce_a1.grid(row=0, column=5)
result_ce_a1.grid(row=0, column=6)

lbl_da_a2 = tk.Label(master=frm_alturas, text="Anillo h2")
ent_da_a2 = tk.Entry(master=frm_alturas, width=10)
unt_da_a2 = tk.Label(master=frm_alturas, text="cm")
lbl_ce_a2 = tk.Label(master=frm_alturas, text="Cir. ext.")
ent_ce_a2 = tk.Entry(master=frm_alturas, width=10)
unt_ce_a2 = tk.Label(master=frm_alturas, text="cm")
result_ce_a2 = tk.Label(master=frm_alturas)
lbl_da_a2.grid(row=1, column=0, sticky="e")
ent_da_a2.grid(row=1, column=1)
unt_da_a2.grid(row=1, column=2)
lbl_ce_a2.grid(row=1, column=3, sticky="e")
ent_ce_a2.grid(row=1, column=4)
unt_ce_a2.grid(row=1, column=5)
result_ce_a2.grid(row=1, column=6)

lbl_da_a3 = tk.Label(master=frm_alturas, text="Anillo h3")
ent_da_a3 = tk.Entry(master=frm_alturas, width=10)
unt_da_a3 = tk.Label(master=frm_alturas, text="cm")
lbl_ce_a3 = tk.Label(master=frm_alturas, text="Cir. ext.")
ent_ce_a3 = tk.Entry(master=frm_alturas, width=10)
unt_ce_a3 = tk.Label(master=frm_alturas, text="cm")
result_ce_a3 = tk.Label(master=frm_alturas)
lbl_da_a3.grid(row=2, column=0, sticky="e")
ent_da_a3.grid(row=2, column=1)
unt_da_a3.grid(row=2, column=2)
lbl_ce_a3.grid(row=2, column=3, sticky="e")
ent_ce_a3.grid(row=2, column=4)
unt_ce_a3.grid(row=2, column=5)
result_ce_a3.grid(row=2, column=6)

lbl_da_a4 = tk.Label(master=frm_alturas, text="Anillo h4")
ent_da_a4 = tk.Entry(master=frm_alturas, width=10)
unt_da_a4 = tk.Label(master=frm_alturas, text="cm")
lbl_ce_a4 = tk.Label(master=frm_alturas, text="Cir. ext.")
ent_ce_a4 = tk.Entry(master=frm_alturas, width=10)
unt_ce_a4 = tk.Label(master=frm_alturas, text="cm")
result_ce_a4 = tk.Label(master=frm_alturas)
lbl_da_a4.grid(row=3, column=0, sticky="e")
ent_da_a4.grid(row=3, column=1)
unt_da_a4.grid(row=3, column=2)
lbl_ce_a4.grid(row=3, column=3, sticky="e")
ent_ce_a4.grid(row=3, column=4)
unt_ce_a4.grid(row=3, column=5)
result_ce_a4.grid(row=3, column=6)

lbl_da_a5 = tk.Label(master=frm_alturas, text="Anillo h5")
ent_da_a5 = tk.Entry(master=frm_alturas, width=10)
unt_da_a5 = tk.Label(master=frm_alturas, text="cm")
lbl_ce_a5 = tk.Label(master=frm_alturas, text="Cir. ext.")
ent_ce_a5 = tk.Entry(master=frm_alturas, width=10)
unt_ce_a5 = tk.Label(master=frm_alturas, text="cm")
result_ce_a5 = tk.Label(master=frm_alturas)
lbl_da_a5.grid(row=4, column=0, sticky="e")
ent_da_a5.grid(row=4, column=1)
unt_da_a5.grid(row=4, column=2)
lbl_ce_a5.grid(row=4, column=3, sticky="e")
ent_ce_a5.grid(row=4, column=4)
unt_ce_a5.grid(row=4, column=5)
result_ce_a5.grid(row=4, column=6)

lbl_da_a6 = tk.Label(master=frm_alturas, text="Anillo h6")
ent_da_a6 = tk.Entry(master=frm_alturas, width=10)
unt_da_a6 = tk.Label(master=frm_alturas, text="in")
lbl_ce_a6 = tk.Label(master=frm_alturas, text="Cir. ext.")
ent_ce_a6 = tk.Entry(master=frm_alturas, width=10)
unt_ce_a6 = tk.Label(master=frm_alturas, text="cm")
result_ce_a6 = tk.Label(master=frm_alturas)
lbl_da_a6.grid(row=5, column=0, sticky="e")
ent_da_a6.grid(row=5, column=1)
unt_da_a6.grid(row=5, column=2)
lbl_ce_a6.grid(row=5, column=3, sticky="e")
ent_ce_a6.grid(row=5, column=4)
unt_ce_a6.grid(row=5, column=5)
result_ce_a6.grid(row=5, column=6)

lbl_da_a7 = tk.Label(master=frm_alturas, text="Anillo h7")
ent_da_a7 = tk.Entry(master=frm_alturas, width=10)
unt_da_a7 = tk.Label(master=frm_alturas, text="cm")
lbl_ce_a7 = tk.Label(master=frm_alturas, text="Cir. ext.")
ent_ce_a7 = tk.Entry(master=frm_alturas, width=10)
unt_ce_a7 = tk.Label(master=frm_alturas, text="cm")
result_ce_a7 = tk.Label(master=frm_alturas)
lbl_da_a7.grid(row=6, column=0, sticky="e")
ent_da_a7.grid(row=6, column=1)
unt_da_a7.grid(row=6, column=2)
lbl_ce_a7.grid(row=6, column=3, sticky="e")
ent_ce_a7.grid(row=6, column=4)
unt_ce_a7.grid(row=6, column=5)
result_ce_a7.grid(row=6, column=6)

lbl_da_a8 = tk.Label(master=frm_alturas, text="Anillo h8")
ent_da_a8 = tk.Entry(master=frm_alturas, width=10)
unt_da_a8 = tk.Label(master=frm_alturas, text="cm")
lbl_ce_a8 = tk.Label(master=frm_alturas, text="Cir. ext.")
ent_ce_a8 = tk.Entry(master=frm_alturas, width=10)
unt_ce_a8 = tk.Label(master=frm_alturas, text="cm")
result_ce_a8 = tk.Label(master=frm_alturas)
lbl_da_a8.grid(row=7, column=0, sticky="e")
ent_da_a8.grid(row=7, column=1)
unt_da_a8.grid(row=7, column=2)
lbl_ce_a8.grid(row=7, column=3, sticky="e")
ent_ce_a8.grid(row=7, column=4)
unt_ce_a8.grid(row=7, column=5)
result_ce_a8.grid(row=7, column=6)

lbl_da_a9 = tk.Label(master=frm_alturas, text="Anillo h9")
ent_da_a9 = tk.Entry(master=frm_alturas, width=10)
unt_da_a9 = tk.Label(master=frm_alturas, text="cm")
lbl_ce_a9 = tk.Label(master=frm_alturas, text="Cir. ext.")
ent_ce_a9 = tk.Entry(master=frm_alturas, width=10)
unt_ce_a9 = tk.Label(master=frm_alturas, text="cm")
result_ce_a9 = tk.Label(master=frm_alturas)
lbl_da_a9.grid(row=8, column=0, sticky="e")
ent_da_a9.grid(row=8, column=1)
unt_da_a9.grid(row=8, column=2)
lbl_ce_a9.grid(row=8, column=3, sticky="e")
ent_ce_a9.grid(row=8, column=4)
unt_ce_a9.grid(row=8, column=5)
result_ce_a9.grid(row=8, column=6)

lbl_da_a10 = tk.Label(master=frm_alturas, text="Anillo h10")
ent_da_a10 = tk.Entry(master=frm_alturas, width=10)
unt_da_a10 = tk.Label(master=frm_alturas, text="cm")
lbl_ce_a10 = tk.Label(master=frm_alturas, text="Cir. ext.")
ent_ce_a10 = tk.Entry(master=frm_alturas, width=10)
unt_ce_a10 = tk.Label(master=frm_alturas, text="cm")
result_ce_a10 = tk.Label(master=frm_alturas)
lbl_da_a10.grid(row=9, column=0, sticky="e")
ent_da_a10.grid(row=9, column=1)
unt_da_a10.grid(row=9, column=2)
lbl_ce_a10.grid(row=9, column=3, sticky="e")
ent_ce_a10.grid(row=9, column=4)
unt_ce_a10.grid(row=9, column=5)
result_ce_a10.grid(row=9, column=6)

# Funcion para las alturas de juntas


def alturas():
    h1 = float(ent_da_a1.get())
    result_ce_a1["text"] = f"{(h1)}" + " cm"
    h2 = float(ent_da_a2.get())
    h3 = float(ent_da_a3.get())
    h4 = float(ent_da_a4.get())
    h5 = float(ent_da_a5.get())
    h6 = float(ent_da_a6.get())
    h7 = float(ent_da_a7.get())
    h8 = float(ent_da_a8.get())
    h9 = float(ent_da_a9.get())
    h10 = float(ent_da_a10.get())
    result_ce_a10["text"] = f"{(h10-h9)}" + " cm"
    result_ce_a9["text"] = f"{(h9-h8)}" + " cm"
    result_ce_a8["text"] = f"{(h8-h7)}" + " cm"
    result_ce_a7["text"] = f"{(h7-h6)}" + " cm"
    result_ce_a6["text"] = f"{(h6-h5)}" + " cm"
    result_ce_a5["text"] = f"{(h5-h4)}" + " cm"
    result_ce_a4["text"] = f"{(h4-h3)}" + " cm"
    result_ce_a3["text"] = f"{(h3-h2)}" + " cm"
    result_ce_a2["text"] = f"{(h2-h1)}" + " cm"


# Datos de numero juntas
frm_form_41 = tk.Frame(master=p4, relief=tk.GROOVE,
                       width=200, height=100, borderwidth=3)
frm_form_41.pack(side=tk.LEFT, padx=20, pady=10)
frm_titulo_num = tk.Frame(master=frm_form_41, borderwidth=3)
frm_titulo_num.pack()
label_num = tk.Label(master=frm_titulo_num,
                     text="Número\t\t Ancho\t\t Espesor\t\t Alto")
label_num.pack()
frm_nums = tk.Frame(master=frm_form_41, width=200, height=100, borderwidth=3)
frm_nums.pack(side=tk.LEFT, padx=20, pady=10)
# Datos de anillos para juntas
lbl_an1 = tk.Label(master=frm_nums, text="Anillo n1")
ent_an1 = tk.Entry(master=frm_nums, width=10)
ent_aw1 = tk.Entry(master=frm_nums, width=10)
unt_aw1 = tk.Label(master=frm_nums, text="cm")
ent_et1 = tk.Entry(master=frm_nums, width=10)
unt_et1 = tk.Label(master=frm_nums, text="cm")
ent_alto1 = tk.Entry(master=frm_nums, width=10)
unt_alto1 = tk.Label(master=frm_nums, text="cm")
lbl_an1.grid(row=0, column=0, sticky="e")
ent_an1.grid(row=0, column=1)
ent_aw1.grid(row=0, column=2)
unt_aw1.grid(row=0, column=3)
ent_et1.grid(row=0, column=4)
unt_et1.grid(row=0, column=5)
ent_alto1.grid(row=0, column=6)
unt_alto1.grid(row=0, column=7)

lbl_an2 = tk.Label(master=frm_nums, text="Anillo n2")
ent_an2 = tk.Entry(master=frm_nums, width=10)
ent_aw2 = tk.Entry(master=frm_nums, width=10)
unt_aw2 = tk.Label(master=frm_nums, text="cm")
ent_et2 = tk.Entry(master=frm_nums, width=10)
unt_et2 = tk.Label(master=frm_nums, text="cm")
ent_alto2 = tk.Entry(master=frm_nums, width=10)
unt_alto2 = tk.Label(master=frm_nums, text="cm")
lbl_an2.grid(row=1, column=0, sticky="e")
ent_an2.grid(row=1, column=1)
ent_aw2.grid(row=1, column=2)
unt_aw2.grid(row=1, column=3)
ent_et2.grid(row=1, column=4)
unt_et2.grid(row=1, column=5)
ent_alto2.grid(row=1, column=6)
unt_alto2.grid(row=1, column=7)

lbl_an3 = tk.Label(master=frm_nums, text="Anillo n3")
ent_an3 = tk.Entry(master=frm_nums, width=10)
ent_aw3 = tk.Entry(master=frm_nums, width=10)
unt_aw3 = tk.Label(master=frm_nums, text="cm")
ent_et3 = tk.Entry(master=frm_nums, width=10)
unt_et3 = tk.Label(master=frm_nums, text="cm")
ent_alto3 = tk.Entry(master=frm_nums, width=10)
unt_alto3 = tk.Label(master=frm_nums, text="cm")
lbl_an3.grid(row=2, column=0, sticky="e")
ent_an3.grid(row=2, column=1)
ent_aw3.grid(row=2, column=2)
unt_aw3.grid(row=2, column=3)
ent_et3.grid(row=2, column=4)
unt_et3.grid(row=2, column=5)
ent_alto3.grid(row=2, column=6)
unt_alto3.grid(row=2, column=7)

lbl_an4 = tk.Label(master=frm_nums, text="Anillo n4")
ent_an4 = tk.Entry(master=frm_nums, width=10)
ent_aw4 = tk.Entry(master=frm_nums, width=10)
unt_aw4 = tk.Label(master=frm_nums, text="cm")
ent_et4 = tk.Entry(master=frm_nums, width=10)
unt_et4 = tk.Label(master=frm_nums, text="cm")
ent_alto4 = tk.Entry(master=frm_nums, width=10)
unt_alto4 = tk.Label(master=frm_nums, text="cm")
lbl_an4.grid(row=3, column=0, sticky="e")
ent_an4.grid(row=3, column=1)
ent_aw4.grid(row=3, column=2)
unt_aw4.grid(row=3, column=3)
ent_et4.grid(row=3, column=4)
unt_et4.grid(row=3, column=5)
ent_alto4.grid(row=3, column=6)
unt_alto4.grid(row=3, column=7)

lbl_an5 = tk.Label(master=frm_nums, text="Anillo n5")
ent_an5 = tk.Entry(master=frm_nums, width=10)
ent_aw5 = tk.Entry(master=frm_nums, width=10)
unt_aw5 = tk.Label(master=frm_nums, text="cm")
ent_et5 = tk.Entry(master=frm_nums, width=10)
unt_et5 = tk.Label(master=frm_nums, text="cm")
ent_alto5 = tk.Entry(master=frm_nums, width=10)
unt_alto5 = tk.Label(master=frm_nums, text="cm")
lbl_an5.grid(row=4, column=0, sticky="e")
ent_an5.grid(row=4, column=1)
ent_aw5.grid(row=4, column=2)
unt_aw5.grid(row=4, column=3)
ent_et5.grid(row=4, column=4)
unt_et5.grid(row=4, column=5)
ent_alto5.grid(row=4, column=6)
unt_alto5.grid(row=4, column=7)

lbl_an6 = tk.Label(master=frm_nums, text="Anillo n6")
ent_an6 = tk.Entry(master=frm_nums, width=10)
ent_aw6 = tk.Entry(master=frm_nums, width=10)
unt_aw6 = tk.Label(master=frm_nums, text="cm")
ent_et6 = tk.Entry(master=frm_nums, width=10)
unt_et6 = tk.Label(master=frm_nums, text="cm")
ent_alto6 = tk.Entry(master=frm_nums, width=10)
unt_alto6 = tk.Label(master=frm_nums, text="cm")
lbl_an6.grid(row=5, column=0, sticky="e")
ent_an6.grid(row=5, column=1)
ent_aw6.grid(row=5, column=2)
unt_aw6.grid(row=5, column=3)
ent_et6.grid(row=5, column=4)
unt_et6.grid(row=5, column=5)
ent_alto6.grid(row=5, column=6)
unt_alto6.grid(row=5, column=7)

lbl_an7 = tk.Label(master=frm_nums, text="Anillo n7")
ent_an7 = tk.Entry(master=frm_nums, width=10)
ent_aw7 = tk.Entry(master=frm_nums, width=10)
unt_aw7 = tk.Label(master=frm_nums, text="cm")
ent_et7 = tk.Entry(master=frm_nums, width=10)
unt_et7 = tk.Label(master=frm_nums, text="cm")
ent_alto7 = tk.Entry(master=frm_nums, width=10)
unt_alto7 = tk.Label(master=frm_nums, text="cm")
lbl_an7.grid(row=6, column=0, sticky="e")
ent_an7.grid(row=6, column=1)
ent_aw7.grid(row=6, column=2)
unt_aw7.grid(row=6, column=3)
ent_et7.grid(row=6, column=4)
unt_et7.grid(row=6, column=5)
ent_alto7.grid(row=6, column=6)
unt_alto7.grid(row=6, column=7)

lbl_an8 = tk.Label(master=frm_nums, text="Anillo n8")
ent_an8 = tk.Entry(master=frm_nums, width=10)
ent_aw8 = tk.Entry(master=frm_nums, width=10)
unt_aw8 = tk.Label(master=frm_nums, text="cm")
ent_et8 = tk.Entry(master=frm_nums, width=10)
unt_et8 = tk.Label(master=frm_nums, text="cm")
ent_alto8 = tk.Entry(master=frm_nums, width=10)
unt_alto8 = tk.Label(master=frm_nums, text="cm")
lbl_an8.grid(row=7, column=0, sticky="e")
ent_an8.grid(row=7, column=1)
ent_aw8.grid(row=7, column=2)
unt_aw8.grid(row=7, column=3)
ent_et8.grid(row=7, column=4)
unt_et8.grid(row=7, column=5)
ent_alto8.grid(row=7, column=6)
unt_alto8.grid(row=7, column=7)

lbl_an9 = tk.Label(master=frm_nums, text="Anillo n9")
ent_an9 = tk.Entry(master=frm_nums, width=10)
ent_aw9 = tk.Entry(master=frm_nums, width=10)
unt_aw9 = tk.Label(master=frm_nums, text="cm")
ent_et9 = tk.Entry(master=frm_nums, width=10)
unt_et9 = tk.Label(master=frm_nums, text="cm")
ent_alto9 = tk.Entry(master=frm_nums, width=10)
unt_alto9 = tk.Label(master=frm_nums, text="cm")
lbl_an9.grid(row=8, column=0, sticky="e")
ent_an9.grid(row=8, column=1)
ent_aw9.grid(row=8, column=2)
unt_aw9.grid(row=8, column=3)
ent_et9.grid(row=8, column=4)
unt_et9.grid(row=8, column=5)
ent_alto9.grid(row=8, column=6)
unt_alto9.grid(row=8, column=7)

lbl_an10 = tk.Label(master=frm_nums, text="Anillo n10")
ent_an10 = tk.Entry(master=frm_nums, width=10)
ent_aw10 = tk.Entry(master=frm_nums, width=10)
unt_aw10 = tk.Label(master=frm_nums, text="cm")
ent_et10 = tk.Entry(master=frm_nums, width=10)
unt_et10 = tk.Label(master=frm_nums, text="cm")
ent_alto10 = tk.Entry(master=frm_nums, width=10)
unt_alto10 = tk.Label(master=frm_nums, text="cm")
lbl_an10.grid(row=9, column=0, sticky="e")
ent_an10.grid(row=9, column=1)
ent_aw10.grid(row=9, column=2)
unt_aw10.grid(row=9, column=3)
ent_et10.grid(row=9, column=4)
unt_et10.grid(row=9, column=5)
ent_alto10.grid(row=9, column=6)
unt_alto10.grid(row=9, column=7)

# Datos de volumen muerto
frame_vm = tk.Frame(master=p5, width=100, height=100, borderwidth=3)
frame_vm.pack(padx=20, pady=10)
label_vm = tk.Label(master=frame_vm, text="Datos de volumen muerto")
label_vm.pack()
label_num_acc = tk.Label(master=frame_vm, text="Numero de accesorios")
label_num_acc.pack()
entry_num = tk.Entry(master=frame_vm, width=10)
entry_num.pack()
# Desde frame
frm_form_5 = tk.Frame(master=p5, relief=tk.GROOVE,
                      width=200, height=100, borderwidth=3)
frm_form_5.pack(side=tk.LEFT, padx=20, pady=10)
frm_titulo_desde = tk.Frame(master=frm_form_5, borderwidth=3)
frm_titulo_desde.pack()
label_desde = tk.Label(master=frm_titulo_desde, text="Desde")
label_desde.pack()
frm_desde = tk.Frame(master=frm_form_5, width=200, height=100, borderwidth=3)
frm_desde.pack(side=tk.LEFT, padx=20, pady=10)
# Datos accesorios desde
lbl_acca1 = tk.Label(master=frm_desde, text="Accesorio a1")
ent_acca1 = tk.Entry(master=frm_desde, width=10)
unt_acca1 = tk.Label(master=frm_desde, text="cm")
lbl_acca1.grid(row=0, column=0, sticky="e")
ent_acca1.grid(row=0, column=1)
unt_acca1.grid(row=0, column=2)

lbl_acca2 = tk.Label(master=frm_desde, text="Accesorio a2")
ent_acca2 = tk.Entry(master=frm_desde, width=10)
unt_acca2 = tk.Label(master=frm_desde, text="cm")
lbl_acca2.grid(row=1, column=0, sticky="e")
ent_acca2.grid(row=1, column=1)
unt_acca2.grid(row=1, column=2)

lbl_acca3 = tk.Label(master=frm_desde, text="Accesorio a3")
ent_acca3 = tk.Entry(master=frm_desde, width=10)
unt_acca3 = tk.Label(master=frm_desde, text="cm")
lbl_acca3.grid(row=2, column=0, sticky="e")
ent_acca3.grid(row=2, column=1)
unt_acca3.grid(row=2, column=2)

lbl_acca4 = tk.Label(master=frm_desde, text="Accesorio a4")
ent_acca4 = tk.Entry(master=frm_desde, width=10)
unt_acca4 = tk.Label(master=frm_desde, text="cm")
lbl_acca4.grid(row=3, column=0, sticky="e")
ent_acca4.grid(row=3, column=1)
unt_acca4.grid(row=3, column=2)

lbl_acca5 = tk.Label(master=frm_desde, text="Accesorio a5")
ent_acca5 = tk.Entry(master=frm_desde, width=10)
unt_acca5 = tk.Label(master=frm_desde, text="cm")
lbl_acca5.grid(row=4, column=0, sticky="e")
ent_acca5.grid(row=4, column=1)
unt_acca5.grid(row=4, column=2)

lbl_acca6 = tk.Label(master=frm_desde, text="Accesorio a6")
ent_acca6 = tk.Entry(master=frm_desde, width=10)
unt_acca6 = tk.Label(master=frm_desde, text="cm")
lbl_acca6.grid(row=5, column=0, sticky="e")
ent_acca6.grid(row=5, column=1)
unt_acca6.grid(row=5, column=2)

lbl_acca7 = tk.Label(master=frm_desde, text="Accesorio a7")
ent_acca7 = tk.Entry(master=frm_desde, width=10)
unt_acca7 = tk.Label(master=frm_desde, text="cm")
lbl_acca7.grid(row=6, column=0, sticky="e")
ent_acca7.grid(row=6, column=1)
unt_acca7.grid(row=6, column=2)

lbl_acca8 = tk.Label(master=frm_desde, text="Accesorio a8")
ent_acca8 = tk.Entry(master=frm_desde, width=10)
unt_acca8 = tk.Label(master=frm_desde, text="cm")
lbl_acca8.grid(row=7, column=0, sticky="e")
ent_acca8.grid(row=7, column=1)
unt_acca8.grid(row=7, column=2)

lbl_acca9 = tk.Label(master=frm_desde, text="Accesorio a9")
ent_acca9 = tk.Entry(master=frm_desde, width=10)
unt_acca9 = tk.Label(master=frm_desde, text="cm")
lbl_acca9.grid(row=8, column=0, sticky="e")
ent_acca9.grid(row=8, column=1)
unt_acca9.grid(row=8, column=2)

lbl_acca10 = tk.Label(master=frm_desde, text="Accesorio a10")
ent_acca10 = tk.Entry(master=frm_desde, width=10)
unt_acca10 = tk.Label(master=frm_desde, text="cm")
lbl_acca10.grid(row=9, column=0, sticky="e")
ent_acca10.grid(row=9, column=1)
unt_acca10.grid(row=9, column=2)

# Hasta frame
frm_form_52 = tk.Frame(master=p5, relief=tk.GROOVE,
                       width=200, height=100, borderwidth=3)
frm_form_52.pack(side=tk.LEFT, padx=20, pady=10)
frm_titulo_hasta = tk.Frame(master=frm_form_52, borderwidth=3)
frm_titulo_hasta.pack()
label_hasta = tk.Label(master=frm_titulo_hasta, text="Hasta")
label_hasta.pack()
frm_hasta = tk.Frame(master=frm_form_52, width=200, height=100, borderwidth=3)
frm_hasta.pack(side=tk.LEFT, padx=20, pady=10)
# Datos accesorios hasta
ent_acha1 = tk.Entry(master=frm_hasta, width=10)
unt_acha1 = tk.Label(master=frm_hasta, text="cm")
ent_acha1.grid(row=0, column=1)
unt_acha1.grid(row=0, column=2)

ent_acha2 = tk.Entry(master=frm_hasta, width=10)
unt_acha2 = tk.Label(master=frm_hasta, text="cm")
ent_acha2.grid(row=1, column=1)
unt_acha2.grid(row=1, column=2)

ent_acha3 = tk.Entry(master=frm_hasta, width=10)
unt_acha3 = tk.Label(master=frm_hasta, text="cm")
ent_acha3.grid(row=2, column=1)
unt_acha3.grid(row=2, column=2)

ent_acha4 = tk.Entry(master=frm_hasta, width=10)
unt_acha4 = tk.Label(master=frm_hasta, text="cm")
ent_acha4.grid(row=3, column=1)
unt_acha4.grid(row=3, column=2)

ent_acha5 = tk.Entry(master=frm_hasta, width=10)
unt_acha5 = tk.Label(master=frm_hasta, text="cm")
ent_acha5.grid(row=4, column=1)
unt_acha5.grid(row=4, column=2)

ent_acha6 = tk.Entry(master=frm_hasta, width=10)
unt_acha6 = tk.Label(master=frm_hasta, text="cm")
ent_acha6.grid(row=5, column=1)
unt_acha6.grid(row=5, column=2)

ent_acha7 = tk.Entry(master=frm_hasta, width=10)
unt_acha7 = tk.Label(master=frm_hasta, text="cm")
ent_acha7.grid(row=6, column=1)
unt_acha7.grid(row=6, column=2)

ent_acha8 = tk.Entry(master=frm_hasta, width=10)
unt_acha8 = tk.Label(master=frm_hasta, text="cm")
ent_acha8.grid(row=7, column=1)
unt_acha8.grid(row=7, column=2)

ent_acha9 = tk.Entry(master=frm_hasta, width=10)
unt_acha9 = tk.Label(master=frm_hasta, text="cm")
ent_acha9.grid(row=8, column=1)
unt_acha9.grid(row=8, column=2)

ent_acha10 = tk.Entry(master=frm_hasta, width=10)
unt_acha10 = tk.Label(master=frm_hasta, text="cm")
ent_acha10.grid(row=9, column=1)
unt_acha10.grid(row=9, column=2)

# Lit/cm frame
frm_form_vm = tk.Frame(master=p5, relief=tk.GROOVE,
                       width=200, height=100, borderwidth=3)
frm_form_vm.pack(side=tk.LEFT, padx=20, pady=10)
frm_titulo_vm = tk.Frame(master=frm_form_vm, borderwidth=3)
frm_titulo_vm.pack()
label_vm = tk.Label(master=frm_titulo_vm, text="Lit/cm")
label_vm.pack()
frm_vm = tk.Frame(master=frm_form_vm, width=200, height=100, borderwidth=3)
frm_vm.pack(side=tk.LEFT, padx=20, pady=10)
# Datos accesorios hasta
ent_vm1 = tk.Entry(master=frm_vm, width=10)
unt_vm1 = tk.Label(master=frm_vm, text="bbl")
ent_vm1.grid(row=0, column=1)
unt_vm1.grid(row=0, column=2)

ent_vm2 = tk.Entry(master=frm_vm, width=10)
unt_vm2 = tk.Label(master=frm_vm, text="bbl")
ent_vm2.grid(row=1, column=1)
unt_vm2.grid(row=1, column=2)

ent_vm3 = tk.Entry(master=frm_vm, width=10)
unt_vm3 = tk.Label(master=frm_vm, text="bbl")
ent_vm3.grid(row=2, column=1)
unt_vm3.grid(row=2, column=2)

ent_vm4 = tk.Entry(master=frm_vm, width=10)
unt_vm4 = tk.Label(master=frm_vm, text="bbl")
ent_vm4.grid(row=3, column=1)
unt_vm4.grid(row=3, column=2)

ent_vm5 = tk.Entry(master=frm_vm, width=10)
unt_vm5 = tk.Label(master=frm_vm, text="bbl")
ent_vm5.grid(row=4, column=1)
unt_vm5.grid(row=4, column=2)

ent_vm6 = tk.Entry(master=frm_vm, width=10)
unt_vm6 = tk.Label(master=frm_vm, text="bbl")
ent_vm6.grid(row=5, column=1)
unt_vm6.grid(row=5, column=2)

ent_vm7 = tk.Entry(master=frm_vm, width=10)
unt_vm7 = tk.Label(master=frm_vm, text="bbl")
ent_vm7.grid(row=6, column=1)
unt_vm7.grid(row=6, column=2)

ent_vm8 = tk.Entry(master=frm_vm, width=10)
unt_vm8 = tk.Label(master=frm_vm, text="bbl")
ent_vm8.grid(row=7, column=1)
unt_vm8.grid(row=7, column=2)

ent_vm9 = tk.Entry(master=frm_vm, width=10)
unt_vm9 = tk.Label(master=frm_vm, text="bbl")
ent_vm9.grid(row=8, column=1)
unt_vm9.grid(row=8, column=2)
ent_vm10 = tk.Entry(master=frm_vm, width=10)
unt_vm10 = tk.Label(master=frm_vm, text="bbl")
ent_vm10.grid(row=9, column=1)
unt_vm10.grid(row=9, column=2)

# volumen muerto frame
frm_form_vmt = tk.Frame(master=p5, relief=tk.GROOVE,
                        width=200, height=100, borderwidth=3)
frm_form_vmt.pack(side=tk.LEFT, padx=20, pady=10)
frm_titulo_vmt = tk.Frame(master=frm_form_vmt, borderwidth=3)
frm_titulo_vmt.pack()
label_vmt = tk.Label(master=frm_titulo_vmt, text="Volumen")
label_vmt.pack()
frm_vmt = tk.Frame(master=frm_form_vmt, width=200, height=100, borderwidth=3)
frm_vmt.pack(side=tk.LEFT, padx=20, pady=10)
# Datos accesorios v muerto
lbl_vm1 = tk.Label(master=frm_vmt)
lbl_vm1.grid(row=0, column=1)

lbl_vm2 = tk.Label(master=frm_vmt)
lbl_vm2.grid(row=1, column=1)

lbl_vm3 = tk.Label(master=frm_vmt)
lbl_vm3.grid(row=2, column=1)

lbl_vm4 = tk.Label(master=frm_vmt)
lbl_vm4.grid(row=3, column=1)

lbl_vm5 = tk.Label(master=frm_vmt)
lbl_vm5.grid(row=4, column=1)

lbl_vm6 = tk.Label(master=frm_vmt)
lbl_vm6.grid(row=5, column=1)

lbl_vm7 = tk.Label(master=frm_vmt)
lbl_vm7.grid(row=6, column=1)

lbl_vm8 = tk.Label(master=frm_vmt)
lbl_vm8.grid(row=7, column=1)

lbl_vm9 = tk.Label(master=frm_vmt)
lbl_vm9.grid(row=8, column=1)

lbl_vm10 = tk.Label(master=frm_vmt)
lbl_vm10.grid(row=9, column=1)

# calculo de volumen muerto


def vmuerto():
    desde1 = float(ent_acca1.get())
    hasta1 = float(ent_acha1.get())
    lit1 = float(ent_vm1.get())
    lbl_vm1["text"] = f"{(lit1)*(hasta1-desde1):.3f}" + " litros"
    desde2 = float(ent_acca2.get())
    hasta2 = float(ent_acha2.get())
    lit2 = float(ent_vm2.get())
    lbl_vm2["text"] = f"{(lit2)*(hasta2-desde2):.3f}" + " litros"
    desde3 = float(ent_acca3.get())
    hasta3 = float(ent_acha3.get())
    lit3 = float(ent_vm3.get())
    lbl_vm3["text"] = f"{(lit3)*(hasta3-desde3):.3f}" + " litros"
    desde4 = float(ent_acca4.get())
    hasta4 = float(ent_acha4.get())
    lit4 = float(ent_vm4.get())
    lbl_vm4["text"] = f"{(lit4)*(hasta4-desde4):.3f}" + " litros"
    desde5 = float(ent_acca5.get())
    hasta5 = float(ent_acha5.get())
    lit5 = float(ent_vm5.get())
    lbl_vm5["text"] = f"{(lit5)*(hasta5-desde5):.3f}" + " litros"
    desde6 = float(ent_acca6.get())
    hasta6 = float(ent_acha6.get())
    lit6 = float(ent_vm6.get())
    lbl_vm6["text"] = f"{(lit6)*(hasta6-desde6):.3f}" + " litros"
    desde7 = float(ent_acca7.get())
    hasta7 = float(ent_acha7.get())
    lit7 = float(ent_vm7.get())
    lbl_vm7["text"] = f"{(lit7)*(hasta7-desde7):.3f}" + " litros"
    desde8 = float(ent_acca8.get())
    hasta8 = float(ent_acha8.get())
    lit8 = float(ent_vm8.get())
    lbl_vm8["text"] = f"{(lit8)*(hasta8-desde8):.3f}" + " litros"
    desde9 = float(ent_acca9.get())
    hasta9 = float(ent_acha9.get())
    lit9 = float(ent_vm9.get())
    lbl_vm9["text"] = f"{(lit9)*(hasta9-desde9):.3f}" + " litros"
    desde10 = float(ent_acca10.get())
    hasta10 = float(ent_acha10.get())
    lit10 = float(ent_vm10.get())
    lbl_vm10["text"] = f"{(lit10)*(hasta10-desde10):.3f}" + " litros"

    # Manhole
    cir_manhole = float(ent_circ_manhole.get())
    long_manhole = float(ent_lon_manhole.get())
    espesor_manhole = float(ent_esp_manhole.get())
    dia_int = (cir_manhole/3.141592)-2*espesor_manhole
    lbl_result_dia_int["text"] = f"{dia_int :.5f}" + " cm"
    total_vol = math.pow(dia_int, 2) * 3.141592*long_manhole*1000/4
    lbl_result_total_vol["text"] = f"{total_vol:.5f}" + " cm"
    lt_cm = total_vol/(dia_int*100)
    lbl_result_lt_cm["text"] = f"{lt_cm:.5f}" + " cm"


# Correciones para la circunferencia
frm_form_corr = tk.Frame(master=p6, relief=tk.GROOVE,
                         width=200, height=100, borderwidth=3)
frm_form_corr.pack(padx=2, pady=10)
frm_titulo_corr = tk.Frame(master=frm_form_corr, borderwidth=3)
frm_titulo_corr.pack()
label_corr = tk.Label(master=frm_titulo_corr,
                      text="CORRECCIONES PARA LA CIRCUNFERENCIA")
label_corr.pack()
frm_corr = tk.Frame(master=frm_form_corr, width=200, height=100, borderwidth=3)
frm_corr.pack(padx=20, pady=10, fill=tk.X)
# Labels para correcciones para la circunferencia
lbl_anillo = tk.Label(master=frm_corr, text="Circunferencia")
lbl_anillo.grid(row=0, column=0)
lbl_n1 = tk.Label(master=frm_corr, text="1")
lbl_n1.grid(row=1, column=0)
lbl_n2 = tk.Label(master=frm_corr, text="2")
lbl_n2.grid(row=2, column=0)
lbl_n3 = tk.Label(master=frm_corr, text="3")
lbl_n3.grid(row=3, column=0)
lbl_n4 = tk.Label(master=frm_corr, text="4")
lbl_n4.grid(row=4, column=0)
lbl_n5 = tk.Label(master=frm_corr, text="5")
lbl_n5.grid(row=5, column=0)
lbl_n6 = tk.Label(master=frm_corr, text="6")
lbl_n6.grid(row=6, column=0)
lbl_n7 = tk.Label(master=frm_corr, text="7")
lbl_n7.grid(row=7, column=0)
lbl_n8 = tk.Label(master=frm_corr, text="8")
lbl_n8.grid(row=8, column=0)
lbl_n9 = tk.Label(master=frm_corr, text="9")
lbl_n9.grid(row=9, column=0)
lbl_n10 = tk.Label(master=frm_corr, text="10")
lbl_n10.grid(row=10, column=0)
lbl_cor_cal = tk.Label(master=frm_corr, text="Circunferencia\n exterior\n(cm)")
lbl_cor_cal.grid(row=0, column=1)
lbl_elv_cinta = tk.Label(master=frm_corr, text="Correción\n Cinta\n(cm)")
lbl_elv_cinta.grid(row=0, column=2)
lbl_base_tanque = tk.Label(master=frm_corr, text="Correción\n Espesor\n(cm)")
lbl_base_tanque.grid(row=0, column=3)
lbl_cir_ext = tk.Label(master=frm_corr, text="Correción\n Tape Rise\n(cm)")
lbl_cir_ext.grid(row=0, column=4)
lbl_cor_cir = tk.Label(master=frm_corr, text="Correción\n a TQ Vacio\n (cm)")
lbl_cor_cir.grid(row=0, column=5)
lbl_cor_max = tk.Label(master=frm_corr, text="Circunferencia\n interna\n (cm)")
lbl_cor_max.grid(row=0, column=6)
lbl_cir_int_max = tk.Label(
    master=frm_corr, text="Correción\n de presion\n (cm)")
lbl_cir_int_max.grid(row=0, column=7)
lbl_cir_int_max_ef = tk.Label(
    master=frm_corr, text="Circunferencia\n Stressed\n (cm)")
lbl_cir_int_max_ef.grid(row=0, column=8)

# RESULTADOS: circunferencia exterior
lbl_result_corr_cal1 = tk.Label(master=frm_corr)
lbl_result_corr_cal1.grid(row=1, column=1)
lbl_result_corr_cal2 = tk.Label(master=frm_corr)
lbl_result_corr_cal2.grid(row=2, column=1)
lbl_result_corr_cal3 = tk.Label(master=frm_corr)
lbl_result_corr_cal3.grid(row=3, column=1)
lbl_result_corr_cal4 = tk.Label(master=frm_corr)
lbl_result_corr_cal4.grid(row=4, column=1)
lbl_result_corr_cal5 = tk.Label(master=frm_corr)
lbl_result_corr_cal5.grid(row=5, column=1)
lbl_result_corr_cal6 = tk.Label(master=frm_corr)
lbl_result_corr_cal6.grid(row=6, column=1)
lbl_result_corr_cal7 = tk.Label(master=frm_corr)
lbl_result_corr_cal7.grid(row=7, column=1)
lbl_result_corr_cal8 = tk.Label(master=frm_corr)
lbl_result_corr_cal8.grid(row=8, column=1)
lbl_result_corr_cal9 = tk.Label(master=frm_corr)
lbl_result_corr_cal9.grid(row=9, column=1)
lbl_result_corr_cal10 = tk.Label(master=frm_corr)
lbl_result_corr_cal10.grid(row=10, column=1)

# RESULTADOS: correcciones para elevacion de la cinta
lbl_result_elv_cinta1 = tk.Label(master=frm_corr, text=0)
lbl_result_elv_cinta1.grid(row=1, column=2)
lbl_result_elv_cinta2 = tk.Label(master=frm_corr, text=0)
lbl_result_elv_cinta2.grid(row=2, column=2)
lbl_result_elv_cinta3 = tk.Label(master=frm_corr, text=0)
lbl_result_elv_cinta3.grid(row=3, column=2)
lbl_result_elv_cinta4 = tk.Label(master=frm_corr, text=0)
lbl_result_elv_cinta4.grid(row=4, column=2)
lbl_result_elv_cinta5 = tk.Label(master=frm_corr, text=0)
lbl_result_elv_cinta5.grid(row=5, column=2)
lbl_result_elv_cinta6 = tk.Label(master=frm_corr, text=0)
lbl_result_elv_cinta6.grid(row=6, column=2)
lbl_result_elv_cinta7 = tk.Label(master=frm_corr, text=0)
lbl_result_elv_cinta7.grid(row=7, column=2)
lbl_result_elv_cinta8 = tk.Label(master=frm_corr, text=0)
lbl_result_elv_cinta8.grid(row=8, column=2)
lbl_result_elv_cinta9 = tk.Label(master=frm_corr, text=0)
lbl_result_elv_cinta9.grid(row=9, column=2)
lbl_result_elv_cinta10 = tk.Label(master=frm_corr, text=0)
lbl_result_elv_cinta10.grid(row=10, column=2)

# RESULTADOS: correcciones espesor
lbl_result_base1 = tk.Label(master=frm_corr)
lbl_result_base1.grid(row=1, column=3)
lbl_result_base2 = tk.Label(master=frm_corr)
lbl_result_base2.grid(row=2, column=3)
lbl_result_base3 = tk.Label(master=frm_corr)
lbl_result_base3.grid(row=3, column=3)
lbl_result_base4 = tk.Label(master=frm_corr)
lbl_result_base4.grid(row=4, column=3)
lbl_result_base5 = tk.Label(master=frm_corr)
lbl_result_base5.grid(row=5, column=3)
lbl_result_base6 = tk.Label(master=frm_corr)
lbl_result_base6.grid(row=6, column=3)
lbl_result_base7 = tk.Label(master=frm_corr)
lbl_result_base7.grid(row=7, column=3)
lbl_result_base8 = tk.Label(master=frm_corr)
lbl_result_base8.grid(row=8, column=3)
lbl_result_base9 = tk.Label(master=frm_corr)
lbl_result_base9.grid(row=9, column=3)
lbl_result_base10 = tk.Label(master=frm_corr)
lbl_result_base10.grid(row=10, column=3)

# RESULTADOS: correcciones tope a rise
lbl_result_ext_int1 = tk.Label(master=frm_corr)
lbl_result_ext_int1.grid(row=1, column=4)
lbl_result_ext_int2 = tk.Label(master=frm_corr)
lbl_result_ext_int2.grid(row=2, column=4)
lbl_result_ext_int3 = tk.Label(master=frm_corr)
lbl_result_ext_int3.grid(row=3, column=4)
lbl_result_ext_int4 = tk.Label(master=frm_corr)
lbl_result_ext_int4.grid(row=4, column=4)
lbl_result_ext_int5 = tk.Label(master=frm_corr)
lbl_result_ext_int5.grid(row=5, column=4)
lbl_result_ext_int6 = tk.Label(master=frm_corr)
lbl_result_ext_int6.grid(row=6, column=4)
lbl_result_ext_int7 = tk.Label(master=frm_corr)
lbl_result_ext_int7.grid(row=7, column=4)
lbl_result_ext_int8 = tk.Label(master=frm_corr)
lbl_result_ext_int8.grid(row=8, column=4)
lbl_result_ext_int9 = tk.Label(master=frm_corr)
lbl_result_ext_int9.grid(row=9, column=4)
lbl_result_ext_int10 = tk.Label(master=frm_corr)
lbl_result_ext_int10.grid(row=10, column=4)

# RESULTADOS: correcciones para base tanque vacio
lbl_result_cor_int1 = tk.Label(master=frm_corr)
lbl_result_cor_int1.grid(row=1, column=5)
lbl_result_cor_int2 = tk.Label(master=frm_corr)
lbl_result_cor_int2.grid(row=2, column=5)
lbl_result_cor_int3 = tk.Label(master=frm_corr)
lbl_result_cor_int3.grid(row=3, column=5)
lbl_result_cor_int4 = tk.Label(master=frm_corr)
lbl_result_cor_int4.grid(row=4, column=5)
lbl_result_cor_int5 = tk.Label(master=frm_corr)
lbl_result_cor_int5.grid(row=5, column=5)
lbl_result_cor_int6 = tk.Label(master=frm_corr)
lbl_result_cor_int6.grid(row=6, column=5)
lbl_result_cor_int7 = tk.Label(master=frm_corr)
lbl_result_cor_int7.grid(row=7, column=5)
lbl_result_cor_int8 = tk.Label(master=frm_corr)
lbl_result_cor_int8.grid(row=8, column=5)
lbl_result_cor_int9 = tk.Label(master=frm_corr)
lbl_result_cor_int9.grid(row=9, column=5)
lbl_result_cor_int10 = tk.Label(master=frm_corr)
lbl_result_cor_int10.grid(row=10, column=5)

# RESULTADOS: circunferencia interna
lbl_result_cor_max1 = tk.Label(master=frm_corr)
lbl_result_cor_max1.grid(row=1, column=6)
lbl_result_cor_max2 = tk.Label(master=frm_corr)
lbl_result_cor_max2.grid(row=2, column=6)
lbl_result_cor_max3 = tk.Label(master=frm_corr)
lbl_result_cor_max3.grid(row=3, column=6)
lbl_result_cor_max4 = tk.Label(master=frm_corr)
lbl_result_cor_max4.grid(row=4, column=6)
lbl_result_cor_max5 = tk.Label(master=frm_corr)
lbl_result_cor_max5.grid(row=5, column=6)
lbl_result_cor_max6 = tk.Label(master=frm_corr)
lbl_result_cor_max6.grid(row=6, column=6)
lbl_result_cor_max7 = tk.Label(master=frm_corr)
lbl_result_cor_max7.grid(row=7, column=6)
lbl_result_cor_max8 = tk.Label(master=frm_corr)
lbl_result_cor_max8.grid(row=8, column=6)
lbl_result_cor_max9 = tk.Label(master=frm_corr)
lbl_result_cor_max9.grid(row=9, column=6)
lbl_result_cor_max10 = tk.Label(master=frm_corr)
lbl_result_cor_max10.grid(row=10, column=6)

# RESULTADOS: correcciones de presion
lbl_result_cir_int_ft1 = tk.Label(master=frm_corr)
lbl_result_cir_int_ft1.grid(row=1, column=7)
lbl_result_cir_int_ft2 = tk.Label(master=frm_corr)
lbl_result_cir_int_ft2.grid(row=2, column=7)
lbl_result_cir_int_ft3 = tk.Label(master=frm_corr)
lbl_result_cir_int_ft3.grid(row=3, column=7)
lbl_result_cir_int_ft4 = tk.Label(master=frm_corr)
lbl_result_cir_int_ft4.grid(row=4, column=7)
lbl_result_cir_int_ft5 = tk.Label(master=frm_corr)
lbl_result_cir_int_ft5.grid(row=5, column=7)
lbl_result_cir_int_ft6 = tk.Label(master=frm_corr)
lbl_result_cir_int_ft6.grid(row=6, column=7)
lbl_result_cir_int_ft7 = tk.Label(master=frm_corr)
lbl_result_cir_int_ft7.grid(row=7, column=7)
lbl_result_cir_int_ft8 = tk.Label(master=frm_corr)
lbl_result_cir_int_ft8.grid(row=8, column=7)
lbl_result_cir_int_ft9 = tk.Label(master=frm_corr)
lbl_result_cir_int_ft9.grid(row=9, column=7)
lbl_result_cir_int_ft10 = tk.Label(master=frm_corr)
lbl_result_cir_int_ft10.grid(row=10, column=7)

# RESULTADOS: correcciones para circunferencia stressed
lbl_result_cir_int_in1 = tk.Label(master=frm_corr)
lbl_result_cir_int_in1.grid(row=1, column=8)
lbl_result_cir_int_in2 = tk.Label(master=frm_corr)
lbl_result_cir_int_in2.grid(row=2, column=8)
lbl_result_cir_int_in3 = tk.Label(master=frm_corr)
lbl_result_cir_int_in3.grid(row=3, column=8)
lbl_result_cir_int_in4 = tk.Label(master=frm_corr)
lbl_result_cir_int_in4.grid(row=4, column=8)
lbl_result_cir_int_in5 = tk.Label(master=frm_corr)
lbl_result_cir_int_in5.grid(row=5, column=8)
lbl_result_cir_int_in6 = tk.Label(master=frm_corr)
lbl_result_cir_int_in6.grid(row=6, column=8)
lbl_result_cir_int_in7 = tk.Label(master=frm_corr)
lbl_result_cir_int_in7.grid(row=7, column=8)
lbl_result_cir_int_in8 = tk.Label(master=frm_corr)
lbl_result_cir_int_in8.grid(row=8, column=8)
lbl_result_cir_int_in9 = tk.Label(master=frm_corr)
lbl_result_cir_int_in9.grid(row=9, column=8)
lbl_result_cir_int_in10 = tk.Label(master=frm_corr)
lbl_result_cir_int_in10.grid(row=10, column=8)

# Funciones para correcion por calibracion


def corTapeRise(diametro_ext_prom, n, alt, ach):
    return (2*n*alt*ach/diametro_ext_prom)+((8*n*alt/3)*math.sqrt(alt/diametro_ext_prom))


def corTanquevacio(circunferencia, corr_cinta, espesor, h1):  # lbl_result_elv_cinta
    k = 62.3/(288*30.48*3.141592*29000000)  # factor de correcion
    prod_tnq = float(ent_prd.get())
    alt_lq = float(ent_altura_liquido.get())
    corr_cinta = float(corr_cinta["text"])
    value = k*prod_tnq*(alt_lq-h1)*((circunferencia-corr_cinta**(2)/espesor))
    if value > 0:
        return value
    else:
        return 0


def cirInt(circunferencia, corr_cinta, corr_esp, corr_tope, cor_tq):
    corr_cinta = float(corr_cinta["text"])
    corr_esp = float(corr_esp["text"])
    corr_tope = float(corr_tope["text"])
    cor_tq = float(cor_tq["text"])
    return circunferencia - corr_cinta - corr_esp - corr_tope - cor_tq


def corrPresion(altura, circunferencia, espesor):  # result_ce_a1
    k = 62.3/(288*30.48*3.141592*29000000)  # factor de correcion
    ge_estacionaria = float(ent_est.get())
    altura = float(altura["text"].split(" ")[0])
    circunferencia = float(circunferencia["text"])
    return k*ge_estacionaria*altura*(circunferencia**(2))/espesor


def stressed(circunferencia, cor_presion):
    circunferencia = float(circunferencia["text"])
    cor_presion = float(cor_presion["text"])
    return circunferencia+cor_presion


def corrCalibracion():
    c1 = float(ent_ce_a1.get())
    lbl_result_corr_cal1["text"] = f"{c1:.3f}"
    c2 = float(ent_ce_a2.get())
    lbl_result_corr_cal2["text"] = f"{c2:.3f}"
    c3 = float(ent_ce_a3.get())
    lbl_result_corr_cal3["text"] = f"{c3:.3f}"
    c4 = float(ent_ce_a4.get())
    lbl_result_corr_cal4["text"] = f"{c4:.3f}"
    c5 = float(ent_ce_a5.get())
    lbl_result_corr_cal5["text"] = f"{c5:.3f}"
    c6 = float(ent_ce_a6.get())
    lbl_result_corr_cal6["text"] = f"{c6:.3f}"
    c7 = float(ent_ce_a7.get())
    lbl_result_corr_cal7["text"] = f"{c7:.3f}"
    c8 = float(ent_ce_a8.get())
    lbl_result_corr_cal8["text"] = f"{c8:.3f}"
    c9 = float(ent_ce_a9.get())
    lbl_result_corr_cal9["text"] = f"{c9:.3f}"
    c10 = float(ent_ce_a10.get())
    lbl_result_corr_cal10["text"] = f"{c10:.3f}"

    e1 = float(ent_et1.get())
    lbl_result_base1["text"] = f"{e1*2*3.141592:.3f}"
    e2 = float(ent_et2.get())
    lbl_result_base2["text"] = f"{e2*2*3.141592:.3f}"
    e3 = float(ent_et3.get())
    lbl_result_base3["text"] = f"{e3*2*3.141592:.3f}"
    e4 = float(ent_et4.get())
    lbl_result_base4["text"] = f"{e4*2*3.141592:.3f}"
    e5 = float(ent_et5.get())
    lbl_result_base5["text"] = f"{e5*2*3.141592:.3f}"
    e6 = float(ent_et6.get())
    lbl_result_base6["text"] = f"{e6*2*3.141592:.3f}"
    e7 = float(ent_et7.get())
    lbl_result_base7["text"] = f"{e7*2*3.141592:.3f}"
    e8 = float(ent_et8.get())
    lbl_result_base8["text"] = f"{e8*2*3.141592:.3f}"
    e9 = float(ent_et9.get())
    lbl_result_base9["text"] = f"{e9*2*3.141592:.3f}"
    e10 = float(ent_et10.get())
    lbl_result_base10["text"] = f"{e10*2*3.141592:.3f}"
    diametro_ext_prom = ((c1+c2+c3+c4+c5+c6+c7+c8+c9+c10)/10)/3.141592

    # Correcion tope a rise
    n1 = float(ent_an1.get())  # numero de juntas
    alt1 = float(ent_alto1.get())  # alto del cordon
    ach1 = float(ent_aw1.get())  # ancho del cordon
    # "{0:.3f}".format(5.1234554321)
    lbl_result_ext_int1["text"] = f"{corTapeRise(diametro_ext_prom,n1,alt1,ach1):.3f}"
    n2 = float(ent_an2.get())
    alt2 = float(ent_alto2.get())
    ach2 = float(ent_aw2.get())
    lbl_result_ext_int2["text"] = f"{corTapeRise(diametro_ext_prom,n2,alt2,ach2):.3f}"
    n3 = float(ent_an3.get())
    alt3 = float(ent_alto3.get())
    ach3 = float(ent_aw3.get())
    lbl_result_ext_int3["text"] = f"{corTapeRise(diametro_ext_prom,n3,alt3,ach3):.3f}"
    n4 = float(ent_an4.get())
    alt4 = float(ent_alto4.get())
    ach4 = float(ent_aw4.get())
    lbl_result_ext_int4["text"] = f"{corTapeRise(diametro_ext_prom,n4,alt4,ach4):.3f}"
    n5 = float(ent_an5.get())
    alt5 = float(ent_alto5.get())
    ach5 = float(ent_aw5.get())
    lbl_result_ext_int5["text"] = f"{corTapeRise(diametro_ext_prom,n5,alt5,ach5):.3f}"
    n6 = float(ent_an6.get())
    alt6 = float(ent_alto6.get())
    ach6 = float(ent_aw6.get())
    lbl_result_ext_int6["text"] = f"{corTapeRise(diametro_ext_prom,n6,alt6,ach6):.3f}"
    n7 = float(ent_an7.get())
    alt7 = float(ent_alto7.get())
    ach7 = float(ent_aw7.get())
    lbl_result_ext_int7["text"] = f"{corTapeRise(diametro_ext_prom,n7,alt7,ach7):.3f}"
    n8 = float(ent_an8.get())
    alt8 = float(ent_alto8.get())
    ach8 = float(ent_aw8.get())
    lbl_result_ext_int8["text"] = f"{corTapeRise(diametro_ext_prom,n8,alt8,ach8):.3f}"
    n9 = float(ent_an9.get())
    alt9 = float(ent_alto9.get())
    ach9 = float(ent_aw9.get())
    lbl_result_ext_int9["text"] = f"{corTapeRise(diametro_ext_prom,n9,alt9,ach9):.3f}"
    n10 = float(ent_an10.get())
    alt10 = float(ent_alto10.get())
    ach10 = float(ent_aw10.get())
    lbl_result_ext_int10["text"] = f"{corTapeRise(diametro_ext_prom,n10,alt10,ach10):.3f}"

    # correcion tanque al vacio
    h1 = float(ent_da_a1.get())
    lbl_result_cor_int1["text"] = f"{corTanquevacio(c1,lbl_result_elv_cinta1,e1,h1):.3f}"
    h2 = float(ent_da_a2.get())
    lbl_result_cor_int2["text"] = f"{corTanquevacio(c2,lbl_result_elv_cinta2,e2,h2):.3f}"
    h3 = float(ent_da_a3.get())
    lbl_result_cor_int3["text"] = f"{corTanquevacio(c3,lbl_result_elv_cinta3,e3,h3):.3f}"
    h4 = float(ent_da_a4.get())
    lbl_result_cor_int4["text"] = f"{corTanquevacio(c4,lbl_result_elv_cinta4,e4,h4):.3f}"
    h5 = float(ent_da_a5.get())
    lbl_result_cor_int5["text"] = f"{corTanquevacio(c5,lbl_result_elv_cinta5,e5,h5):.3f}"
    h6 = float(ent_da_a6.get())
    lbl_result_cor_int6["text"] = f"{corTanquevacio(c6,lbl_result_elv_cinta6,e6,h6):.3f}"
    h7 = float(ent_da_a7.get())
    lbl_result_cor_int7["text"] = f"{corTanquevacio(c7,lbl_result_elv_cinta7,e7,h7):.3f}"
    h8 = float(ent_da_a8.get())
    lbl_result_cor_int8["text"] = f"{corTanquevacio(c8,lbl_result_elv_cinta8,e8,h8):.3f}"
    h9 = float(ent_da_a9.get())
    lbl_result_cor_int9["text"] = f"{corTanquevacio(c9,lbl_result_elv_cinta9,e9,h9):.3f}"
    h10 = float(ent_da_a10.get())
    lbl_result_cor_int10["text"] = f"{corTanquevacio(c10,lbl_result_elv_cinta10,e10,h10):.3f}"

    # Circunferencia interna
    lbl_result_cor_max1["text"] = f"{cirInt(c1,lbl_result_elv_cinta1,lbl_result_base1,lbl_result_ext_int1,lbl_result_cor_int1):.3f}"
    lbl_result_cor_max2["text"] = f"{cirInt(c2,lbl_result_elv_cinta2,lbl_result_base2,lbl_result_ext_int2,lbl_result_cor_int2):.3f}"
    lbl_result_cor_max3["text"] = f"{cirInt(c3,lbl_result_elv_cinta3,lbl_result_base3,lbl_result_ext_int3,lbl_result_cor_int3):.3f}"
    lbl_result_cor_max4["text"] = f"{cirInt(c4,lbl_result_elv_cinta4,lbl_result_base4,lbl_result_ext_int4,lbl_result_cor_int4):.3f}"
    lbl_result_cor_max5["text"] = f"{cirInt(c5,lbl_result_elv_cinta5,lbl_result_base5,lbl_result_ext_int5,lbl_result_cor_int5):.3f}"
    lbl_result_cor_max6["text"] = f"{cirInt(c6,lbl_result_elv_cinta6,lbl_result_base6,lbl_result_ext_int6,lbl_result_cor_int6):.3f}"
    lbl_result_cor_max7["text"] = f"{cirInt(c7,lbl_result_elv_cinta7,lbl_result_base7,lbl_result_ext_int7,lbl_result_cor_int7):.3f}"
    lbl_result_cor_max8["text"] = f"{cirInt(c8,lbl_result_elv_cinta8,lbl_result_base8,lbl_result_ext_int8,lbl_result_cor_int8):.3f}"
    lbl_result_cor_max9["text"] = f"{cirInt(c9,lbl_result_elv_cinta9,lbl_result_base9,lbl_result_ext_int9,lbl_result_cor_int9):.3f}"
    lbl_result_cor_max10["text"] = f"{cirInt(c10,lbl_result_elv_cinta10,lbl_result_base10,lbl_result_ext_int10,lbl_result_cor_int10):.3f}"

    # correcion de presion
    lbl_result_cir_int_ft1["text"] = f"{corrPresion(result_ce_a1,lbl_result_cor_max1,e1):.3f}"
    lbl_result_cir_int_ft2["text"] = f"{corrPresion(result_ce_a2,lbl_result_cor_max2,e2):.3f}"
    lbl_result_cir_int_ft3["text"] = f"{corrPresion(result_ce_a3,lbl_result_cor_max3,e3):.3f}"
    lbl_result_cir_int_ft4["text"] = f"{corrPresion(result_ce_a4,lbl_result_cor_max4,e4):.3f}"
    lbl_result_cir_int_ft5["text"] = f"{corrPresion(result_ce_a5,lbl_result_cor_max5,e5):.3f}"
    lbl_result_cir_int_ft6["text"] = f"{corrPresion(result_ce_a6,lbl_result_cor_max6,e6):.3f}"
    lbl_result_cir_int_ft7["text"] = f"{corrPresion(result_ce_a7,lbl_result_cor_max7,e7):.3f}"
    lbl_result_cir_int_ft8["text"] = f"{corrPresion(result_ce_a8,lbl_result_cor_max8,e8):.3f}"
    lbl_result_cir_int_ft9["text"] = f"{corrPresion(result_ce_a9,lbl_result_cor_max9,e9):.3f}"
    lbl_result_cir_int_ft10["text"] = f"{corrPresion(result_ce_a10,lbl_result_cor_max10,e10):.3f}"

    # Circunferencia stressed
    lbl_result_cir_int_in1["text"] = f"{stressed(lbl_result_cor_max1,lbl_result_cir_int_ft1):.3f}"
    lbl_result_cir_int_in2["text"] = f"{stressed(lbl_result_cor_max2,lbl_result_cir_int_ft2):.3f}"
    lbl_result_cir_int_in3["text"] = f"{stressed(lbl_result_cor_max3,lbl_result_cir_int_ft3):.3f}"
    lbl_result_cir_int_in4["text"] = f"{stressed(lbl_result_cor_max4,lbl_result_cir_int_ft4):.3f}"
    lbl_result_cir_int_in5["text"] = f"{stressed(lbl_result_cor_max5,lbl_result_cir_int_ft5):.3f}"
    lbl_result_cir_int_in6["text"] = f"{stressed(lbl_result_cor_max6,lbl_result_cir_int_ft6):.3f}"
    lbl_result_cir_int_in7["text"] = f"{stressed(lbl_result_cor_max7,lbl_result_cir_int_ft7):.3f}"
    lbl_result_cir_int_in8["text"] = f"{stressed(lbl_result_cor_max8,lbl_result_cir_int_ft8):.3f}"
    lbl_result_cir_int_in9["text"] = f"{stressed(lbl_result_cor_max9,lbl_result_cir_int_ft9):.3f}"
    lbl_result_cir_int_in10["text"] = f"{stressed(lbl_result_cor_max10,lbl_result_cir_int_ft10):.3f}"


# Creacion de botones para guardar informacion
frm_buttons = tk.Frame(master=p6)
frm_buttons.pack(fill=tk.X, ipadx=5, ipady=5)

btn_submit = tk.Button(master=frm_buttons, text="Mostar",
                       command=corrCalibracion)
btn_submit.pack(padx=10, ipadx=10)

# Correciones para anillos
frm_form_vol_inc = tk.Frame(
    master=p7, relief=tk.GROOVE, width=200, height=100, borderwidth=3)
frm_form_vol_inc.pack(padx=250, pady=10)
frm_titulo_vol_inc = tk.Frame(master=frm_form_vol_inc, borderwidth=3)
frm_titulo_vol_inc.pack()
label_vol_inc = tk.Label(master=frm_titulo_vol_inc,
                         text="CORRECCIONES PARA ANILLOS")
label_vol_inc.pack()
frm_vol_inc = tk.Frame(master=frm_form_vol_inc,
                       width=200, height=100, borderwidth=3)
frm_vol_inc.pack(padx=20, pady=10)
# Labels para calculos de volumen incremental
lbl_cor_an = tk.Label(master=frm_vol_inc, text="Anillo")
lbl_cor_an.grid(row=0, column=0)
lbl_an1 = tk.Label(master=frm_vol_inc, text="1")
lbl_an1.grid(row=1, column=0)
lbl_an2 = tk.Label(master=frm_vol_inc, text="2")
lbl_an2.grid(row=2, column=0)
lbl_an3 = tk.Label(master=frm_vol_inc, text="3")
lbl_an3.grid(row=3, column=0)
lbl_an4 = tk.Label(master=frm_vol_inc, text="4")
lbl_an4.grid(row=4, column=0)
lbl_an5 = tk.Label(master=frm_vol_inc, text="5")
lbl_an5.grid(row=5, column=0)
lbl_an6 = tk.Label(master=frm_vol_inc, text="6")
lbl_an6.grid(row=6, column=0)
lbl_an7 = tk.Label(master=frm_vol_inc, text="7")
lbl_an7.grid(row=7, column=0)
lbl_an8 = tk.Label(master=frm_vol_inc, text="8")
lbl_an8.grid(row=8, column=0)
lbl_an9 = tk.Label(master=frm_vol_inc, text="9")
lbl_an9.grid(row=9, column=0)
lbl_an10 = tk.Label(master=frm_vol_inc, text="10")
lbl_an10.grid(row=10, column=0)
lbl_incr_vol = tk.Label(master=frm_vol_inc, text="Litros/cm\n Brutos")
lbl_incr_vol.grid(row=0, column=1)
lbl_vol_cab = tk.Label(master=frm_vol_inc, text="Corr. por anillo\n Litros/cm")
lbl_vol_cab.grid(row=0, column=2)
lbl_vol_cor_cab = tk.Label(
    master=frm_vol_inc, text="Corr. Incremento\n Litros/cm")
lbl_vol_cor_cab.grid(row=0, column=3)
lbl_cor_dilatacion = tk.Label(master=frm_vol_inc, text="Litros/cm\n Netos")
lbl_cor_dilatacion.grid(row=0, column=4)
lbl_col_incr = tk.Label(master=frm_vol_inc, text="Altura Fisica\n (cm)")
lbl_col_incr.grid(row=0, column=5)

# RESULTADOS: Litros/cm Brutos
lbl_result_icr_vol1 = tk.Label(master=frm_vol_inc)
lbl_result_icr_vol1.grid(row=1, column=1)
lbl_result_icr_vol2 = tk.Label(master=frm_vol_inc)
lbl_result_icr_vol2.grid(row=2, column=1)
lbl_result_icr_vol3 = tk.Label(master=frm_vol_inc)
lbl_result_icr_vol3.grid(row=3, column=1)
lbl_result_icr_vol4 = tk.Label(master=frm_vol_inc)
lbl_result_icr_vol4.grid(row=4, column=1)
lbl_result_icr_vol5 = tk.Label(master=frm_vol_inc)
lbl_result_icr_vol5.grid(row=5, column=1)
lbl_result_icr_vol6 = tk.Label(master=frm_vol_inc)
lbl_result_icr_vol6.grid(row=6, column=1)
lbl_result_icr_vol7 = tk.Label(master=frm_vol_inc)
lbl_result_icr_vol7.grid(row=7, column=1)
lbl_result_icr_vol8 = tk.Label(master=frm_vol_inc)
lbl_result_icr_vol8.grid(row=8, column=1)
lbl_result_icr_vol9 = tk.Label(master=frm_vol_inc)
lbl_result_icr_vol9.grid(row=9, column=1)
lbl_result_icr_vol10 = tk.Label(master=frm_vol_inc)
lbl_result_icr_vol10.grid(row=10, column=1)

# RESULTADOS: Corr. por anillo Litros/cm
lbl_result_icr_vol_cab1 = tk.Label(master=frm_vol_inc)
lbl_result_icr_vol_cab1.grid(row=1, column=2)
lbl_result_icr_vol_cab2 = tk.Label(master=frm_vol_inc)
lbl_result_icr_vol_cab2.grid(row=2, column=2)
lbl_result_icr_vol_cab3 = tk.Label(master=frm_vol_inc)
lbl_result_icr_vol_cab3.grid(row=3, column=2)
lbl_result_icr_vol_cab4 = tk.Label(master=frm_vol_inc)
lbl_result_icr_vol_cab4.grid(row=4, column=2)
lbl_result_icr_vol_cab5 = tk.Label(master=frm_vol_inc)
lbl_result_icr_vol_cab5.grid(row=5, column=2)
lbl_result_icr_vol_cab6 = tk.Label(master=frm_vol_inc)
lbl_result_icr_vol_cab6.grid(row=6, column=2)
lbl_result_icr_vol_cab7 = tk.Label(master=frm_vol_inc)
lbl_result_icr_vol_cab7.grid(row=7, column=2)
lbl_result_icr_vol_cab8 = tk.Label(master=frm_vol_inc)
lbl_result_icr_vol_cab8.grid(row=8, column=2)
lbl_result_icr_vol_cab9 = tk.Label(master=frm_vol_inc)
lbl_result_icr_vol_cab9.grid(row=9, column=2)
lbl_result_icr_vol_cab10 = tk.Label(master=frm_vol_inc)
lbl_result_icr_vol_cab10.grid(row=10, column=2)

# RESULTADOS: Corr. Incremento Litros/cm
lbl_result_vol_corr_cab1 = tk.Label(master=frm_vol_inc)
lbl_result_vol_corr_cab1.grid(row=1, column=3)
lbl_result_vol_corr_cab2 = tk.Label(master=frm_vol_inc)
lbl_result_vol_corr_cab2.grid(row=2, column=3)
lbl_result_vol_corr_cab3 = tk.Label(master=frm_vol_inc)
lbl_result_vol_corr_cab3.grid(row=3, column=3)
lbl_result_vol_corr_cab4 = tk.Label(master=frm_vol_inc)
lbl_result_vol_corr_cab4.grid(row=4, column=3)
lbl_result_vol_corr_cab5 = tk.Label(master=frm_vol_inc)
lbl_result_vol_corr_cab5.grid(row=5, column=3)
lbl_result_vol_corr_cab6 = tk.Label(master=frm_vol_inc)
lbl_result_vol_corr_cab6.grid(row=6, column=3)
lbl_result_vol_corr_cab7 = tk.Label(master=frm_vol_inc)
lbl_result_vol_corr_cab7.grid(row=7, column=3)
lbl_result_vol_corr_cab8 = tk.Label(master=frm_vol_inc)
lbl_result_vol_corr_cab8.grid(row=8, column=3)
lbl_result_vol_corr_cab9 = tk.Label(master=frm_vol_inc)
lbl_result_vol_corr_cab9.grid(row=9, column=3)
lbl_result_vol_corr_cab10 = tk.Label(master=frm_vol_inc)
lbl_result_vol_corr_cab10.grid(row=10, column=3)

# RESULTADOS: Litros/cm\n Netos
lbl_result_cor_dil1 = tk.Label(master=frm_vol_inc)
lbl_result_cor_dil1.grid(row=1, column=4)
lbl_result_cor_dil2 = tk.Label(master=frm_vol_inc)
lbl_result_cor_dil2.grid(row=2, column=4)
lbl_result_cor_dil3 = tk.Label(master=frm_vol_inc)
lbl_result_cor_dil3.grid(row=3, column=4)
lbl_result_cor_dil4 = tk.Label(master=frm_vol_inc)
lbl_result_cor_dil4.grid(row=4, column=4)
lbl_result_cor_dil5 = tk.Label(master=frm_vol_inc)
lbl_result_cor_dil5.grid(row=5, column=4)
lbl_result_cor_dil6 = tk.Label(master=frm_vol_inc)
lbl_result_cor_dil6.grid(row=6, column=4)
lbl_result_cor_dil7 = tk.Label(master=frm_vol_inc)
lbl_result_cor_dil7.grid(row=7, column=4)
lbl_result_cor_dil8 = tk.Label(master=frm_vol_inc)
lbl_result_cor_dil8.grid(row=8, column=4)
lbl_result_cor_dil9 = tk.Label(master=frm_vol_inc)
lbl_result_cor_dil9.grid(row=9, column=4)
lbl_result_cor_dil10 = tk.Label(master=frm_vol_inc)
lbl_result_cor_dil10.grid(row=10, column=4)

# RESULTADOS: Altura Fisica (cm)
lbl_result_col_incr1 = tk.Label(master=frm_vol_inc)
lbl_result_col_incr1.grid(row=1, column=5)
lbl_result_col_incr2 = tk.Label(master=frm_vol_inc)
lbl_result_col_incr2.grid(row=2, column=5)
lbl_result_col_incr3 = tk.Label(master=frm_vol_inc)
lbl_result_col_incr3.grid(row=3, column=5)
lbl_result_col_incr4 = tk.Label(master=frm_vol_inc)
lbl_result_col_incr4.grid(row=4, column=5)
lbl_result_col_incr5 = tk.Label(master=frm_vol_inc)
lbl_result_col_incr5.grid(row=5, column=5)
lbl_result_col_incr6 = tk.Label(master=frm_vol_inc)
lbl_result_col_incr6.grid(row=6, column=5)
lbl_result_col_incr7 = tk.Label(master=frm_vol_inc)
lbl_result_col_incr7.grid(row=7, column=5)
lbl_result_col_incr8 = tk.Label(master=frm_vol_inc)
lbl_result_col_incr8.grid(row=8, column=5)
lbl_result_col_incr9 = tk.Label(master=frm_vol_inc)
lbl_result_col_incr9.grid(row=9, column=5)
lbl_result_col_incr10 = tk.Label(master=frm_vol_inc)
lbl_result_col_incr10.grid(row=10, column=5)

# FUNCIONES CORRRECION DE ANILLOS


def litrosBrutos(circ_stress1, circ_stress2):  # lbl_result_cir_int_in1["text"]
    circ_stress1 = float(circ_stress1["text"])
    circ_stress2 = float(circ_stress2["text"])
    promedio = circ_stress1+circ_stress2
    return math.pow(promedio/2, 2)*0.001/(4*3.141592)


def diamDiaStress():
    mean = ((float(lbl_result_cir_int_in1["text"])+float(lbl_result_cir_int_in2["text"])+float(lbl_result_cir_int_in3["text"]) +
            float(lbl_result_cir_int_in4["text"])+float(
                lbl_result_cir_int_in5["text"])+float(lbl_result_cir_int_in6["text"])
            + float(lbl_result_cir_int_in7["text"])+float(
                lbl_result_cir_int_in8["text"])+float(lbl_result_cir_int_in9["text"])
            + float(lbl_result_cir_int_in10["text"]))/10)/3.141592
    return mean


def corrAnillo(altura1, altura2, espesor):
    ge_estacionaria = float(ent_est.get())
    dia_stress = diamDiaStress()
    espesor = float(espesor.get())
    altura1 = float(altura1.get())
    altura2 = float(altura2.get())
    k1 = (3.141592*998.232*(dia_stress**(3))*0.002204 *
          6.4516*ge_estacionaria)/116000000000000
    return k1*(altura2-altura1)/espesor


def corrAnillos():

    lbl_result_icr_vol1["text"] = f"{litrosBrutos(lbl_result_cir_int_in1,lbl_result_cir_int_in2):.3f}"
    lbl_result_icr_vol2["text"] = f"{litrosBrutos(lbl_result_cir_int_in2,lbl_result_cir_int_in3):.3f}"
    lbl_result_icr_vol3["text"] = f"{litrosBrutos(lbl_result_cir_int_in3,lbl_result_cir_int_in4):.3f}"
    lbl_result_icr_vol4["text"] = f"{litrosBrutos(lbl_result_cir_int_in4,lbl_result_cir_int_in5):.3f}"
    lbl_result_icr_vol5["text"] = f"{litrosBrutos(lbl_result_cir_int_in5,lbl_result_cir_int_in6):.3f}"
    lbl_result_icr_vol6["text"] = f"{litrosBrutos(lbl_result_cir_int_in6,lbl_result_cir_int_in7):.3f}"
    lbl_result_icr_vol7["text"] = f"{litrosBrutos(lbl_result_cir_int_in7,lbl_result_cir_int_in8):.3f}"
    lbl_result_icr_vol8["text"] = f"{litrosBrutos(lbl_result_cir_int_in8,lbl_result_cir_int_in9):.3f}"
    lbl_result_icr_vol9["text"] = f"{litrosBrutos(lbl_result_cir_int_in9,lbl_result_cir_int_in10):.3f}"
    lbl_result_icr_vol10["text"] = f"{litrosBrutos(lbl_result_cir_int_in10,lbl_result_cir_int_in10):.3f}"

    # Correccion por anillo
    lbl_result_icr_vol_cab1["text"] = 0
    lbl_result_icr_vol_cab2["text"] = f"{corrAnillo(ent_da_a1,ent_da_a2,ent_et1):.3f}"
    lbl_result_icr_vol_cab3["text"] = f"{corrAnillo(ent_da_a2,ent_da_a3,ent_et2):.3f}"
    lbl_result_icr_vol_cab4["text"] = f"{corrAnillo(ent_da_a3,ent_da_a4,ent_et3):.3f}"
    lbl_result_icr_vol_cab5["text"] = f"{corrAnillo(ent_da_a4,ent_da_a5,ent_et4):.3f}"
    lbl_result_icr_vol_cab6["text"] = f"{corrAnillo(ent_da_a5,ent_da_a6,ent_et5):.3f}"
    lbl_result_icr_vol_cab7["text"] = f"{corrAnillo(ent_da_a6,ent_da_a7,ent_et6):.3f}"
    lbl_result_icr_vol_cab8["text"] = f"{corrAnillo(ent_da_a7,ent_da_a8,ent_et7):.3f}"
    lbl_result_icr_vol_cab9["text"] = f"{corrAnillo(ent_da_a8,ent_da_a9,ent_et8):.3f}"
    lbl_result_icr_vol_cab10["text"] = f"{corrAnillo(ent_da_a9,ent_da_a10,ent_et9):.3f}"

    # Correcion incremento
    lbl_result_vol_corr_cab1["text"] = 0
    ci2 = float(lbl_result_icr_vol_cab2["text"])
    lbl_result_vol_corr_cab2["text"] = f"{ci2:.3f}"
    ci3 = float(lbl_result_icr_vol_cab3["text"])
    icr2 = float(lbl_result_vol_corr_cab2["text"])
    lbl_result_vol_corr_cab3["text"] = f"{ci3+icr2:.3f}"
    ci4 = float(lbl_result_icr_vol_cab4["text"])
    icr3 = float(lbl_result_vol_corr_cab3["text"])
    lbl_result_vol_corr_cab4["text"] = f"{ci4+icr3:.3f}"
    ci5 = float(lbl_result_icr_vol_cab5["text"])
    icr4 = float(lbl_result_vol_corr_cab4["text"])
    lbl_result_vol_corr_cab5["text"] = f"{ci5+icr4:.3f}"
    ci6 = float(lbl_result_icr_vol_cab6["text"])
    icr5 = float(lbl_result_vol_corr_cab5["text"])
    lbl_result_vol_corr_cab6["text"] = f"{ci6+icr5:.3f}"
    ci7 = float(lbl_result_icr_vol_cab7["text"])
    icr6 = float(lbl_result_vol_corr_cab6["text"])
    lbl_result_vol_corr_cab7["text"] = f"{ci7+icr6:.3f}"
    ci8 = float(lbl_result_icr_vol_cab8["text"])
    icr7 = float(lbl_result_vol_corr_cab7["text"])
    lbl_result_vol_corr_cab8["text"] = f"{ci8+icr7:.3f}"
    ci9 = float(lbl_result_icr_vol_cab9["text"])
    icr8 = float(lbl_result_vol_corr_cab8["text"])
    lbl_result_vol_corr_cab9["text"] = f"{ci9+icr8:.3f}"
    ci10 = float(lbl_result_icr_vol_cab10["text"])
    icr9 = float(lbl_result_vol_corr_cab9["text"])
    lbl_result_vol_corr_cab10["text"] = f"{ci10+icr9:.3f}"

    # Litros/cm Netos
    lb1 = float(lbl_result_icr_vol1["text"])
    cil1 = float(lbl_result_vol_corr_cab1["text"])
    lbl_result_cor_dil1["text"] = f"{lb1+cil1:.3f}"
    lb2 = float(lbl_result_icr_vol2["text"])
    cil2 = float(lbl_result_vol_corr_cab2["text"])
    lbl_result_cor_dil2["text"] = f"{lb2+cil2:.3f}"
    lb3 = float(lbl_result_icr_vol3["text"])
    cil3 = float(lbl_result_vol_corr_cab3["text"])
    lbl_result_cor_dil3["text"] = f"{lb3+cil3:.3f}"
    lb4 = float(lbl_result_icr_vol4["text"])
    cil4 = float(lbl_result_vol_corr_cab4["text"])
    lbl_result_cor_dil4["text"] = f"{lb4+cil4:.3f}"
    lb5 = float(lbl_result_icr_vol5["text"])
    cil5 = float(lbl_result_vol_corr_cab5["text"])
    lbl_result_cor_dil5["text"] = f"{lb5+cil5:.3f}"
    lb6 = float(lbl_result_icr_vol6["text"])
    cil6 = float(lbl_result_vol_corr_cab6["text"])
    lbl_result_cor_dil6["text"] = f"{lb6+cil6:.3f}"
    lb7 = float(lbl_result_icr_vol7["text"])
    cil7 = float(lbl_result_vol_corr_cab7["text"])
    lbl_result_cor_dil7["text"] = f"{lb7+cil7:.3f}"
    lb8 = float(lbl_result_icr_vol8["text"])
    cil8 = float(lbl_result_vol_corr_cab8["text"])
    lbl_result_cor_dil8["text"] = f"{lb8+cil8:.3f}"
    lb9 = float(lbl_result_icr_vol9["text"])
    cil9 = float(lbl_result_vol_corr_cab9["text"])
    lbl_result_cor_dil9["text"] = f"{lb9+cil9:.3f}"
    lb10 = float(lbl_result_icr_vol10["text"])
    cil10 = float(lbl_result_vol_corr_cab10["text"])
    lbl_result_cor_dil10["text"] = f"{lb10+cil10:.3f}"

    # Altura fisica
    c1 = float(ent_da_a1.get())
    lbl_result_col_incr1["text"] = f"{c1:.3f}"
    c2 = float(ent_da_a2.get())
    lbl_result_col_incr2["text"] = f"{c2:.3f}"
    c3 = float(ent_da_a3.get())
    lbl_result_col_incr3["text"] = f"{c3:.3f}"
    c4 = float(ent_da_a4.get())
    lbl_result_col_incr4["text"] = f"{c4:.3f}"
    c5 = float(ent_da_a5.get())
    lbl_result_col_incr5["text"] = f"{c5:.3f}"
    c6 = float(ent_da_a6.get())
    lbl_result_col_incr6["text"] = f"{c6:.3f}"
    c7 = float(ent_da_a7.get())
    lbl_result_col_incr7["text"] = f"{c7:.3f}"
    c8 = float(ent_da_a8.get())
    lbl_result_col_incr8["text"] = f"{c8:.3f}"
    c9 = float(ent_da_a9.get())
    lbl_result_col_incr9["text"] = f"{c9:.3f}"
    c10 = float(ent_da_a10.get())
    lbl_result_col_incr10["text"] = f"{c10:.3f}"


# Calculo de volumenes muertos
frm_titulo_p8 = tk.Frame(master=p8, borderwidth=3)
frm_titulo_p8.pack()
label_p8 = tk.Label(master=frm_titulo_p8,
                    text="CALCULO DE LOS VOLUMENES MUERTOS")
label_p8.pack()
frm_form_volm_ac = tk.Frame(
    master=p8, relief=tk.GROOVE, width=100, height=100, borderwidth=3)
frm_form_volm_ac.pack(fill=tk.X, padx=20, pady=10)
frm_titulo_volm_ac = tk.Frame(master=frm_form_volm_ac, borderwidth=3)
frm_titulo_volm_ac.pack()
label_volm_ac = tk.Label(master=frm_titulo_volm_ac,
                         text="CALCULOS DE LOS ACCESORIOS")
label_volm_ac.pack()
frm_volm_ac = tk.Frame(master=frm_form_volm_ac,
                       width=100, height=100, borderwidth=3)
frm_volm_ac.pack(fill=tk.X, padx=20, pady=10)
# Labels para volumenes muertos
lbl_vm_ac = tk.Label(master=frm_volm_ac, text="Altura\ncm")
lbl_vm_ac.grid(row=0, column=0)
lbl_vm_alt = tk.Label(master=frm_volm_ac, text="Base Inicial \nlit/cm")
lbl_vm_alt.grid(row=0, column=1)
lbl_vm_acc1 = tk.Label(master=frm_volm_ac, text="Accesorio 1")
lbl_vm_acc1.grid(row=0, column=2)
lbl_vm_acc2 = tk.Label(master=frm_volm_ac, text="Accesorio 2")
lbl_vm_acc2.grid(row=0, column=3)
lbl_vm_acc3 = tk.Label(master=frm_volm_ac, text="Accesorio 3")
lbl_vm_acc3.grid(row=0, column=4)
lbl_vm_acc4 = tk.Label(master=frm_volm_ac, text="Accesorio 4")
lbl_vm_acc4.grid(row=0, column=5)
lbl_vm_acc5 = tk.Label(master=frm_volm_ac, text="Accesorio 5")
lbl_vm_acc5.grid(row=0, column=6)
lbl_vm_acc6 = tk.Label(master=frm_volm_ac, text="Accesorio 6")
lbl_vm_acc6.grid(row=0, column=7)
lbl_vm_acc7 = tk.Label(master=frm_volm_ac, text="Accesorio 7")
lbl_vm_acc7.grid(row=0, column=8)
lbl_vm_acc8 = tk.Label(master=frm_volm_ac, text="Accesorio 8")
lbl_vm_acc8.grid(row=0, column=9)
lbl_vm_acc9 = tk.Label(master=frm_volm_ac, text="Accesorio 9")
lbl_vm_acc9.grid(row=0, column=10)
lbl_vm_bsf = tk.Label(master=frm_volm_ac, text="Base Final\n lit/cm")
lbl_vm_bsf.grid(row=0, column=11)
lbl_vm_lt_cr = tk.Label(master=frm_volm_ac, text="Litros\n corregidos")
lbl_vm_lt_cr.grid(row=0, column=12)
# Alturas
ent_alt1 = tk.Entry(master=frm_volm_ac, width=10)
ent_alt1.grid(row=1, column=0)
ent_alt2 = tk.Entry(master=frm_volm_ac, width=10)
ent_alt2.grid(row=2, column=0)
ent_alt3 = tk.Entry(master=frm_volm_ac, width=10)
ent_alt3.grid(row=3, column=0)
ent_alt4 = tk.Entry(master=frm_volm_ac, width=10)
ent_alt4.grid(row=4, column=0)
ent_alt5 = tk.Entry(master=frm_volm_ac, width=10)
ent_alt5.grid(row=5, column=0)
ent_alt6 = tk.Entry(master=frm_volm_ac, width=10)
ent_alt6.grid(row=6, column=0)
ent_alt7 = tk.Entry(master=frm_volm_ac, width=10)
ent_alt7.grid(row=7, column=0)
ent_alt8 = tk.Entry(master=frm_volm_ac, width=10)
ent_alt8.grid(row=8, column=0)
ent_alt9 = tk.Entry(master=frm_volm_ac, width=10)
ent_alt9.grid(row=9, column=0)
ent_alt10 = tk.Entry(master=frm_volm_ac, width=10)
ent_alt10.grid(row=10, column=0)

# Base inicial
ent_bs1 = tk.Label(master=frm_volm_ac, width=10)
ent_bs1.grid(row=1, column=1)
ent_bs2 = tk.Label(master=frm_volm_ac, width=10)
ent_bs2.grid(row=2, column=1)
ent_bs3 = tk.Label(master=frm_volm_ac, width=10)
ent_bs3.grid(row=3, column=1)
ent_bs4 = tk.Label(master=frm_volm_ac, width=10)
ent_bs4.grid(row=4, column=1)
ent_bs5 = tk.Label(master=frm_volm_ac, width=10)
ent_bs5.grid(row=5, column=1)
ent_bs6 = tk.Label(master=frm_volm_ac, width=10)
ent_bs6.grid(row=6, column=1)
ent_bs7 = tk.Label(master=frm_volm_ac, width=10)
ent_bs7.grid(row=7, column=1)
ent_bs8 = tk.Label(master=frm_volm_ac, width=10)
ent_bs8.grid(row=8, column=1)
ent_bs9 = tk.Label(master=frm_volm_ac, width=10)
ent_bs9.grid(row=9, column=1)
ent_bs10 = tk.Label(master=frm_volm_ac, width=10)
ent_bs10.grid(row=10, column=1)

# Accesorio 1
ent_ac_1 = tk.Entry(master=frm_volm_ac, width=10)
ent_ac_1.grid(row=1, column=2)
ent_ac_2 = tk.Entry(master=frm_volm_ac, width=10)
ent_ac_2.grid(row=2, column=2)
ent_ac_3 = tk.Entry(master=frm_volm_ac, width=10)
ent_ac_3.grid(row=3, column=2)
ent_ac_4 = tk.Entry(master=frm_volm_ac, width=10)
ent_ac_4.grid(row=4, column=2)
ent_ac_5 = tk.Entry(master=frm_volm_ac, width=10)
ent_ac_5.grid(row=5, column=2)
ent_ac_6 = tk.Entry(master=frm_volm_ac, width=10)
ent_ac_6.grid(row=6, column=2)
ent_ac_7 = tk.Entry(master=frm_volm_ac, width=10)
ent_ac_7.grid(row=7, column=2)
ent_ac_8 = tk.Entry(master=frm_volm_ac, width=10)
ent_ac_8.grid(row=8, column=2)
ent_ac_9 = tk.Entry(master=frm_volm_ac, width=10)
ent_ac_9.grid(row=9, column=2)
ent_ac_10 = tk.Entry(master=frm_volm_ac, width=10)
ent_ac_10.grid(row=10, column=2)

# Accesorio 2
ent_ac2_1 = tk.Entry(master=frm_volm_ac, width=10)
ent_ac2_1.grid(row=1, column=3)
ent_ac2_2 = tk.Entry(master=frm_volm_ac, width=10)
ent_ac2_2.grid(row=2, column=3)
ent_ac2_3 = tk.Entry(master=frm_volm_ac, width=10)
ent_ac2_3.grid(row=3, column=3)
ent_ac2_4 = tk.Entry(master=frm_volm_ac, width=10)
ent_ac2_4.grid(row=4, column=3)
ent_ac2_5 = tk.Entry(master=frm_volm_ac, width=10)
ent_ac2_5.grid(row=5, column=3)
ent_ac2_6 = tk.Entry(master=frm_volm_ac, width=10)
ent_ac2_6.grid(row=6, column=3)
ent_ac2_7 = tk.Entry(master=frm_volm_ac, width=10)
ent_ac2_7.grid(row=7, column=3)
ent_ac2_8 = tk.Entry(master=frm_volm_ac, width=10)
ent_ac2_8.grid(row=8, column=3)
ent_ac2_9 = tk.Entry(master=frm_volm_ac, width=10)
ent_ac2_9.grid(row=9, column=3)
ent_ac2_10 = tk.Entry(master=frm_volm_ac, width=10)
ent_ac2_10.grid(row=10, column=3)

# Accesorio 3
ent_ac3_1 = tk.Entry(master=frm_volm_ac, width=10)
ent_ac3_1.grid(row=1, column=4)
ent_ac3_2 = tk.Entry(master=frm_volm_ac, width=10)
ent_ac3_2.grid(row=2, column=4)
ent_ac3_3 = tk.Entry(master=frm_volm_ac, width=10)
ent_ac3_3.grid(row=3, column=4)
ent_ac3_4 = tk.Entry(master=frm_volm_ac, width=10)
ent_ac3_4.grid(row=4, column=4)
ent_ac3_5 = tk.Entry(master=frm_volm_ac, width=10)
ent_ac3_5.grid(row=5, column=4)
ent_ac3_6 = tk.Entry(master=frm_volm_ac, width=10)
ent_ac3_6.grid(row=6, column=4)
ent_ac3_7 = tk.Entry(master=frm_volm_ac, width=10)
ent_ac3_7.grid(row=7, column=4)
ent_ac3_8 = tk.Entry(master=frm_volm_ac, width=10)
ent_ac3_8.grid(row=8, column=4)
ent_ac3_9 = tk.Entry(master=frm_volm_ac, width=10)
ent_ac3_9.grid(row=9, column=4)
ent_ac3_10 = tk.Entry(master=frm_volm_ac, width=10)
ent_ac3_10.grid(row=10, column=4)

# Accesorio 4
ent_ac4_1 = tk.Entry(master=frm_volm_ac, width=10)
ent_ac4_1.grid(row=1, column=5)
ent_ac4_2 = tk.Entry(master=frm_volm_ac, width=10)
ent_ac4_2.grid(row=2, column=5)
ent_ac4_3 = tk.Entry(master=frm_volm_ac, width=10)
ent_ac4_3.grid(row=3, column=5)
ent_ac4_4 = tk.Entry(master=frm_volm_ac, width=10)
ent_ac4_4.grid(row=4, column=5)
ent_ac4_5 = tk.Entry(master=frm_volm_ac, width=10)
ent_ac4_5.grid(row=5, column=5)
ent_ac4_6 = tk.Entry(master=frm_volm_ac, width=10)
ent_ac4_6.grid(row=6, column=5)
ent_ac4_7 = tk.Entry(master=frm_volm_ac, width=10)
ent_ac4_7.grid(row=7, column=5)
ent_ac4_8 = tk.Entry(master=frm_volm_ac, width=10)
ent_ac4_8.grid(row=8, column=5)
ent_ac4_9 = tk.Entry(master=frm_volm_ac, width=10)
ent_ac4_9.grid(row=9, column=5)
ent_ac4_10 = tk.Entry(master=frm_volm_ac, width=10)
ent_ac4_10.grid(row=10, column=5)

# Accesorio 5
ent_ac5_1 = tk.Entry(master=frm_volm_ac, width=10)
ent_ac5_1.grid(row=1, column=6)
ent_ac5_2 = tk.Entry(master=frm_volm_ac, width=10)
ent_ac5_2.grid(row=2, column=6)
ent_ac5_3 = tk.Entry(master=frm_volm_ac, width=10)
ent_ac5_3.grid(row=3, column=6)
ent_ac5_4 = tk.Entry(master=frm_volm_ac, width=10)
ent_ac5_4.grid(row=4, column=6)
ent_ac5_5 = tk.Entry(master=frm_volm_ac, width=10)
ent_ac5_5.grid(row=5, column=6)
ent_ac5_6 = tk.Entry(master=frm_volm_ac, width=10)
ent_ac5_6.grid(row=6, column=6)
ent_ac5_7 = tk.Entry(master=frm_volm_ac, width=10)
ent_ac5_7.grid(row=7, column=6)
ent_ac5_8 = tk.Entry(master=frm_volm_ac, width=10)
ent_ac5_8.grid(row=8, column=6)
ent_ac5_9 = tk.Entry(master=frm_volm_ac, width=10)
ent_ac5_9.grid(row=9, column=6)
ent_ac5_10 = tk.Entry(master=frm_volm_ac, width=10)
ent_ac5_10.grid(row=10, column=6)

# Accesorio 6
ent_ac6_1 = tk.Entry(master=frm_volm_ac, width=10)
ent_ac6_1.grid(row=1, column=7)
ent_ac6_2 = tk.Entry(master=frm_volm_ac, width=10)
ent_ac6_2.grid(row=2, column=7)
ent_ac6_3 = tk.Entry(master=frm_volm_ac, width=10)
ent_ac6_3.grid(row=3, column=7)
ent_ac6_4 = tk.Entry(master=frm_volm_ac, width=10)
ent_ac6_4.grid(row=4, column=7)
ent_ac6_5 = tk.Entry(master=frm_volm_ac, width=10)
ent_ac6_5.grid(row=5, column=7)
ent_ac6_6 = tk.Entry(master=frm_volm_ac, width=10)
ent_ac6_6.grid(row=6, column=7)
ent_ac6_7 = tk.Entry(master=frm_volm_ac, width=10)
ent_ac6_7.grid(row=7, column=7)
ent_ac6_8 = tk.Entry(master=frm_volm_ac, width=10)
ent_ac6_8.grid(row=8, column=7)
ent_ac6_9 = tk.Entry(master=frm_volm_ac, width=10)
ent_ac6_9.grid(row=9, column=7)
ent_ac6_10 = tk.Entry(master=frm_volm_ac, width=10)
ent_ac6_10.grid(row=10, column=7)

# Accesorio 7
ent_ac7_1 = tk.Entry(master=frm_volm_ac, width=10)
ent_ac7_1.grid(row=1, column=8)
ent_ac7_2 = tk.Entry(master=frm_volm_ac, width=10)
ent_ac7_2.grid(row=2, column=8)
ent_ac7_3 = tk.Entry(master=frm_volm_ac, width=10)
ent_ac7_3.grid(row=3, column=8)
ent_ac7_4 = tk.Entry(master=frm_volm_ac, width=10)
ent_ac7_4.grid(row=4, column=8)
ent_ac7_5 = tk.Entry(master=frm_volm_ac, width=10)
ent_ac7_5.grid(row=5, column=8)
ent_ac7_6 = tk.Entry(master=frm_volm_ac, width=10)
ent_ac7_6.grid(row=6, column=8)
ent_ac7_7 = tk.Entry(master=frm_volm_ac, width=10)
ent_ac7_7.grid(row=7, column=8)
ent_ac7_8 = tk.Entry(master=frm_volm_ac, width=10)
ent_ac7_8.grid(row=8, column=8)
ent_ac7_9 = tk.Entry(master=frm_volm_ac, width=10)
ent_ac7_9.grid(row=9, column=8)
ent_ac7_10 = tk.Entry(master=frm_volm_ac, width=10)
ent_ac7_10.grid(row=10, column=8)

# Accesorio 8
ent_ac8_1 = tk.Entry(master=frm_volm_ac, width=10)
ent_ac8_1.grid(row=1, column=9)
ent_ac8_2 = tk.Entry(master=frm_volm_ac, width=10)
ent_ac8_2.grid(row=2, column=9)
ent_ac8_3 = tk.Entry(master=frm_volm_ac, width=10)
ent_ac8_3.grid(row=3, column=9)
ent_ac8_4 = tk.Entry(master=frm_volm_ac, width=10)
ent_ac8_4.grid(row=4, column=9)
ent_ac8_5 = tk.Entry(master=frm_volm_ac, width=10)
ent_ac8_5.grid(row=5, column=9)
ent_ac8_6 = tk.Entry(master=frm_volm_ac, width=10)
ent_ac8_6.grid(row=6, column=9)
ent_ac8_7 = tk.Entry(master=frm_volm_ac, width=10)
ent_ac8_7.grid(row=7, column=9)
ent_ac8_8 = tk.Entry(master=frm_volm_ac, width=10)
ent_ac8_8.grid(row=8, column=9)
ent_ac8_9 = tk.Entry(master=frm_volm_ac, width=10)
ent_ac8_9.grid(row=9, column=9)
ent_ac8_10 = tk.Entry(master=frm_volm_ac, width=10)
ent_ac8_10.grid(row=10, column=9)

# Accesorio 9
ent_ac9_1 = tk.Entry(master=frm_volm_ac, width=10)
ent_ac9_1.grid(row=1, column=10)
ent_ac9_2 = tk.Entry(master=frm_volm_ac, width=10)
ent_ac9_2.grid(row=2, column=10)
ent_ac9_3 = tk.Entry(master=frm_volm_ac, width=10)
ent_ac9_3.grid(row=3, column=10)
ent_ac9_4 = tk.Entry(master=frm_volm_ac, width=10)
ent_ac9_4.grid(row=4, column=10)
ent_ac9_5 = tk.Entry(master=frm_volm_ac, width=10)
ent_ac9_5.grid(row=5, column=10)
ent_ac9_6 = tk.Entry(master=frm_volm_ac, width=10)
ent_ac9_6.grid(row=6, column=10)
ent_ac9_7 = tk.Entry(master=frm_volm_ac, width=10)
ent_ac9_7.grid(row=7, column=10)
ent_ac9_8 = tk.Entry(master=frm_volm_ac, width=10)
ent_ac9_8.grid(row=8, column=10)
ent_ac9_9 = tk.Entry(master=frm_volm_ac, width=10)
ent_ac9_9.grid(row=9, column=10)
ent_ac9_10 = tk.Entry(master=frm_volm_ac, width=10)
ent_ac9_10.grid(row=10, column=10)

# Base Final
lbl_vm_bsf1 = tk.Label(master=frm_volm_ac)
lbl_vm_bsf1.grid(row=1, column=11)
lbl_vm_bsf2 = tk.Label(master=frm_volm_ac)
lbl_vm_bsf2.grid(row=2, column=11)
lbl_vm_bsf3 = tk.Label(master=frm_volm_ac)
lbl_vm_bsf3.grid(row=3, column=11)
lbl_vm_bsf4 = tk.Label(master=frm_volm_ac)
lbl_vm_bsf4.grid(row=4, column=11)
lbl_vm_bsf5 = tk.Label(master=frm_volm_ac)
lbl_vm_bsf5.grid(row=5, column=11)
lbl_vm_bsf6 = tk.Label(master=frm_volm_ac)
lbl_vm_bsf6.grid(row=6, column=11)
lbl_vm_bsf7 = tk.Label(master=frm_volm_ac)
lbl_vm_bsf7.grid(row=7, column=11)
lbl_vm_bsf8 = tk.Label(master=frm_volm_ac)
lbl_vm_bsf8.grid(row=8, column=11)
lbl_vm_bsf9 = tk.Label(master=frm_volm_ac)
lbl_vm_bsf9.grid(row=9, column=11)
lbl_vm_bsf10 = tk.Label(master=frm_volm_ac)
lbl_vm_bsf10.grid(row=10, column=11)

# Litros corregidos
lbl_vm_lt_cr1 = tk.Label(master=frm_volm_ac)
lbl_vm_lt_cr1.grid(row=1, column=12)
lbl_vm_lt_cr2 = tk.Label(master=frm_volm_ac)
lbl_vm_lt_cr2.grid(row=2, column=12)
lbl_vm_lt_cr3 = tk.Label(master=frm_volm_ac)
lbl_vm_lt_cr3.grid(row=3, column=12)
lbl_vm_lt_cr4 = tk.Label(master=frm_volm_ac)
lbl_vm_lt_cr4.grid(row=4, column=12)
lbl_vm_lt_cr5 = tk.Label(master=frm_volm_ac)
lbl_vm_lt_cr5.grid(row=5, column=12)
lbl_vm_lt_cr6 = tk.Label(master=frm_volm_ac)
lbl_vm_lt_cr6.grid(row=6, column=12)
lbl_vm_lt_cr7 = tk.Label(master=frm_volm_ac)
lbl_vm_lt_cr7.grid(row=7, column=12)
lbl_vm_lt_cr8 = tk.Label(master=frm_volm_ac)
lbl_vm_lt_cr8.grid(row=8, column=12)
lbl_vm_lt_cr9 = tk.Label(master=frm_volm_ac)
lbl_vm_lt_cr9.grid(row=9, column=12)
lbl_vm_lt_cr10 = tk.Label(master=frm_volm_ac)
lbl_vm_lt_cr10.grid(row=10, column=12)

# Funciones para resultados


def baseInicial(altura):  # float(ent_da_a1.get())  altura
    altura = float(altura.get())
    if altura > float(ent_da_a1.get()) and altura <= float(ent_da_a2.get()):
        return float(lbl_result_cor_dil1["text"].split()[0])
    elif altura > float(ent_da_a2.get()) and altura <= float(ent_da_a3.get()):
        return float(lbl_result_cor_dil2["text"].split()[0])
    elif altura > float(ent_da_a3.get()) and altura <= float(ent_da_a4.get()):
        return float(lbl_result_cor_dil3["text"].split()[0])
    elif altura > float(ent_da_a4.get()) and altura <= float(ent_da_a5.get()):
        return float(lbl_result_cor_dil4["text"].split()[0])
    elif altura > float(ent_da_a5.get()) and altura <= float(ent_da_a6.get()):
        return float(lbl_result_cor_dil5["text"].split()[0])
    elif altura > float(ent_da_a6.get()) and altura <= float(ent_da_a7.get()):
        return float(lbl_result_cor_dil6["text"].split()[0])
    elif altura > float(ent_da_a7.get()) and altura <= float(ent_da_a8.get()):
        return float(lbl_result_cor_dil7["text"].split()[0])
    elif altura > float(ent_da_a8.get()) and altura <= float(ent_da_a9.get()):
        return float(lbl_result_cor_dil8["text"].split()[0])
    elif altura > float(ent_da_a9.get()) and altura <= float(ent_da_a10.get()):
        return float(lbl_result_cor_dil9["text"].split()[0])
    return float(ent_altura_base_inicial_cm0.get())


def baseFinal(altura, bi, a1, a2, a3, a4, a5, a6, a7, a8, a9):
    altura = float(altura.get())
    bi = float(bi['text'])
    a1 = float(a1.get())
    a2 = float(a2.get())
    a3 = float(a3.get())
    a4 = float(a4.get())
    a5 = float(a5.get())
    a6 = float(a6.get())
    a7 = float(a7.get())
    a8 = float(a8.get())
    a9 = float(a9.get())
    return bi+a1+a2+a3+a4+a5+a6+a7+a8+a9


def litrosCoor(baseFinal, tempAcero):  # ent_temp_acero
    altura = float(ent_altura_tanque.get())
    inclinacionMayor = float(ent_inclinacion_tanque.get())
    inclinacion = inclinacionMayor/altura
    correcion_incl = 0
    if inclinacion > 0.014:
        correcion_incl = (math.pow(((inclinacion*inclinacion)+1), 0.5)-1)*100
    baseFinal = float(baseFinal['text'])
    tempAcero = float(tempAcero.get())
    factor_cor_temp = 1+12.4 * \
        math.pow(10, -6)*(tempAcero-60)+4*math.pow(10, -9)*(tempAcero-60)
    return baseFinal*factor_cor_temp+(baseFinal*correcion_incl/100)


def mostrarCorreciones():
    # Resultado base inicial
    ent_bs1["text"] = f"{baseInicial(ent_alt1):.3f}"
    ent_bs2["text"] = f"{baseInicial(ent_alt2):.3f}"
    ent_bs3["text"] = f"{baseInicial(ent_alt3):.3f}"
    ent_bs4["text"] = f"{baseInicial(ent_alt4):.3f}"
    ent_bs5["text"] = f"{baseInicial(ent_alt5):.3f}"
    ent_bs6["text"] = f"{baseInicial(ent_alt6):.3f}"
    ent_bs7["text"] = f"{baseInicial(ent_alt7):.3f}"
    ent_bs8["text"] = f"{baseInicial(ent_alt8):.3f}"
    ent_bs9["text"] = f"{baseInicial(ent_alt9):.3f}"
    ent_bs10["text"] = f"{baseInicial(ent_alt10):.3f}"

    # Resultados base final
    lbl_vm_bsf1['text'] = f"{baseFinal(ent_alt1,ent_bs1,ent_ac_1,ent_ac2_1,ent_ac3_1,ent_ac4_1,ent_ac5_1,ent_ac6_1,ent_ac7_1,ent_ac8_1,ent_ac9_1):.3f}"
    lbl_vm_bsf2['text'] = f"{baseFinal(ent_alt2,ent_bs2,ent_ac_2,ent_ac2_2,ent_ac3_2,ent_ac4_2,ent_ac5_2,ent_ac6_2,ent_ac7_2,ent_ac8_2,ent_ac9_2):.3f}"
    lbl_vm_bsf3['text'] = f"{baseFinal(ent_alt3,ent_bs3,ent_ac_3,ent_ac2_3,ent_ac3_3,ent_ac4_3,ent_ac5_3,ent_ac6_3,ent_ac7_3,ent_ac8_3,ent_ac9_3):.3f}"
    lbl_vm_bsf4['text'] = f"{baseFinal(ent_alt4,ent_bs4,ent_ac_4,ent_ac2_4,ent_ac3_4,ent_ac4_4,ent_ac5_4,ent_ac6_4,ent_ac7_4,ent_ac8_4,ent_ac9_4):.3f}"
    lbl_vm_bsf5['text'] = f"{baseFinal(ent_alt5,ent_bs5,ent_ac_5,ent_ac2_5,ent_ac3_5,ent_ac4_5,ent_ac5_5,ent_ac6_5,ent_ac7_5,ent_ac8_5,ent_ac9_5):.3f}"
    lbl_vm_bsf6['text'] = f"{baseFinal(ent_alt6,ent_bs6,ent_ac_6,ent_ac2_6,ent_ac3_6,ent_ac4_6,ent_ac5_6,ent_ac6_6,ent_ac7_6,ent_ac8_6,ent_ac9_6):.3f}"
    lbl_vm_bsf7['text'] = f"{baseFinal(ent_alt7,ent_bs7,ent_ac_7,ent_ac2_7,ent_ac3_7,ent_ac4_7,ent_ac5_7,ent_ac6_7,ent_ac7_7,ent_ac8_7,ent_ac9_7):.3f}"
    lbl_vm_bsf8['text'] = f"{baseFinal(ent_alt8,ent_bs8,ent_ac_8,ent_ac2_8,ent_ac3_8,ent_ac4_8,ent_ac5_8,ent_ac6_8,ent_ac7_8,ent_ac8_8,ent_ac9_8):.3f}"
    lbl_vm_bsf9['text'] = f"{baseFinal(ent_alt9,ent_bs9,ent_ac_9,ent_ac2_9,ent_ac3_9,ent_ac4_9,ent_ac5_9,ent_ac6_9,ent_ac7_9,ent_ac8_9,ent_ac9_9):.3f}"
    lbl_vm_bsf10['text'] = f"{baseFinal(ent_alt10,ent_bs10,ent_ac_10,ent_ac2_10,ent_ac3_10,ent_ac4_10,ent_ac5_10,ent_ac6_10,ent_ac7_10,ent_ac8_10,ent_ac9_10):.3f}"

    # Litros corregidos
    lbl_vm_lt_cr1['text'] = f"{0}"
    lbl_vm_lt_cr2['text'] = f"{litrosCoor(lbl_vm_bsf2,ent_temp_acero):.3f}"
    lbl_vm_lt_cr3['text'] = f"{litrosCoor(lbl_vm_bsf3,ent_temp_acero):.3f}"
    lbl_vm_lt_cr4['text'] = f"{litrosCoor(lbl_vm_bsf4,ent_temp_acero):.3f}"
    lbl_vm_lt_cr5['text'] = f"{litrosCoor(lbl_vm_bsf5,ent_temp_acero):.3f}"
    lbl_vm_lt_cr6['text'] = f"{litrosCoor(lbl_vm_bsf6,ent_temp_acero):.3f}"
    lbl_vm_lt_cr7['text'] = f"{litrosCoor(lbl_vm_bsf7,ent_temp_acero):.3f}"
    lbl_vm_lt_cr8['text'] = f"{litrosCoor(lbl_vm_bsf8,ent_temp_acero):.3f}"
    lbl_vm_lt_cr9['text'] = f"{litrosCoor(lbl_vm_bsf9,ent_temp_acero):.3f}"
    lbl_vm_lt_cr10['text'] = f"{litrosCoor(lbl_vm_bsf10,ent_temp_acero):.3f}"


# Calculo del Manhole
frm_form_techo = tk.Frame(master=p5, relief=tk.GROOVE,
                          width=200, height=100, borderwidth=3)
frm_form_techo.pack(side=tk.LEFT, padx=20, pady=10)
frm_titulo_techo = tk.Frame(master=frm_form_techo, borderwidth=3)
frm_titulo_techo.pack()
label_techo = tk.Label(master=frm_titulo_techo, text="CALCULO DEL MANHOLE")
label_techo.pack()
frm_techo = tk.Frame(master=frm_form_techo, width=200,
                     height=100, borderwidth=3)
frm_techo.pack(side=tk.LEFT, padx=20, pady=10)
# Labels para calculo del manhole
lbl_vol_techo = tk.Label(master=frm_techo, text="Circunf. [m]:")
lbl_vol_techo.grid(row=0, column=0)
ent_circ_manhole = tk.Entry(master=frm_techo, width=10)
ent_circ_manhole.grid(row=0, column=1)
lbl_alt_techo = tk.Label(master=frm_techo, text="Longitud [m]:")
lbl_alt_techo.grid(row=1, column=0)
ent_lon_manhole = tk.Entry(master=frm_techo, width=10)
ent_lon_manhole.grid(row=1, column=1)
lbl_techo_incr = tk.Label(master=frm_techo, text="Espesor [m]:")
lbl_techo_incr.grid(row=2, column=0)
ent_esp_manhole = tk.Entry(master=frm_techo, width=10)
ent_esp_manhole.grid(row=2, column=1)
# Resultados calculo del manhole
lbl_dia_int = tk.Label(master=frm_techo, text="Dia. Int [m]:")
lbl_dia_int.grid(row=3, column=0)
lbl_total_vol = tk.Label(master=frm_techo, text="Total Vol. [Litros]:")
lbl_total_vol.grid(row=4, column=0)
lbl_lt_cm = tk.Label(master=frm_techo, text="Litros/cm:")
lbl_lt_cm.grid(row=5, column=0)
lbl_result_dia_int = tk.Label(master=frm_techo)
lbl_result_dia_int.grid(row=3, column=1)
lbl_result_total_vol = tk.Label(master=frm_techo)
lbl_result_total_vol.grid(row=4, column=1)
lbl_result_lt_cm = tk.Label(master=frm_techo)
lbl_result_lt_cm.grid(row=5, column=1)

# TABLA DE AFORO FINAL


def listaTablaFinal():
    lt1 = float(ent_altura_base_inicial_cm0.get())
    cm1 = float(ent_alt1.get())
    cm2 = float(ent_alt2.get())
    cm3 = float(ent_alt3.get())
    cm4 = float(ent_alt4.get())
    cm5 = float(ent_alt5.get())
    cm6 = float(ent_alt6.get())
    cm7 = float(ent_alt7.get())
    cm8 = float(ent_alt8.get())
    cm9 = float(ent_alt9.get())
    cm10 = float(ent_alt10.get())
    centimetro1 = float(ent_alt2.get())
    centimetro2 = float(ent_alt3.get())
    centimetro3 = float(ent_alt4.get())
    centimetro4 = float(ent_alt5.get())
    centimetro5 = float(ent_alt6.get())
    centimetro6 = float(ent_alt7.get())
    centimetro7 = float(ent_alt8.get())
    centimetro8 = float(ent_alt9.get())
    centimetro9 = float(ent_alt10.get())
    centimetro10 = 0
    lt_cm1 = float(lbl_vm_lt_cr2['text'])
    lt_cm2 = float(lbl_vm_lt_cr3['text'])
    lt_cm3 = float(lbl_vm_lt_cr4['text'])
    lt_cm4 = float(lbl_vm_lt_cr5['text'])
    lt_cm5 = float(lbl_vm_lt_cr6['text'])
    lt_cm6 = float(lbl_vm_lt_cr7['text'])
    lt_cm7 = float(lbl_vm_lt_cr8['text'])
    lt_cm8 = float(lbl_vm_lt_cr9['text'])
    lt_cm9 = float(lbl_vm_lt_cr10['text'])
    lt_cm10 = 0
    lt2 = lt1 + (centimetro1-cm1)*lt_cm1
    lt3 = lt2 + (centimetro2-cm2)*lt_cm2
    lt4 = lt3 + (centimetro3-cm3)*lt_cm3
    lt5 = lt4 + (centimetro4-cm4)*lt_cm4
    lt6 = lt5 + (centimetro5-cm5)*lt_cm5
    lt7 = lt6 + (centimetro6-cm6)*lt_cm6
    lt8 = lt7 + (centimetro7-cm7)*lt_cm7
    lt9 = lt8 + (centimetro8-cm8)*lt_cm8
    lt10 = lt9 + (centimetro9-cm9)*lt_cm9
    litros = [lt1, lt2, lt3, lt4, lt5, lt6, lt7, lt8, lt9, lt10]
    cms = [cm1, cm2, cm3, cm4, cm5, cm6, cm7, cm8, cm9, cm10]
    lt_cms = [lt_cm1, lt_cm2, lt_cm3, lt_cm4, lt_cm5,
              lt_cm6, lt_cm7, lt_cm8, lt_cm9, lt_cm10]
    centimetros = [centimetro1, centimetro2, centimetro3, centimetro4, centimetro5,
                   centimetro6, centimetro7, centimetro8, centimetro9, centimetro10]
    return litros, cms, lt_cms, centimetros


def rings_reducer(acc, curr, from_height, rings_height, lts_cms_net, altura):
    index, value = curr
    if index + 1 == len(rings_height):
        # last ring
        return acc
    if value < from_height and rings_height[index + 1] < from_height:
        print(f"skipped index: {index} (too low)")
        return acc
    if altura > value:
        # pending rings
        start = value
        end = altura
        if value < from_height:
            start = from_height
        if altura > rings_height[index + 1]:
            end = rings_height[index + 1]
        print(
            f"applied index: {index}\tvalue: {value}\tlts_cms: {lts_cms_net[index]}")
        print(
            f"with height: {end - start}\tend: {end}\tstart: {start}\n")
        return acc + (end - start) * lts_cms_net[index]
    return acc


def calculoLitros(litros, cms, lt_cms, centimetros, altura):
    lts = 0
    if altura < cms[9]:
        for i in range(0, len(litros)):
            if (altura > cms[i] and altura <= centimetros[i]):
                lt = litros[i]+(altura-cms[i])*lt_cms[i]
                lts += lt
    else:
        rings_height = [float(lbl_result_col_incr1["text"]),
                        float(lbl_result_col_incr2["text"]),
                        float(lbl_result_col_incr3["text"]),
                        float(lbl_result_col_incr4["text"]),
                        float(lbl_result_col_incr5["text"]),
                        float(lbl_result_col_incr6["text"]),
                        float(lbl_result_col_incr7["text"]),
                        float(lbl_result_col_incr8["text"]),
                        float(lbl_result_col_incr9["text"]),
                        float(lbl_result_col_incr10["text"])]
        lts_cms_net = [float(lbl_result_cor_dil1["text"]),
                       float(lbl_result_cor_dil2["text"]),
                       float(lbl_result_cor_dil3["text"]),
                       float(lbl_result_cor_dil4["text"]),
                       float(lbl_result_cor_dil5["text"]),
                       float(lbl_result_cor_dil6["text"]),
                       float(lbl_result_cor_dil7["text"]),
                       float(lbl_result_cor_dil8["text"]),
                       float(lbl_result_cor_dil9["text"]),
                       float(lbl_result_cor_dil10["text"])]
        lts = litros[9] + functools.reduce(lambda acc,
                                           curr: rings_reducer(acc, curr, cms[9], rings_height, lts_cms_net, altura), enumerate(rings_height), 0)
    return lts


frm_form_aforo = tk.Frame(master=p9, relief=tk.GROOVE,
                          width=100, height=100, borderwidth=3)
frm_form_aforo.pack(fill=tk.X, padx=20, pady=10)
frm_titulo_aforo = tk.Frame(master=frm_form_aforo, borderwidth=3)
frm_titulo_aforo.pack(fill=tk.X)
label_aforo = tk.Label(master=frm_titulo_aforo, text="Altura vs. Volumen")
label_aforo.pack(fill=tk.X)
frm_aforo_final = tk.Frame(master=frm_form_aforo,
                           width=100, height=100, borderwidth=3)
frm_aforo_final.pack(fill=tk.X, padx=20, pady=10)
# Labels tabla de aforo final
lbl_tf_altura = tk.Label(master=frm_aforo_final, text="Altura [cm]")
lbl_tf_altura.grid(row=0, column=0)
ent_altura = tk.Entry(master=frm_aforo_final)
ent_altura.grid(row=1, column=0)
lbl_incr_lt = tk.Label(master=frm_aforo_final, text="Litros")
lbl_incr_lt.grid(row=0, column=1)
result_lb_lt = tk.Label(master=frm_aforo_final)
result_lb_lt.grid(row=1, column=1)
lbl_incr_gal = tk.Label(master=frm_aforo_final, text="Galones")
lbl_incr_gal.grid(row=0, column=2)
result_lb_gal = tk.Label(master=frm_aforo_final)
result_lb_gal.grid(row=1, column=2)


def mostrarTablaFinal():
    altura = float(ent_altura.get())
    litros, cms, lt_cms, centimetros = listaTablaFinal()
    litros_finales = calculoLitros(litros, cms, lt_cms, centimetros, altura)
    result_lb_lt["text"] = f"{litros_finales:.3f}"  # /3.78541
    galones_finales = litros_finales/3.78541
    result_lb_gal["text"] = f"{galones_finales:.3f}"


# Creacion de botones para guardar informacion
frm_buttons7 = tk.Frame(master=p7)
frm_buttons7.pack(fill=tk.X, ipadx=5, ipady=5)

btn_submit7 = tk.Button(master=frm_buttons7,
                        text="Mostrar", command=corrAnillos)
btn_submit7.pack(padx=10, ipadx=10)

# Creacion de botones para guardar informacion
frm_buttons8 = tk.Frame(master=p8)
frm_buttons8.pack(fill=tk.X, ipadx=5, ipady=5)

btn_submit8 = tk.Button(master=frm_buttons8,
                        text="Mostrar", command=mostrarCorreciones)
btn_submit8.pack(padx=10, ipadx=10)

# Creacion de botones para guardar informacion
frm_buttons9 = tk.Frame(master=p9)
frm_buttons9.pack(fill=tk.X, ipadx=5, ipady=5)

btn_submit9 = tk.Button(master=frm_buttons9,
                        text="Mostrar", command=mostrarTablaFinal)
btn_submit9.pack(padx=10, ipadx=10)

# Creacion de botones para guardar informacion
frm_buttons3 = tk.Frame(master=p3)
frm_buttons3.pack(fill=tk.X, ipadx=5, ipady=5)

btn_submit3 = tk.Button(master=frm_buttons3,
                        text="Mostrar", command=promedioCirc)
btn_submit3.pack(side=tk.LEFT, padx=10, ipadx=10)

# Creacion de botones para guardar informacion
frm_buttons4 = tk.Frame(master=p4)
frm_buttons4.pack(fill=tk.X, ipadx=5, ipady=5)

btn_submit4 = tk.Button(master=frm_buttons4, text="Mostrar", command=alturas)
btn_submit4.pack(side=tk.LEFT, padx=10, ipadx=10)

# Creacion de botones para guardar informacion
frm_buttons5 = tk.Frame(master=p5)
frm_buttons5.pack(fill=tk.X, ipadx=5, ipady=5)

btn_submit5 = tk.Button(master=frm_buttons5, text="Mostrar", command=vmuerto)
btn_submit5.pack(side=tk.LEFT, padx=10, ipadx=10)

# Start the application
window.mainloop()
