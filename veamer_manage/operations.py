from flask import jsonify, Flask, request
import sqlite3
import json


def quote_if_string(value): # function to quote string if not all charachters are numeric (needed to make sql query) 
	if value.isnumeric():
		return value
	else:
		return "'" + value + "'"



def makeSqlInsertQuery(json_dict):  # making sql query based on input dictionary 
	sql_string = " INSERT INTO MOVIES "
	params = " ( "
	values = " VALUES ( "
	for key in json_dict.keys():
		params = params + str(key) + ", "
		if (str(json_dict[key])).isnumeric() :
		    values = values + str(json_dict[key]) + ", "
		else:
		    values = values + " '" + str(json_dict[key]) +"' "+ ", "
	    

	params = params[:-2] + " ) "
	values = values[:-2] + " ) "
	sql_string = sql_string + params + values
	return sql_string



def isValidInsert(json_dict):   # checking if valid input is given in json
	attributes=["name","year","description","duration_in_min","cast"]
	for key in json_dict:
		if key not in attributes:
			return False
	return True
	




def insert_data(json_obj):    
	json_dict = json.loads(json.dumps(json_obj))
	if isValidInsert(json_dict):

		if json_dict.__contains__("name") and json_dict.__contains__("year"):
			conn= sqlite3.connect("movies.db")
			sql_string = makeSqlInsertQuery(json_dict)
			#cur=conn.cursor()
			conn.execute(sql_string)
			conn.commit()
			conn.close()
			return jsonify({"message":"insertion successful"}),202
			"""try:
				conn= sqlite3.connect("movies.db")
				sql_string = makeSqlInsertQuery(json_dict)
				conn.execute(sql_string)
				conn.commit()
				conn.close()
				return jsonify({"message":sql_string}),500
			except:
				return jsonify({"message":"internal db error"}),500"""

			# insert
		else:
			return jsonify({"message":"atleast include name and year of the movie"}),206

	else:
		return jsonify({"message":"Invalid attributes in json file"}),205




def search(key):  # search in DB
	conn = sqlite3.connect("movies.db")
	cur = conn.cursor()
	cur.execute("SELECT * FROM MOVIES WHERE (NAME LIKE " + "'%" +key+"%' )")
	rows = cur.fetchall()
	conn.close()
	return rows




def makeSqlUpdateQuery(json_dict):  
	values_dict = json_dict["new_values"]
	sql_string = "UPDATE MOVIES SET "
	values_string = ""
	for key in values_dict:
		values_string = values_string + " " + key + " = " + quote_if_string(values_dict[key]) +", "
	values_string = values_string[:-2]
	sql_string = sql_string + values_string + " WHERE NAME = " + quote_if_string(json_dict["name"]) + " AND YEAR = " + quote_if_string(json_dict["year"]) + ";"
	return sql_string








def isValidUpdate(json_dict):

	if json_dict.__contains__("name") and json_dict.__contains__("year") and json_dict.__contains__("new_values"):
		values_dict = json_dict["new_values"]
		attributes=["name","year","description","cast","duration_in_min"]
		for key in values_dict:
			if key not in attributes:
				return False

		return True


	else:
		return False







def update_data(json_obj):
	json_dict = json.loads(json.dumps(json_obj))
	if isValidUpdate(json_dict):
		if json_dict.__contains__("name") and json_dict.__contains__("year"):
			try:
				conn = sqlite3.connect("movies.db")
				cur  = conn.cursor()
				cur.execute("SELECT * FROM MOVIES WHERE NAME = '" + json_dict["name"] + "' AND " + " YEAR = " + json_dict["year"])
				rows = cur.fetchall()
				if len(rows) < 1:
					conn.close()
					raise IOError("no such movie !")
			
				#conn.close()
				

			except IOError:

				return jsonify({"message":" check - attributes it must have  name and year to uniquely identify a movie and new_values should be amongst [name,year,description,cast,duration_in_min] "}),206
			else:
				cur = conn.cursor()
				cur.execute(makeSqlUpdateQuery(json_dict))
				conn.commit()
				conn.close()
				return jsonify({"message":"update successful","new_values":json_dict["new_values"]}),202

	else:
		return jsonify({"message":" check attributes it must have  name and year to uniquely identify a movie and new_values should be amongst [name,year,description,cast,duration_in_min] "}),206
			



def makeSqlDeleteQuery(json_dict):
	sql_string = "DELETE FROM MOVIES WHERE " + "NAME = " + quote_if_string(json_dict["name"]) + " AND YEAR = " + quote_if_string(json_dict["year"])
	return sql_string


	


def isValidDelete(json_dict):
	if json_dict.__contains__("name") and json_dict.__contains__("year"):
		attributes = ["name","year"]
		for key in json_dict:
			if key not in attributes:
				return False
		if not str(json_dict["year"]).isnumeric():
			return False

		return True
	else:
		return False

	




def delete_data(json_obj):
	json_dict = json.loads(json.dumps(json_obj))
	if isValidDelete(json_dict):
		try:
				conn = sqlite3.connect("movies.db")
				cur  = conn.cursor()
				cur.execute("SELECT * FROM MOVIES WHERE NAME = '" + json_dict["name"] + "' AND " + " YEAR = " + json_dict["year"])
				rows = cur.fetchall()
				if len(rows) < 1:
					conn.close()
					raise IOError("no such movie !")

		except:
				return jsonify({"message":" check - attributes it must have  name and year to be able to delete a record !"}),206


		else:
				cur = conn.cursor()
				cur.execute(makeSqlDeleteQuery(json_dict))
				conn.commit()
				conn.close()
				return jsonify({"message":"Delete successful","Deleted movie with ":json_dict}),202

	else:
		return jsonify({"message":" check - attributes it must have  name and year to be able to delete a record !"}),206
	







