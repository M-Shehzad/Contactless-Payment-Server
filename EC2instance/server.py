from flask import Flask, redirect, url_for, request
import numpy as np
import json
import tensorflow as tf

app = Flask(__name__)

model = tf.keras.models.load_model('./0000001')

@app.route('/predict', methods=['POST'])
def predict():
    
    # print(request.get_json())
    data = request.get_json()
    data = np.array(data['image'])
    data.reshape(-1,150,150,1)
    print(data.shape)
    prediction = model.predict(data)
    print(type(prediction))
    return json.dumps({'prediction': prediction.tolist()})

if __name__ == '__main__':
    app.run(debug=True)