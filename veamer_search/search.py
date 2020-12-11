from flask import Flask, jsonify, request
import requests
app = Flask(__name__)


def get_data(parameters):
	#payload= {"key":"sholay"}
	resp = requests.get('http://manage:5000/get_data',params=parameters)
	return resp.json()




@app.route("/",methods=['GET','POST'])
def hello():
	if request.method == 'POST':
		#json_ = request.get_json()
		return jsonify({"message":"uri : /search, params: key(keyword to be searched) method GET"}),201
	else:
		return jsonify({"message":"uri : /search, params: key(keyword to be searched) method GET"}),201






@app.route("/search",methods=['GET'])
def search():
	parameters = request.args
	res = get_data(parameters)
	#print(parameters)
	return res,200



def main():
	app.run(debug=True,host='0.0.0.0' , port=5001)

if __name__ == '__main__':
	main()




	