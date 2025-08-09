# Simple FastAPI "Hello World" Application

This project is a very simple web application built with Python and the [FastAPI](https://fastapi.tiangolo.com/) framework. It provides a single API endpoint that returns a "Hello World" message.

The application is containerized using Docker.

## API Endpoint

### `GET /`

Returns a JSON response with a "Hello World" message.

**Example Response:**

```json
{
  "message": "Hello World"
}
```

### `GET /test`

Returns a JSON response with a "Happy test" message.

**Example Response:**

```json
{
  "message": "Happy test"
}
```

### `GET /book/{book_name}`

Retrieves information about a book from the MySQL database.

*   **`book_name`** (path parameter): The name of the book to retrieve.

**Example Success Response (200 OK):**

```json
{
  "id": 1,
  "name": "The Hitchhiker's Guide to the Galaxy",
  "author": "Douglas Adams"
}
```

**Example Error Response (404 Not Found):**

```json
{
  "detail": "Book not found"
}
```

**Example Error Response (500 Internal Server Error):**

```json
{
  "detail": "Database connection failed"
}
```

## Configuration

The application requires the following environment variables to be set for database connection:

*   `DB_HOST`: The hostname or IP address of the MySQL server.
*   `DB_USER`: The username for the database connection.
*   `DB_PASSWORD`: The password for the database user.
*   `DB_NAME`: The name of the database to connect to.

## How to Run

This application is designed to be run as a Docker container.

### Prerequisites

*   [Docker](https://docs.docker.com/get-docker/) installed on your machine.

### Steps

1.  **Clone the repository:**

    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2.  **Build the Docker image:**

    From the root of the project directory, run the following command:

    ```bash
    docker build -t fastapi-hello-world .
    ```

3.  **Run the Docker container:**

    You need to pass the database connection details as environment variables to the container.

    ```bash
    docker run -p 8080:8080 \
      -e DB_HOST=<your_db_host> \
      -e DB_USER=<your_db_user> \
      -e DB_PASSWORD=<your_db_password> \
      -e DB_NAME=<your_db_name> \
      fastapi-hello-world
    ```

4.  **Access the application:**

    Open your web browser or use a tool like `curl` to access the application at:

    [http://localhost:8080](http://localhost:8080)

    You should see the following response:

    ```json
    {"message":"Hello World"}
    ```
