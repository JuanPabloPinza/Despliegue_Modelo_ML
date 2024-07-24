from flask import Flask, request, jsonify
from flasgger import Swagger, swag_from
import joblib
import numpy as np

app = Flask(__name__)
swagger = Swagger(app)

# Cargar el modelo
model = joblib.load('svm_model_rbf.pkl')

# Cargar el normalizador
scaler = joblib.load('scaler.pkl')

@app.route('/predict', methods=['POST'])
@swag_from({
    'summary': 'Realiza una predicción de ingresos anuales',
    'description': 'Proporciona los parámetros necesarios para realizar una predicción de ingresos anuales utilizando un modelo SVM con kernel RBF.',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'features': {
                        'type': 'array',
                        'items': {
                            'type': 'number'
                        },
                        'example': [50, 5, 83311, 9, 13, 2, 3, 0, 4, 1, 0, 0, 13, 38]
                    }
                }
            }
        }
    ],
    'responses': {
        '200': {
            'description': 'Resultado de la predicción',
            'schema': {
                'type': 'object',
                'properties': {
                    'prediction': {
                        'type': 'integer'
                    }
                }
            }
        }
    }
})
def predict():
    """Endpoint para predecir ingresos anuales"""
    data = request.get_json()
    input_data = np.array([data['features']])
    input_data_scaled = scaler.transform(input_data)
    prediction = model.predict(input_data_scaled)
    return jsonify({'prediction': int(prediction[0])})

if __name__ == '__main__':
    app.run(debug=True)
