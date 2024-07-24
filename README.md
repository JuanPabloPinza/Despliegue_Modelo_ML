# Despliegue_Modelo_ML
Pinza Zurita | Aplicaciones Basadas del Conocimiento | 14923

# Sistema de Predicción de Ingresos Anuales

Este proyecto implementa un sistema de predicción de ingresos anuales utilizando un modelo SVM con kernel RBF. La aplicación permite a los usuarios ingresar sus datos a través de una interfaz web basada en Streamlit y realiza predicciones utilizando un servidor backend implementado con Flask.

## Requisitos

- Anaconda (para gestionar los entornos)
- Python 3.9

## Configuración del Entorno

### Paso 1: Crear y Activar un Entorno Conda

Primero, crea y activa un nuevo entorno en Anaconda:

conda create --name prediccion_ingresos python=3.9
conda activate prediccion_ingresos


### Paso 2: Instalar las Bibliotecas Necesarias
Instala las bibliotecas necesarias en tu entorno Conda:

conda install flask
conda install -c conda-forge flasgger
conda install -c conda-forge streamlit
conda install scikit-learn
conda install pandas
conda install numpy

### Paso 3: Entrenamiento y Guardado del Modelo
Antes de ejecutar la aplicación, necesitas entrenar y guardar el modelo y el escalador. Ejecuta el siguiente código ModeloFinal.ipynb

### Paso 4: Ejecutar el Servidor Flask
Navega al directorio donde tienes app.py, svm_model_rbf.pkl, y scaler.pkl y ejecuta:

python app.py

### Paso 5: Ejecutar la Aplicación Streamlit
En otra terminal, navega al directorio donde tienes streamlit_app.py y ejecuta:

streamlit run streamlit_app.py

### Estructura del Proyecto
.
├── app.py
├── databaseFinal.csv
├── README.md
├── scaler.pkl
├── streamlit_app.py
├── svm_model_rbf.pkl
└── train_model.py


### Notas:
Asegúrate de tener el archivo databaseFinal.csv en el directorio correcto antes de ejecutar train_model.py.
La aplicación Streamlit se abrirá en tu navegador predeterminado una vez que la ejecutes.
Puedes acceder a la documentación Swagger del servidor Flask en http://localhost:5000/apidocs.
