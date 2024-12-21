from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def db_connection():
    try:
        return sqlite3.connect('students.sqlite')
    except sqlite3.error as e:
        print(e)
        return None

@app.route("/students", methods=["GET", "POST"])
def students():
    conn = db_connection()
    cursor = conn.cursor()

    if request.method == "GET":
        cursor.execute("SELECT * FROM students")
        students = [
            dict(id=row[0], firstname=row[1], lastname=row[2], gender=row[3], age=row[4])
            for row in cursor.fetchall()
        ]
        return jsonify(students) if students else jsonify([])

    if request.method == "POST":
        data = request.form
        sql = """INSERT INTO students (firstname, lastname, gender, age) VALUES (?, ?, ?, ?)"""
        cursor.execute(sql, (data["firstname"], data["lastname"], data["gender"], data["age"]))
        conn.commit()
        return f"Student with id: {cursor.lastrowid} created successfully", 201

@app.route('/student/<int:id>', methods=["GET", "PUT", "DELETE"])
def student(id):
    conn = db_connection()
    cursor = conn.cursor()

    if request.method == "GET":
        cursor.execute("SELECT * FROM students WHERE id=?", (id,))
        student = cursor.fetchone()
        return jsonify(dict(id=student[0], firstname=student[1], lastname=student[2], gender=student[3], age=student[4])) if student else ("Student not found", 404)

    if request.method == "PUT":
        data = request.form
        sql = """UPDATE students SET firstname=?, lastname=?, gender=?, age=? WHERE id=?"""
        cursor.execute(sql, (data["firstname"], data["lastname"], data["gender"], data["age"], id))
        conn.commit()
        updated_student = {
            "id": id,
            "firstname": data["firstname"],
            "lastname": data["lastname"],
            "gender": data["gender"],
            "age": data["age"]
        }
        return jsonify(updated_student)

    if request.method == "DELETE":
        cursor.execute("DELETE FROM students WHERE id=?", (id,))
        conn.commit()
        return f"Student with id: {id} has been deleted.", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=False)
