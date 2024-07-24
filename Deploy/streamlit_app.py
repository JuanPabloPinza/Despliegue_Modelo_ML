import numpy as np
import streamlit as st
import requests

st.set_page_config(page_title="Sistema de Predicción de Ingresos Anuales", page_icon=":bar_chart:", layout="centered")

# URL del servidor Flask
URL = "http://localhost:5000/predict"

# # Diccionarios de mapeo con su nombre original
# institucion_trabajo_mapping = {
#     "Federal-gov": 0,
#     "Local-gov": 1,
#     "Never-worked": 2,
#     "Private": 3,
#     "Self-emp-inc": 4,
#     "Self-emp-not-inc": 5,
#     "State-gov": 6,
#     "Without-pay": 7
# }

# estudios_mapping = {
#     "10th": 0,
#     "11th": 1,
#     "12th": 2,
#     "1st-4th": 3,
#     "5th-6th": 4,
#     "7th-8th": 5,
#     "9th": 6,
#     "Assoc-acdm": 7,
#     "Assoc-voc": 8,
#     "Bachelors": 9,
#     "Doctorate": 10,
#     "HS-grad": 11,
#     "Masters": 12,
#     "Preschool": 13,
#     "Prof-school": 14,
#     "Some-college": 15
# }

# estado_civil_mapping = {
#     "Divorced": 0,
#     "Married-AF-spouse": 1,
#     "Married-civ-spouse": 2,
#     "Married-spouse-absent": 3,
#     "Never-married": 4,
#     "Separated": 5,
#     "Widowed": 6
# }

# ocupacion_mapping = {
#     "Adm-clerical": 0,
#     "Armed-Forces": 1,
#     "Craft-repair": 2,
#     "Exec-managerial": 3,
#     "Farming-fishing": 4,
#     "Handlers-cleaners": 5,
#     "Machine-op-inspct": 6,
#     "Other-service": 7,
#     "Priv-house-serv": 8,
#     "Prof-specialty": 9,
#     "Protective-serv": 10,
#     "Sales": 11,
#     "Tech-support": 12,
#     "Transport-moving": 13
# }

# relacion_familiar_mapping = {
#     "Married": 0,
#     "Not-in-family": 1,
#     "Other-relative": 2,
#     "Own-child": 3,
#     "Unmarried": 4
# }

# raza_mapping = {
#     "Amer-Indian-Eskimo": 0,
#     "Asian-Pac-Islander": 1,
#     "Black": 2,
#     "Other": 3,
#     "White": 4
# }

# genero_mapping = {
#     "Female": 0,
#     "Male": 1
# }

# pais_mapping = {
#     "Cambodia": 0,
#     "Canada": 1,
#     "China": 2,
#     "Columbia": 3,
#     "Cuba": 4,
#     "Dominican-Republic": 5,
#     "Ecuador": 6,
#     "El-Salvador": 7,
#     "England": 8,
#     "France": 9,
#     "Germany": 10,
#     "Greece": 11,
#     "Guatemala": 12,
#     "Haiti": 13,
#     "Holand-Netherlands": 14,
#     "Honduras": 15,
#     "Hong": 16,
#     "Hungary": 17,
#     "India": 18,
#     "Iran": 19,
#     "Ireland": 20,
#     "Italy": 21,
#     "Jamaica": 22,
#     "Japan": 23,
#     "Laos": 24,
#     "Mexico": 25,
#     "Nicaragua": 26,
#     "Outlying-US(Guam-USVI-etc)": 27,
#     "Peru": 28,
#     "Philippines": 29,
#     "Poland": 30,
#     "Portugal": 31,
#     "Puerto-Rico": 32,
#     "Scotland": 33,
#     "South": 34,
#     "Taiwan": 35,
#     "Thailand": 36,
#     "Trinadad&Tobago": 37,
#     "United-States": 38,
#     "Vietnam": 39,
#     "Yugoslavia": 40
# }
#
# Diccionarios de mapeo pero en español
institucion_trabajo_mapping = {
    "Gobierno Federal": 0,
    "Gobierno Local": 1,
    "Nunca Trabajado": 2,
    "Privado": 3,
    "Auto-empleado Incorporado": 4,
    "Auto-empleado No Incorporado": 5,
    "Gobierno Estatal": 6,
    "Sin Pago": 7
}

estudios_mapping = {
    "Décimo Grado": 0,
    "Undécimo Grado": 1,
    "Duodécimo Grado": 2,
    "Primero a Cuarto Grado": 3,
    "Quinto a Sexto Grado": 4,
    "Séptimo a Octavo Grado": 5,
    "Noveno Grado": 6,
    "Asociado Académico": 7,
    "Asociado Vocacional": 8,
    "Licenciatura": 9,
    "Doctorado": 10,
    "Graduado de Secundaria": 11,
    "Maestría": 12,
    "Preescolar": 13,
    "Profesional": 14,
    "Algo de Universidad": 15
}

estado_civil_mapping = {
    "Divorciado": 0,
    "Casado con AF": 1,
    "Casado Civil": 2,
    "Casado con Esposo Ausente": 3,
    "Nunca Casado": 4,
    "Separado": 5,
    "Viudo": 6
}

ocupacion_mapping = {
    "Administrativo": 0,
    "Fuerzas Armadas": 1,
    "Reparación": 2,
    "Ejecutivo Gerencial": 3,
    "Agricultura Pesca": 4,
    "Manejadores y Limpiadores": 5,
    "Operación de Maquinaria": 6,
    "Otros Servicios": 7,
    "Servicio Doméstico": 8,
    "Profesional": 9,
    "Protección": 10,
    "Ventas": 11,
    "Soporte Técnico": 12,
    "Transporte": 13
}

relacion_familiar_mapping = {
    "Casado": 0,
    "No en Familia": 1,
    "Otro Pariente": 2,
    "Hijo Propio": 3,
    "Soltero": 4
}

raza_mapping = {
    "Indio Americano Esquimal": 0,
    "Isleño Asiático del Pacífico": 1,
    "Negro": 2,
    "Otro": 3,
    "Blanco": 4
}

genero_mapping = {
    "Femenino": 0,
    "Masculino": 1
}

pais_mapping = {
    "Camboya": 0,
    "Canadá": 1,
    "China": 2,
    "Colombia": 3,
    "Cuba": 4,
    "República Dominicana": 5,
    "Ecuador": 6,
    "El Salvador": 7,
    "Inglaterra": 8,
    "Francia": 9,
    "Alemania": 10,
    "Grecia": 11,
    "Guatemala": 12,
    "Haití": 13,
    "Holanda": 14,
    "Honduras": 15,
    "Hong Kong": 16,
    "Hungría": 17,
    "India": 18,
    "Irán": 19,
    "Irlanda": 20,
    "Italia": 21,
    "Jamaica": 22,
    "Japón": 23,
    "Laos": 24,
    "México": 25,
    "Nicaragua": 26,
    "Territorios Lejanos de EE.UU.": 27,
    "Perú": 28,
    "Filipinas": 29,
    "Polonia": 30,
    "Portugal": 31,
    "Puerto Rico": 32,
    "Escocia": 33,
    "Sur de EE.UU.": 34,
    "Taiwán": 35,
    "Tailandia": 36,
    "Trinidad y Tobago": 37,
    "Estados Unidos": 38,
    "Vietnam": 39,
    "Yugoslavia": 40
}


# Valores constantes calculados en base a las gráficas originales
comp1_mean = 189671
comp2_mean = 10     
comp3_mode = 0
comp4_mode = 0

def main():
    # Título
    st.title("SISTEMA DE PREDICCIÓN DE INGRESOS ANUALES")
    st.write("A continuación se le presentan unas constantes que facilitan la predicción:")
    st.write(f"Comp1 (Media): {comp1_mean}")
    st.write(f"Comp2 (Media): {comp2_mean}")
    st.write(f"Comp3 (Moda): {comp3_mode}")
    st.write(f"Comp4 (Moda): {comp4_mode}")
    # Lectura de datos
    edad = st.number_input("Edad:", min_value=0)
    institucion_trabajo = st.selectbox("Institución de Trabajo:", list(institucion_trabajo_mapping.keys()))
    estudios = st.selectbox("Estudios:", list(estudios_mapping.keys()))
    estado_civil = st.selectbox("Estado Civil:", list(estado_civil_mapping.keys()))
    ocupacion = st.selectbox("Ocupación:", list(ocupacion_mapping.keys()))
    relacion_familiar = st.selectbox("Relación Familiar:", list(relacion_familiar_mapping.keys()))
    raza = st.selectbox("Raza:", list(raza_mapping.keys()))
    genero = st.selectbox("Género:", list(genero_mapping.keys()))
    horas_semana = st.number_input("Horas por Semana:", min_value=0)
    pais = st.selectbox("País:", list(pais_mapping.keys()))
    

    
    # El botón predicción se usa para iniciar el procesamiento
    if st.button("Predicción :"): 
        x_in = [
            edad, 
            institucion_trabajo_mapping[institucion_trabajo], 
            comp1_mean, 
            estudios_mapping[estudios], 
            comp2_mean, 
            estado_civil_mapping[estado_civil], 
            ocupacion_mapping[ocupacion], 
            relacion_familiar_mapping[relacion_familiar], 
            raza_mapping[raza], 
            genero_mapping[genero], 
            comp3_mode, 
            comp4_mode, 
            horas_semana, 
            pais_mapping[pais]
        ]
        data = {'features': x_in}
        
        # Hacer la solicitud al servidor Flask
        response = requests.post(URL, json=data)
        
        if response.status_code == 200:
            result = response.json()
            st.success(f'EL RESULTADO DE INGRESOS ANUALES ES: {result["prediction"]}')
        else:
            st.error("Error al realizar la predicción")

if __name__ == '__main__':
    main()
