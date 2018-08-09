from databases import *
from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html', students=query_all())

@app.route('/add_student_route',methods=['GET', 'POST'])
def add():
	if request.method == 'GET' :
		return render_template('add.html')
	else:
		name = request.form['student_name']
 		year = request.form['student_year']
 		add_student(name,year)
		return render_template('result.html', 
			n=name,
		    y=year)
		print ("TAMARA IS Y2")

@app.route('/student/<int:student_id>')
def display_student(student_id):
    return render_template('student.html', student=query_by_id(student_id))


# def save_vote(): 
# 	if request.method == 'GET'
# 		return render_template('add.html')
# 	else:
# 		name = request.form['student_name']
# 		year = request.form['student_year']

# 		save_to_satabase(name, year)
# 		return render_template('home.html')
# 		n=name
# 		y=year
		




app.run(debug=True)
