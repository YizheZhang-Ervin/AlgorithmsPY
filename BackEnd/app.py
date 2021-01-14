from flask import Flask
from flask_restful import Api,Resource,reqparse
from flask_cors import CORS
from flask import jsonify
import os

app = Flask(__name__)
api = Api(app)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
BASE_DIR = os.path.dirname(__file__)
parser = reqparse.RequestParser()
parser.add_argument('params', type=str)

class AlgorithmsAPI(Resource):
    def get(self,pkg):
        try:
            jsonObj = {"result":"new "+pkg}
            return jsonify(jsonObj)
        except Exception:
            return jsonify({"error":"error"})
    
    def post(self,pkg):
        try:
            args = parser.parse_args()
            arg_name = eval(args['params'])
            jsonObj = {"result":"new "+str(arg_name)}
            return jsonify(jsonObj)
        except Exception:
            return jsonify({"error":"error"})

api.add_resource(AlgorithmsAPI, '/api/<pkg>')

if __name__ == '__main__':
    app.run(debug=True)