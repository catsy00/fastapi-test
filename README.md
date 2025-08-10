# 간단한 FastAPI "Hello World" 애플리케이션

이 프로젝트는 Python과 [FastAPI](https://fastapi.tiangolo.com/) 프레임워크로 구축된 매우 간단한 웹 애플리케이션입니다. "Hello World" 메시지를 반환하는 단일 API 엔드포인트를 제공합니다.

애플리케이션은 Docker를 사용하여 컨테이너화되어 있습니다.

## API 엔드포인트

### `GET /`

"Hello World" 메시지가 포함된 JSON 응답을 반환합니다.

**응답 예시:**

```json
{
  "message": "Hello World"
}
```

### `GET /test`

"Happy test" 메시지가 포함된 JSON 응답을 반환합니다.

**응답 예시:**

```json
{
  "message": "Happy test"
}
```

### `GET /book/{book_name}`

MySQL 데이터베이스에서 책 정보를 조회합니다.

*   **`book_name`** (경로 매개변수): 조회할 책의 이름입니다.

**성공 응답 예시 (200 OK):**

```json
{
  "id": 1,
  "name": "은하수를 여행하는 히치하이커를 위한 안내서",
  "author": "더글러스 애덤스"
}
```

**오류 응답 예시 (404 Not Found):**

```json
{
  "detail": "Book not found"
}
```

**오류 응답 예시 (500 Internal Server Error):**

```json
{
  "detail": "Database connection failed"
}
```

## 설정

애플리케이션이 데이터베이스에 연결하려면 다음 환경 변수를 설정해야 합니다.

*   `DB_HOST`: MySQL 서버의 호스트 이름 또는 IP 주소.
*   `DB_USER`: 데이터베이스 연결에 사용할 사용자 이름.
*   `DB_PASSWORD`: 데이터베이스 사용자의 비밀번호.
*   `DB_NAME`: 연결할 데이터베이스의 이름.

## 실행 방법

이 애플리케이션은 Docker 컨테이너로 실행되도록 설계되었습니다.

### 사전 요구 사항

*   사용자 컴퓨터에 [Docker](https://docs.docker.com/get-docker/)가 설치되어 있어야 합니다.

### 단계

1.  **리포지토리 클론:**

    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2.  **Docker 이미지 빌드:**

    프로젝트의 루트 디렉토리에서 다음 명령을 실행합니다.

    ```bash
    docker build -t fastapi-hello-world .
    ```

3.  **Docker 컨테이너 실행:**

    데이터베이스 연결 정보를 환경 변수로 컨테이너에 전달해야 합니다.

    ```bash
    docker run -p 8080:8080 \
      -e DB_HOST=<your_db_host> \
      -e DB_USER=<your_db_user> \
      -e DB_PASSWORD=<your_db_password> \
      -e DB_NAME=<your_db_name> \
      fastapi-hello-world
    ```

4.  **애플리케이션 접속:**

    웹 브라우저를 열거나 `curl`과 같은 도구를 사용하여 다음 주소로 애플리케이션에 접속합니다.

    [http://localhost:8080](http://localhost:8080)

    다음과 같은 응답을 볼 수 있습니다.

    ```json
    {"message":"Hello World"}
    ```
