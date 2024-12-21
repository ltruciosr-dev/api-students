# README: Student Management System

This project is a basic **Student Management System** built using Python, SQLite, and Flask. It provides APIs to perform CRUD operations on a student database and includes a script for creating the database schema.

---

## Features

1. **Database Schema Initialization**
   - Script to create the `students` table in an SQLite database.

2. **RESTful API**
   - Endpoints to manage student records (Create, Read, Update, Delete).
   - JSON-based communication.

---

## Prerequisites

Ensure you have the following installed:
- Python 3.x
- SQLite

---

## Installation and Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-repo/student-management.git
   cd student-management
   ```

2. **Set Up the Database**
   Run the `create_students_table.py` script to initialize the SQLite database:
   ```bash
   python create_students_table.py
   ```

3. **Start the Flask Application**
   Run the `app.py` script to start the API server:
   ```bash
   python app.py
   ```

   The server will be available at `http://127.0.0.1:8000`.

---

## Endpoints

### 1. **GET /students**
   - Fetch all student records.
   - **Response Example:**
     ```json
     [
         {
             "id": 1,
             "firstname": "John",
             "lastname": "Doe",
             "gender": "Male",
             "age": "21"
         }
     ]
     ```

### 2. **POST /students**
   - Add a new student record.
   - **Request Form Data:**
     - `firstname`: First name of the student.
     - `lastname`: Last name of the student.
     - `gender`: Gender of the student.
     - `age`: Age of the student.

   - **Response Example:**
     ```plaintext
     Student with id: 1 created successfully
     ```

### 3. **GET /student/<id>**
   - Fetch details of a specific student by ID.
   - **Response Example:**
     ```json
     {
         "id": 1,
         "firstname": "John",
         "lastname": "Doe",
         "gender": "Male",
         "age": "21"
     }
     ```

### 4. **PUT /student/<id>**
   - Update details of a specific student.
   - **Request Form Data:**
     - `firstname`: Updated first name.
     - `lastname`: Updated last name.
     - `gender`: Updated gender.
     - `age`: Updated age.

   - **Response Example:**
     ```json
     {
         "id": 1,
         "firstname": "Jane",
         "lastname": "Doe",
         "gender": "Female",
         "age": "22"
     }
     ```

### 5. **DELETE /student/<id>**
   - Delete a student record by ID.
   - **Response Example:**
     ```plaintext
     Student with id: 1 has been deleted.
     ```

---

## File Structure

- **`create_students_table.py`**
  - Script to initialize the SQLite database and create the `students` table.

- **`app.py`**
  - Flask application with RESTful endpoints for student management.

---

## License

This project is open-source and available under the [MIT License](LICENSE).

---

## Acknowledgments

This system is a simple demonstration of how to:
- Use SQLite for lightweight data storage.
- Create RESTful APIs with Flask.
- Perform CRUD operations programmatically.
