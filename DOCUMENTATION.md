# Person API Documentation

Welcome to the documentation for the Person API. This API allows you to perform CRUD (Create, Read, Update, Delete) operations on person records.

## Table of Contents

- [Standard Request and Response Formats](#standard-request-and-response-formats)
- [Sample API Usage](#sample-api-usage)
- [Known Limitations and Assumptions](#known-limitations-and-assumptions)
- [Setup and Deployment Instructions](#setup-and-deployment-instructions)

---

## Standard Request and Response Formats

### Create a Person (POST /api)

**Request Format**

- HTTP Method: POST
- URL: `/api`

- **Request Headers:**
  - Content-Type: application/json

- **Request Body:**

  ```json
  {
    "name": string
  }

**Response Format**

HTTP Status Code: 201 (Created) on success

**JSON Response Body:**
   ```json
  {
    "message": "Person created successfully, 'id': last_id"
  }
   ```
### Retrieve a Person (GET '/api/<int:user_id>')

**Request Format**

HTTP Method: GET
URL: '/api/<int:user_id>'

**Response Format**

HTTP Status Code: 200 (OK) on success

**JSON Response Body:**
```json
  {
    "name": string,
    "id": numbers,
}
```
### Update a Person (PUT '/api/<int:user_id>')
**Request Format**

HTTP Method: PUT

URL: '/api/<int:user_id>'>

**Request Headers:**

Content-Type: application/json
**Request Body:**
```json
{
    "name": string
}
```
**Response Format**

HTTP Status Code: 200 (OK) on success

**JSON Response Body:**
```json
{
    "message": "Person updated successfully"
}
```

### Delete a Person (DELETE /api/<int:user_id>)
**Request Format**

HTTP Method: DELETE
URL: '/api/<int:user_id>'

**Response Format**
```json
{
    "message": "Person deleted successfully"
}
```
HTTP Status Code: 204 (No Content) on success


### Retrieve all users created (GET '/api/')
**Request Format**

HTTP Method: GET
URL: '/api/'>

**Response Format**
```json
{
    "name": "chisom Daniel",
    "id": 1
}
{
    "name": "John Doe",
    "id": 2
}
{
    "name": "John daniel",
    "id": 3
}
```
HTTP Status Code: 204 on success
ALL PERSONS CREATED IN JSON FORMAT


## Sample API Usage

**Creating a Person**
**Request**

POST /api HTTP/1.1
Host: localhost:5000

Content-Type: application/json
```json
{
    "name": "John Doe"
}
```

**Response**
```json
{
    "message": "Person created successfully, 'id': last_id"
}
```

**Retrieving a Person**
**Request**

GET /api/<int:user_id> HTTP/1.1
Host: localhost:5000

**Response**
```json
{
    "name": "John Doe",
    "id": <int:user_id>
}
```

**Updating a Person**
**Request**

PUT /api/<int:user_id> HTTP/1.1
Host: localhost:5000

Content-Type: application/json
```json
{
    "name": "john doe",
    "id": <int:user_id>
}
```
**Response**
```json
{
    "message": "Person updated successfully"
}
```


**Deleting a Person**
**Request**

DELETE /api/<int:user_id> HTTP/1.1
Host: localhost:5000

**Response**
```json
{
    "message": "Person deleted successfully"
}
```
(HTTP Status Code: 204 No Content)


**Retrieving all Persons**
**Request**

GET /api/ HTTP/1.1
Host: localhost:5000

**Response**
```json
{
    "name": "chisom Daniel",
    "id": 1
}
{
    "name": "John Doe",
    "id": 2
}
{
    "name": "John daniel",
    "id": 3
}
```



## Known Limitations and Assumptions
. The API assumes that each person's name is unique.

. The API uses SQLite as the default database. You can configure it to use other databases such as MySQL.

. Error handling for edge cases, such as non-existent records, is not provided in this basic example.

## Setup and Deployment Instructions

To set up and deploy the API locally or on a server, follow these steps:

## Clone the repository to your local machine:
```bash
git clone https://github.com/yourusername/person-api.git
```

## Navigate to the project directory:
```bash
cd person-api
```

## Install the required Python packages:
```bash
pip install -r requirements.txt
```
 ## Configure the database settings in app.py.
```bash
connect = sqlite3.connect('database.db')
connect.execute(
    'CREATE TABLE IF NOT EXISTS Persons (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, age TEXT)')
```

## Start the API server:
```bash
python app.py
```


The API will be accessible at http://localhost:5000.
You can now use Postman or other tools to interact with the API as described in the Sample API Usage section.


### Note: This documentation assumes that you have Postman or a similar tool for testing the API. You can also use tools like curl or write your own code to make HTTP requests to the API endpoints.
 
## That's it! You have successfully set up and deployed the Person API.
