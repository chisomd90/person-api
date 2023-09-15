from flask import Flask, request, jsonify
from model import db, Person

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.sqlite3'
db.init_app(app)

# Create a new person
@app.route('/api', methods=['POST'])
def create_person():
    data = request.json
    new_person = Person(name=data['name'], age=data['age'])
    db.session.add(new_person)
    db.session.commit()
    return jsonify({'message': 'Person created successfully'}), 201

# Read a person by ID
@app.route('/api/<int:user_id>', methods=['GET'])
def get_person(user_id):
    person = Person.query.get_or_404(user_id)
    return jsonify({'name': person.name, 'age': person.age})

# # Read a person by ID
# @app.route('/api/', methods=['GET'])
# def get_all_persons():
#     person = Person.query.filterBy().
#     print(person)
#     return jsonify({'test': 'true'})

# Update a person by ID
@app.route('/api/<int:user_id>', methods=['PUT'])
def update_person(user_id):
    person = Person.query.get_or_404(user_id)
    data = request.json
    person.name = data['name']
    person.age = data['age']
    db.session.commit()
    return jsonify({'message': 'Person updated successfully'})

# Delete a person by ID
@app.route('/api/<int:user_id>', methods=['DELETE'])
def delete_person(user_id):
    person = Person.query.get_or_404(user_id)
    db.session.delete(person)
    db.session.commit()
    return jsonify({'message': 'Person deleted successfully'})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
