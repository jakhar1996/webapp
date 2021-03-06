from flask import Flask, render_template, url_for, request, redirect
from flask_pymongo import PyMongo
import re


app = Flask(__name__)

app.config[ "MONGO_DBNAME" ] = "web_app"
app.config[ 'MANGO_URI'] = "mongodb://localhost:27017/web_app"


mongo = PyMongo(app)

		
@app.route('/send')
def links():
	return render_template ('form.html')


@app.route('/send', methods=['POST'])
def send():
	url = request.form['URL']
	users = mongo.db.allLinks

	match = re.search(r"\w\w\w\.\w+\.\.*" , url) 
	match_https = re.search(r"https|http\://\w+\.\.*" , url) 
	match_simp = re.search(r"\w+\.\w+" , url)

	if match:
		users.insert({"Link" : request.form['URL']})
		return render_template ('form_success.html')
	elif match_https:
		users.insert({"Link" : request.form['URL']})
		return render_template ('form_success.html')

	elif match_simp:
		users.insert({"Link" : request.form['URL']})
		return render_template ('form_success.html')
	
	else:
		print "not found"
		return render_template ('form_error.html')

@app.route('/lists')
def collection():
	res = '';
	users = mongo.db.allLinks
	for item in users.find():
		res += str(item.get('Link')) + "<br />"

	return res




if __name__== '__main__':
	app.run(debug=True)