## Book Management API
A simple RESTful Book Management API built with **FastAPI**. This project demonstrates the fundamentals of building APIs using Python, including CRUD operations, input validation, HTTP status codes, exception handling, and query parameter searching. The project uses an in-memory list to store data, making it ideal for learning FastAPI before integrating a database.
## Features
- Retrieve all books
- Retrieve a book by ID
- Add a new book
- Update an existing book
- Delete a book
- Search books by title using query parameters
- Input validation with Pydantic
- Error handling using HTTPException
- Automatic API documentation with Swagger UI
- Organized project structure with separate models file
## Technologies Used
- Python 3.x
- FastAPI
- Uvicorn
- Pydantic
## Project Structure
```
book_api/
│── main.py
│── models.py
│── requirements.txt
└── README.md
```
---
```
## Install dependencies
```bash
pip install -r requirements.txt
```
## Run the Application
Start the FastAPI server:
```bash
uvicorn main:app --reload
```
The application will run at:
```
http://127.0.0.1:8000
```
## API Documentation
Swagger UI
```
http://127.0.0.1:8000/docs
```
ReDoc
```
http://127.0.0.1:8000/redoc
```
## API Endpoints
| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/` | Welcome message |
| GET | `/books` | Retrieve all books |
| GET | `/books/{id}` | Retrieve a book by ID |
| POST | `/books` | Add a new book |
| PUT | `/books/{id}` | Update an existing book |
| DELETE | `/books/{id}` | Delete a book |
| GET | `/search?title=` | Search books by title |
## Sample Request
### Add a Book
**POST** `/books`
```json
{
    "id": 3,
    "title": "Machine Learning",
    "author": "Sara",
    "price": 1200
}
```
### Sample Response
```json
{
    "message": "Book Added Successfully",
    "book": {
        "id": 3,
        "title": "Machine Learning",
        "author": "Sara",
        "price": 1200
    }
}
```
## Input Validation
This project uses **Pydantic** to validate incoming data.
Validation rules include:
- Book ID must be greater than 0.
- Title must contain at least 2 characters.
- Author name must contain at least 2 characters.
- Price must be greater than 0.
If invalid data is submitted, FastAPI automatically returns a validation error.
## Error Handling
The API uses `HTTPException` to return meaningful error responses.
Example:
```json
{
    "detail": "Book not found"
}
```
Status Code:
```
404 Not Found
```
## Response Status Codes
| Status Code | Description |
|--------------|-------------|
| 200 OK | Request successful |
| 201 Created | Resource created successfully |
| 404 Not Found | Book not found |
| 422 Unprocessable Entity | Validation error |
## Testing
You can test the API using:
- Swagger UI (`/docs`)
- ReDoc (`/redoc`)
- Postman
- Thunder Client (VS Code Extension)
## Learning Outcomes
This project demonstrates:
- FastAPI Fundamentals
- REST API Development
- CRUD Operations
- Request and Response Handling
- Input Validation with Pydantic
- HTTP Exceptions
- Response Status Codes
- Query Parameters
- Project Organization
- API Testing
## Future Improvements

- Connect with MySQL or PostgreSQL
- MongoDB Integration
- SQLAlchemy ORM
- User Authentication (JWT)
- Sorting and Filtering
- Docker Support
- Unit Testing
## Author

**DEvolped By Muhammad Zeeshan Haider**  
# Student-Management-Api
A simple Student Management API built with FastAPI that demonstrates CRUD operations, routing, path and query parameters, Pydantic validation, and proper HTTP status codes.
## Features
- FastAPI project setup
- RESTful API endpoints
- Get all students
- Get a student by ID
- Add a new student
- Update student details
- Delete a student
- Path Parameters
- Query Parameters
- Request & Response Models
- Pydantic input validation
- Proper HTTP status codes
- Interactive Swagger API documentation
## Project Structure
```
student-management-api/
│
├── student.py
├── models.py
├── requirements.txt
├── README.md
└── .gitignore
```
## Technologies Used
- Python 3
- FastAPI
- Uvicorn
- Pydantic
## Run the Application
Start the FastAPI development server:
```bash
uvicorn main:app --reload
```
Server will run at:
```
http://127.0.0.1:8000
```
## API Documentation
Swagger UI
```
http://127.0.0.1:8000/docs
```
ReDoc Documentation
```
http://127.0.0.1:8000/redoc
```
## API Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Welcome message |
| GET | `/students` | Get all students |
| GET | `/students/{id}` | Get a student by ID |
| POST | `/students` | Add a new student |
| PUT | `/students/{id}` | Update student information |
| DELETE | `/students/{id}` | Delete a student |
## Example Student Object
```json
{
  "id": 1,
  "name": "Ali",
  "age": 20,
  "course": "Computer Science"
}
```
## Example Request (POST)
```json
{
  "name": "Zeeshan",
  "age": 22,
  "course": "BS Information Technology"
}
```
## Learning Objectives
This project covers the following FastAPI concepts:
- FastAPI project setup
- Routing
- Path Parameters
- Query Parameters
- Request Models
- Response Models
- Pydantic Basics
- CRUD Operations
- HTTP Status Codes
- API Testing with Swagger UI
## Project Highlights
- Beginner-friendly FastAPI project
- Clean and simple code structure
- No database required (uses in-memory storage)
- Input validation using Pydantic
- Interactive API documentation
- Easy to understand and extend
## Future Improvements
- Integrate MySQL or SQLite database
- Add SQLAlchemy ORM
- Implement JWT Authentication
- Add User Login and Registration
- Docker Support
- Unit Testing
## Author
** Devolped By Muhammad Zeeshan Haider **

