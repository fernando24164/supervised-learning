from webapp.backend import model
from flask import Blueprint, jsonify, request

api = Blueprint('api', __name__, url_prefix='/api')


@api.route('/predict', methods=['GET', 'POST'])
def predict():
    prediction = model.predict([[76], [77], [78]])
    return jsonify(predict_value_76=int(prediction[0]),
                   predict_value_77=int(prediction[1]),
                   predict_value_78=int(prediction[2]))
