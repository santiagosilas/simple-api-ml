from flask import Flask
from flask_restful import Api
from resources.predictor import PredictorResource

app = Flask(__name__)
app.config.from_object('config')

api = Api(app)
api.add_resource(PredictorResource, '/predict')

if __name__ == '__main__':
    app.run(debug=True, port = 5000)