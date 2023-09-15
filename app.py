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
    age = data["age"]
    with sqlite3.connect("database.db") as users:
         cursor = users.cursor()
         cursor.execute("INSERT INTO Persons \
                        (name, age) VALUES (?,?)", (name, age))
         print(users.commit())
    return jsonify({'message': 'Person created successfully'}), 201


@app.route('/api/<int:user_id>', methods=['GET'])
def get_person(user_id):
    try:
        # Establish a connection to the SQLite database
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()

        # Use a parameterized query to fetch the person's data by user_id
        cursor.execute("SELECT id, name, age FROM Persons WHERE id = ?", (user_id,))
        person = cursor.fetchone()

        # Check if a person with the given user_id was found
        if person:
            # Create a dictionary to represent the person's data
            person_dict = {
                "id": person[0],
                "name": person[1],
                "age": person[2]
            }
            return jsonify({"person": person_dict}), 200
        else:
            return jsonify({"message": "Person not found"}), 404
        
    except sqlite3.Error as e:
        # Handle any potential database errors here
        return jsonify({"error": str(e)}), 500


# Get all persons
@app.route('/api/', methods=['GET'])
def get_all_persons():
    connect = sqlite3.connect('database.db')
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM Persons")
    person = cursor.fetchall()
    result = list(map(convertListToObject, person))
    return jsonify({"result": result}), 200



# # Update a person by ID
@app.route('/api/<int:user_id>', methods=['PUT'])
def update_person(user_id):
    try:
        # Establish a connection to the SQLite database
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()

        # Retrieve the updated data from the request JSON
        data = request.json
        new_name = data.get('name')
        new_age = data.get('age')

        # Check if the person with the specified user_id exists
        cursor.execute("SELECT id FROM Persons WHERE id = ?", (user_id,))
        person = cursor.fetchone()

        if person:
            # Update the person's information in the database
            cursor.execute("UPDATE Persons SET name = ?, age = ? WHERE id = ?", (new_name, new_age, user_id))
            connection.commit()
            return jsonify({'message': 'Person updated successfully'}), 200
        else:
            return jsonify({'message': 'Person not found'}), 404

    except sqlite3.Error as e:
        # Handle any potential database errors here
        return jsonify({"error": str(e)}), 500

    finally:
        # Make sure to close the database connection when done
        connection.close()

# # Delete a person by ID
@app.route('/api/<int:user_id>', methods=['DELETE'])
def delete_person(user_id):
    try:
        # Establish a connection to the SQLite database
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()

        # Check if the person with the specified user_id exists
        cursor.execute("SELECT id FROM Persons WHERE id = ?", (user_id,))
        person = cursor.fetchone()

        if person:
            # Delete the person from the database
            cursor.execute("DELETE FROM Persons WHERE id = ?", (user_id,))
            connection.commit()
            return jsonify({'message': 'Person deleted successfully'}), 200
        else:
            return jsonify({'message': 'Person not found'}), 404

    except sqlite3.Error as e:
        # Handle any potential database errors here
        return jsonify({"error": str(e)}), 500

    finally:
        # Make sure to close the database connection when done
        connection.close()

def __init__(self, name, age):
        self.name = name
        self.age = age

if __name__ == '__main__':
    # with app.app_context():
        # db.create_all()

    app.run(debug=True)
