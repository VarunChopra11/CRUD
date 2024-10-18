
# Flask-MongoDB User Management API

This project is a Basic Flask-based API for user management, using MongoDB as the database and Docker for containerization. It includes routes for creating, reading, updating, and deleting users. Passwords are securely hashed, and the API interacts with MongoDB for data storage. The application is set up and run using Docker for easy deployment.

## Features

- User creation, retrieval, updating, and deletion (CRUD).
- Password hashing for security.
- MongoDB for data storage.
- Dockerized for easy setup and deployment.

## Folder Structure

```
app/
│
├── models/
│   └── user_model.py        # User schema validation
│
├── routes/
│   ├── __init__.py          # Blueprint initialization
│   └── user_routes.py       # User-related routes
│
├── services/
│   ├── __init__.py          # Service initialization
│   ├── config.py            # Configuration settings (MongoDB URI, port, etc.)
│   └── user_services.py     # User-related business logic (CRUD operations)
|
|── config.py                # Configuration settings (MongoDB URI, port, etc.)
│── database.py              # MongoDB initialization
└── main.py                  # Main entry point of the application

docker-compose.yml           # Docker Compose setup for Flask and MongoDB
Dockerfile                   # Dockerfile for building the Flask app image
requirements.txt             # Python dependencies
```

## Getting Started

### Prerequisites

Make sure you have the following installed on your local machine:
- Docker
- Docker Compose
- Python 3.9

### Setup and Installation

1. Clone the repository:

   ```bash
   git clone [https://github.com/your-repo-name/flask-mongo-api.git](https://github.com/VarunChopra11/CRUD.git)
   cd CRUD
   ```

2. Build and run the application with Docker Compose:

   ```bash
   docker-compose up --build
   ```

   This will:
   - Build the Flask app based on the Dockerfile.
   - Set up a MongoDB container to persist user data.

3. Access the API:

   The Flask API will be accessible at:
   ```
   http://localhost:5000
   ```

4. Verify MongoDB:

   MongoDB service will be running at:
   ```
   mongodb://localhost:27017/users_db
   ```

   You can verify the MongoDB setup using a MongoDB client or the Mongo shell.

## API Endpoints

The following API endpoints are available for managing users:

- **Create a user (POST)**: `/users`
   - Payload: `{"id": "<id>", "name": "<name>", "email": "<email>", "password": "<password>"}`
- **Get all users (GET)**: `/users`
- **Get a user by ID (GET)**: `/users/<id>`
- **Update a user by ID (PUT)**: `/users/<id>`
   - Payload: Partial or complete update JSON
- **Delete a user by ID (DELETE)**: `/users/<id>`


## Configuration

The configuration for MongoDB is set in `config.py` and can be modified via environment variables:

- `MONGO_URI`: The MongoDB URI (default is `mongodb://mongo:27017/users_db` in the Docker setup).

To change these, you can update the `docker-compose.yml` file or export environment variables before running the app:

```bash
export MONGO_URI=mongodb://<your-mongo-uri>
```

## Requirements

The dependencies for this project are listed in `requirements.txt`. The main dependencies include:
- Flask
- Flask-PyMongo
- Werkzeug
- Marshmallow
- Bson

To install them locally:

```bash
pip install -r requirements.txt
```

## Running Locally (without Docker)

If you prefer to run the project without Docker:

1. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

2. Set up MongoDB locally and update the `MONGO_URI` in `config.py`.

3. Run the application:

   ```bash
   python main.py
   ```

   The app will be available at `http://localhost:5000`.

## License

This project is licensed under the MIT License.
