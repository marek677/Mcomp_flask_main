from flask import Flask, g, make_response, Blueprint
from flask import Flask, flash, redirect, render_template, request, session, abort
import os
import sys


app = Flask(__name__,static_url_path='/static')
@app.route('/json/<filename>')
def generate_json(filename):
	#this is temporary
	with open(filename+".json") as f:
		return f.read()
#default
@app.route('/')
def home():
	return render_template('my_example.html')

if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True,host='0.0.0.0', port=4000)
