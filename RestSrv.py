from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS
from time import strftime

app = Flask(__name__)
CORS(app)
api = Api(app)

class Time(Resource):
	def get(self):
		return {'time': strftime("%a, %d %b %Y %H:%M:%S +0000")} 

class Ping(Resource):
	def get(self):
		return {'ping': "Ping!"} 
		
class Calc(Resource):
	def get(self):
		args = request.args
		num1 = float(args['num1'])
		num2 = float(args['num2'])
		return {'result': str(num1+num2)} 
		
api.add_resource(Time, '/time') 
api.add_resource(Ping, '/ping') 
api.add_resource(Calc, '/calc') 

if __name__ == '__main__':
	app.run(port='5002')
	