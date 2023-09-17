from flask import Flask, request, jsonify
from utils import convertListToObject
import sqlite3

connect = sqlite3.connect('mydatabase.db')
connect.execute(
    'CREATE TABLE IF NOT EXISTS Persons (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT)')

app = Flask(__name__)

@app.route('/api', methods=['POST'])
def create_person():
    data = request.json
    name = data["name"]
    
    with sqlite3.connect("mydatabase.db") as users:
        cursor = users.cursor()
        cursor.execute("INSERT INTO Persons (name) VALUES (?)", (name,))
        users.commit()

        # Fetch the last inserted id and store it in the response
        last_id = cursor.lastrowid

    
    return jsonify({'message': 'Person created successfully', 'id': last_id}), 201

@app.route('/api/<int:user_id>', methods=['GET'])
def get_person(user_id):
    try:
        # Establish a connection to the SQLite database
        connection = sqlite3.connect('mydatabase.db')
        cursor = connection.cursor()

        # Use a parameterized query to fetch the person's data by user_id
        cursor.execute("SELECT id, name FROM Persons WHERE id = ?", (user_id,))
        person = cursor.fetchone()

        # Check if a person with the given user_id was found
        if person:
            # Create a dictionary to represent the person's data
            person_dict = {
                "id": person[0],
                "name": person[1]
            }
            return jsonify({"person": person_dict}), 200
        else:
            return jsonify({"message": "Person not found"}), 404
        
    except sqlite3.Error as e:
        # Handle any potential database errors here
        return jsonify({"error": str(e)}), 500

@app.route('/api/', methods=['GET'])
def get_all_persons():
    try:
        # Establish a connection to the SQLite database
        connection = sqlite3.connect('mydatabase.db')
        cursor = connection.cursor()

        # Execute the SQL query to retrieve all persons
        cursor.execute("SELECT id, name FROM Persons")
        persons = cursor.fetchall()

        # Create a list of dictionaries representing the persons
        result = [{"id": p[0], "name": p[1]} for p in persons]

        # Close the database connection
        connection.close()

        return jsonify({"result": result}), 200
    except sqlite3.Error as e:
        # Handle any potential database errors here
        return jsonify({"error": str(e)}), 500


@app.route('/api/<int:user_id>', methods=['PUT'])
def update_person(user_id):
    try:
        # Establish a connection to the SQLite database
        connection = sqlite3.connect('mydatabase.db')
        cursor = connection.cursor()

        # Retrieve the updated data from the request JSON
        data = request.json
        new_name = data.get('name')

        # Check if the person with the specified user_id exists
        cursor.execute("SELECT id FROM Persons WHERE id = ?", (user_id,))
        person = cursor.fetchone()

        if person:
            # Update the person's information in the database
            cursor.execute("UPDATE Persons SET name = ? WHERE id = ?", (new_name, user_id))
            connection.commit()
            return jsonify({'message': 'Person updated successfully'}), 200
        else:
            return jsonify({'message': 'Person not found'}), 404

    except sqlite3.Error as e:
        # Handle any potential database errors here
        return jsonify({"error": str(e)}), 500

@app.route('/api/<int:user_id>', methods=['DELETE'])
def delete_person(user_id):
    try:
        # Establish a connection to the SQLite database
        connection = sqlite3.connect('mydatabase.db')
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

if __name__ == '__main__':
    app.run(debug=True)
