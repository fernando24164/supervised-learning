from backend import model
from flask import Blueprint, jsonify, request

api = Blueprint('api', __name__, url_prefix='/api')


def to_2d_array(arr):
    return [arr[i:i+1] for i in range(0, len(arr), 1)]


def flatten(arr):
    return[item for sublist in arr for item in sublist]


@api.route('/predict', methods=['POST'])
def predict():
    points_to_predict = request.get_json().get('points', "")
    points = to_2d_array(points_to_predict)
    prediction = model.predict(points)
    answer = flatten(prediction)
    return jsonify(response=answer)
