from flask import Flask
from flask_restful import Api,Resource,reqparse
from flask_cors import CORS
from flask import jsonify
import os
from datas import getProblem

app = Flask(__name__)
api = Api(app)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
BASE_DIR = os.path.dirname(__file__)
parser = reqparse.RequestParser()
parser.add_argument('name', type=str)

class AlgorithmsAPI(Resource):
    def get(self,name):
        try:
            problemDesc,problemResult = getProblem(name)
            jsonObj = {"left":problemDesc}
            return jsonify(jsonObj)
        except Exception:
            return jsonify({"error":"error"})
    
    def post(self,name):
        try:
            args = parser.parse_args()
            arg_name = eval(args['name'])
            problemDesc,problemResult = getProblem(arg_name)
            jsonObj = {"result":problemResult}
            return jsonify(jsonObj)
        except Exception:
            return jsonify({"error":"error"})

api.add_resource(AlgorithmsAPI, '/api/<name>')

if __name__ == '__main__':
    app.run(debug=True)