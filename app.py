from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from utils import convertListToObject
import sqlite3

connect = sqlite3.connect('database.db')
connect.execute(
    'CREATE TABLE IF NOT EXISTS Persons (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, age TEXT)')



app = Flask(__name__)

# Create a new person
@app.route('/api', methods=['POST'])
def create_person():
    data = request.json
    name = data["name"]
    age=data["age"]
    with sqlite3.connect("database.db") as users:
         cursor = users.cursor()
         cursor.execute("INSERT INTO Persons \
                        (name, age) VALUES (?,?)", (name, age))
         print(users.commit())
    return jsonify({'message': 'Person created successfully'}), 201

# Read a person by ID
@app.route('/api/<int:user_id>', methods=['GET'])
def get_person(user_id):
    # id = int(user_id)
    connect = sqlite3.connect('database.db')
    cursor = connect.cursor()
    cursor.execute("SELECT cast(id as integer) FROM Persons WHERE id = id")
    person = cursor.fetchall()
    print(person)
    # result = list(map(convertListToObject, person))
    return jsonify({"result": 'result'}), 200

# Get all persons
@app.route('/api/', methods=['GET'])
def get_all_persons():
    connect = sqlite3.connect('database.db')
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM Persons")
    person = cursor.fetchall()
    result = list(map(convertListToObject, person))
    return jsonify({"result": result}), 200

# Update a person by ID
@app.route('/api/<int:user_id>', methods=['PUT'])
def update_person(user_id):
    # person = Person.query.get_or_404(user_id)
    data = request.json
    # person.name = data['name']
    # person.age = data['age']
    # db.session.commit()
    return jsonify({'message': 'Person updated successfully'})

# Delete a person by ID
@app.route('/api/<int:user_id>', methods=['DELETE'])
def delete_person(user_id):
    # person = Person.query.get_or_404(user_id)
    # db.session.delete(person)
    # db.session.commit()
    return jsonify({'message': 'Person deleted successfully'})

def __init__(self, name, age):
        self.name = name
        self.age = age

if __name__ == '__main__':
    # with app.app_context():
        # db.create_all()

    app.run(debug=True)
