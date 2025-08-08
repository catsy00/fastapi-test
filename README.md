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

    ```bash
    docker run -p 8080:8080 fastapi-hello-world
    ```

4.  **Access the application:**

    Open your web browser or use a tool like `curl` to access the application at:

    [http://localhost:8080](http://localhost:8080)

    You should see the following response:

    ```json
    {"message":"Hello World"}
    ```
