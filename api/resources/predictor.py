from flask_restful import request, reqparse, abort, Resource
import numpy as np
import os, ast
from resources import ml_model

def predict(features):
    n = len(features)
    features = np.array(features)
    features = features.astype(float)

    _class = int(ml_model.predict([features])[0])
    print(type(_class))
    output = {'class': _class}
    return output

class PredictorResource(Resource):
    def get(self):
        # http://localhost:5000/predict?features=...
        args = request.args

        features = args['features']
        features = ast.literal_eval(features) 
        output = predict(features)
        return output

