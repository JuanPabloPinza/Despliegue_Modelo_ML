import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
import joblib

# Cargar el dataset
data = pd.read_csv('databaseFinal.csv')

# Separar características y etiquetas
X = data.drop(columns=['ingresos-anuales'])
y = data['ingresos-anuales']

# Dividir el dataset en conjunto de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Normalizar las características
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Crear y entrenar el modelo SVM con kernel RBF
model_rbf = SVC(kernel='rbf', random_state=42)
model_rbf.fit(X_train_scaled, y_train)

# Guardar el modelo y el escalador
joblib.dump(model_rbf, 'svm_model_rbf.pkl')
joblib.dump(scaler, 'scaler.pkl')
