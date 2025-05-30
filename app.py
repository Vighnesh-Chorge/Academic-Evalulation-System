from flask import Flask, render_template, request, redirect, url_for, session
import mysql.connector

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Connect to MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Vighnesh@123",
    database="academic_evaluation"
)
cursor = db.cursor(dictionary=True)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    roll_number = request.form['roll_number']
    semester_marks = request.form['semester_marks']
    assignment_grades = request.form['assignment_grades']

    sql = "INSERT INTO student_data (name, roll_number, semester_marks, assignment_grades) VALUES (%s, %s, %s, %s)"
    val = (name, roll_number, semester_marks, assignment_grades)
    cursor.execute(sql, val)
    db.commit()

    return "Data submitted successfully!"

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username == 'admin' and password == 'admin123':
            session['admin'] = True
            return redirect(url_for('admin_view_students'))
        else:
            return "Invalid credentials. Try again."

    return render_template('login.html')

@app.route('/admin/students')
def admin_view_students():
    if not session.get('admin'):
        return redirect(url_for('login'))

    cursor.execute("SELECT * FROM student_data")
    all_student_data = cursor.fetchall()
    print("Fetched student data:", all_student_data)  # Optional debug print
    return render_template('admin_students.html', students=all_student_data)

@app.route('/logout')
def logout():
    session.pop('admin', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
