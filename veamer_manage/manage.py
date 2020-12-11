from flask import Flask, jsonify, request
from operations import insert_data,search, update_data, delete_data
app = Flask(__name__)


@app.route("/",methods=['GET','POST'])
def hello():
	if request.method == 'POST':
		#json_ = request.get_json()
		return jsonify({"message":"uri : /get_data, params: key(keyword to be searched) method GET.  /insert POST,/update POST, /delete POST"}),201
	else:
		return jsonify({"message":"uri : /get_data, params: key(keyword to be searched) method GET.  /insert POST,/update POST, /delete POST"}),201



# insert a record in movies db - input json

@app.route("/insert",methods=['GET','POST'])
def insert():
	if request.method == 'POST':
		json_ = request.get_json()
		result_json = insert_data(json_)   # defined in operations.py
		return result_json




# return data in json format to the caller which matches key
@app.route("/get_data",methods=['GET'])
def get_data():
	params=request.args
	res = search(params["key"])  # defined in operations.py
	return jsonify({"result":res})



#update data in db,  we need json input
@app.route("/update",methods=['POST'])
def update():
	json_ = request.get_json()
	result_json = update_data(json_)      # defined in operations.py
	return result_json


#input needed in json
@app.route("/delete",methods=['POST'])
def delete():
	json_ = request.get_json()
	result_json = delete_data(json_)      # defined in operations.py
	return result_json 



def main():
	app.run(host ='0.0.0.0', port = 5000, debug = True)


if __name__ == '__main__':
	main()
	
