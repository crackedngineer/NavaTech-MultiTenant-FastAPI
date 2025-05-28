# NavaTech-MultiTenant-FastAPI

## Prerequisites
Before you begin, ensure you have the following installed on your system:

Docker: [Install Docker](https://docs.docker.com/get-docker/)

Docker Compose: Docker Desktop typically includes Docker Compose. If not, follow the [installation guide](https://docs.docker.com/compose/install/).

## Installation and Setup
Follow these steps to get the application up and running using Docker Compose:

#### Clone the Repository:

```
git clone <your-repository-url>
cd organization-management # Or your project's root directory
```

#### Create Environment File:
The project uses environment variables for configuration (e.g., database connection, secret keys). Create a .env file by copying the example:

```
cp .env.example .env
```

Note: You will need to create a .env.example file if one doesn't exist

#### Build and Run Services:
This command will build the Docker images (if not already built) and start the PostgreSQL database and the FastAPI application containers.

```
docker-compose up --build -d
```

The -d flag runs the services in detached mode (in the background).

## Accessing the API
Once all services are running and migrations are applied, the FastAPI application will be accessible at:

**API Documentation (Swagger UI)**: http://localhost:8000/docs

**API Root**: http://localhost:8000/v1

## Basic API Usage (Example)
You can use curl or a tool like Postman/Insomnia to interact with the API.

**1. Create an Organization**
Endpoint: `POST /api/v1/organisation`

```sh
curl -X POST "http://localhost:8000/api/v1/organisation" \
-H "Content-Type: application/json" \
-d '{
  "email": "admin@example.com",
  "password": "StrongP@ssw0rd1!",
  "name": "MyFirstOrg",
  "host": "myfirstorg.com"
}'
```

**2. Get Organization by Name**
Endpoint: GET `/api/v1/organisation/{name}`

```sh
curl -X GET "http://localhost:8000/api/v1/organisation/{name}"
```

**3. Admin Login (for the created organization)**
Endpoint: POST `/api/v1/organisation/{name}/auth/login`

```sh
curl -X POST "http://localhost:8000/api/v1/organisation/{name}/auth/login" \
-H "Content-Type: application/json" \
-d '{
  "email": "admin@example.com",
  "password": "StrongP@ssw0rd1!",
}'
```

This will return a JWT token that can be used for authenticating future requests to tenant-specific endpoints.