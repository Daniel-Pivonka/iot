from flask import Flask, request, json
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
	def post(self):
		value = request.get_data()
		value = json.loads(value)
		return {'hello':value['user']}

api.add_resource(HelloWorld, '/test')

app.run(host='0.0.0.0', debug=True)