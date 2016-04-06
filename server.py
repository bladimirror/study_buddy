from flask import Flask, request, render_template, redirect, session, flash
#from mysqlconnection import MySQLConnector

app = Flask(__name__)
app.secret_key = 'secret_key_shhhh'
#mysql = MySQLConnector('study_buddy_db')

#INDEX PAGE
@app.route('/')
def index():
	return render_template('index.html')

