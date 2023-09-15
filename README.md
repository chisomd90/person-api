
# Person API

The Person API is a simple RESTful API that allows you to perform CRUD (Create, Read, Update, Delete) operations on person records. This README provides instructions on setting up, running, and using the API.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
  - [Installation](#installation)
  - [Configuration](#configuration)
- [Running the API](#running-the-api)
- [API Endpoints](#api-endpoints)
  - [Create a Person](#create-a-person)
  - [Retrieve a Person](#retrieve-a-person)
  - [Update a Person](#update-a-person)
  - [Delete a Person](#delete-a-person)
- [Testing the API](#testing-the-api)
- [Contributing](#contributing)
- [License](#license)

### Prerequisites

Before you begin, ensure you have the following:

- Python 3.6+
- pip (Python package manager)
- [Flask](https://flask.palletsprojects.com/en/2.1.x/)
- [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/3.x/)
- MySQL (or an alternative database, based on your choice)

## Getting Started

### Installation

1. Clone this repository to your local machine:
git clone https://github.com/yourusername/person-api.git ------- Navigate to the project directory:


cd person-api ------- Install the required Python packages:
pip install -r requirements.txt


### Running the API
Ensure your database is set up and running.

Run the following command to create the database tables:


python create_db.py ------ Start the API server:


python app.py -------- The API should now be running locally at http://localhost:5000.

### API Endpoints

  ## Create a Person
Endpoint: POST /api

Description: Create a new person with the given name.

Request Body: JSON data containing person details (name, age, email).

Example Request: 
  curl -X POST http://localhost:5000/api/John%20Doe -H "Content-Type: application/json" -d 
  ```json
  '{
  "name": "Chisom Daniel",
  "age": 30,
}'
```

  ## Retreive a person
Endpoint: GET /api/<int:user_id>

Description: Retrieve details of a person with the given name.

Example Request:
  curl http://localhost:5000/api/John%20Doe

  ## Update a person
Endpoint: PUT /api/<int:user_id>

Description: Update details of a person with the given name.

Request Body: JSON data containing updated person details (age, email).

Example Request:
   curl -X PUT http://localhost:5000/api/John%20Doe -H "Content-Type: application/json" -d 
   ```json
   '{
       "name": "john doe",
       "age": 35,
    }'
```
  ## Delete a person
Endpoint: DELETE /api/<int:user_id>

Description: Delete a person with the given name.

Example Request:
   curl -X DELETE http://localhost:5000/api/John%20Doe


### Testing the API
You can use Postman or a testing framework (e.g., pytest) to test the API. Detailed instructions for testing the API can be found in the Testing the API section of the README.

### Contributing
If you'd like to contribute to this project, please follow the guidelines in CONTRIBUTING.md.

### License
This project is licensed under the MIT License - see the LICENSE.md file for details.