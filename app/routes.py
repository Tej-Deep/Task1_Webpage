from flask import render_template
from app import application

@application.route('/')
@application.route('/index')
def index():
    return render_template('index.html', title='2D 10.020 Data Driven World Home')

@application.route('/task1')
def Task1():
    return render_template('task1.html', title='2D 10.020 Data Driven World Task 1')

@application.route('/task2')
def Task2():
    return render_template('task2.html', title='2D 10.020 Data Driven World Task 2')