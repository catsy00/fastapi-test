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

---

## OpenShift에 Argo CD로 배포하기

이 애플리케이션은 OpenShift 클러스터에 Argo CD를 사용하여 배포할 수 있습니다. `deploy/` 디렉토리에 필요한 모든 설정 파일이 포함되어 있습니다.

### 사전 요구 사항

*   OpenShift 클러스터에 접근할 수 있는 `oc` CLI.
*   클러스터에 Argo CD가 설치되어 있어야 합니다.
*   애플리케이션을 배포할 네임스페이스(프로젝트).

### 배포 단계

1.  **설정 파일 수정:**

    배포하기 전에 `deploy/` 디렉토리의 설정 파일에 있는 자리표시자(placeholder) 값들을 실제 환경에 맞게 수정해야 합니다.

    *   `deploy/secret.yaml`: `stringData` 섹션에 실제 데이터베이스 연결 정보를 입력합니다.
    *   `deploy/argocd-application.yaml`:
        *   `repoURL`: 이 Git 리포지토리의 실제 URL로 변경합니다.
        *   `namespace`: 애플리케이션을 배포할 OpenShift 네임스페이스로 변경합니다.
    *   (선택 사항) 다른 `.yaml` 파일들에서 주석 처리된 `namespace` 필드를 활성화하고 당신의 네임스페이스를 지정할 수 있습니다.

2.  **네임스페이스 생성:**

    애플리케이션을 배포할 네임스페이스가 없다면 생성합니다.

    ```bash
    oc new-project your-app-namespace
    ```

3.  **Secret 적용:**

    수정한 `secret.yaml` 파일을 OpenShift 클러스터에 적용하여 데이터베이스 접속 정보를 저장합니다.

    ```bash
    oc apply -f deploy/secret.yaml -n your-app-namespace
    ```

4.  **이미지 빌드 및 푸시 (OpenShift 내부 레지스트리 사용):**

    OpenShift는 내부 컨테이너 이미지 레지스트리를 제공합니다. 로컬의 Docker 이미지를 OpenShift로 가져올 수 있습니다.

    a. **OpenShift에 로그인하고 CLI 설정:**
       OpenShift 웹 콘솔에서 로그인 토큰을 복사하여 CLI에 로그인합니다.

    b. **로컬에서 Docker 이미지 빌드:**
       (이미 빌드했다면 이 단계는 건너뛸 수 있습니다.)
       ```bash
       docker build -t fastapi-hello-world:latest .
       ```

    c. **ImageStream 생성:**
       애플리케이션 이미지를 관리할 ImageStream을 생성합니다.
       ```bash
       oc apply -f deploy/imagestream.yaml -n your-app-namespace
       ```

    d. **이미지 푸시:**
       로컬 Docker 이미지를 OpenShift의 ImageStream으로 푸시합니다. 이를 위해 먼저 레지스트리 경로를 확인하고 이미지를 태그한 후 푸시해야 합니다.
       ```bash
       # ImageStream 경로 확인
       IMAGE_REGISTRY_PATH=$(oc get is fastapi-hello-world -n your-app-namespace -o 'jsonpath={.status.dockerImageRepository}')

       # 로컬 이미지 태그
       docker tag fastapi-hello-world:latest $IMAGE_REGISTRY_PATH:latest

       # OpenShift 레지스트리에 로그인 (필요 시) 및 이미지 푸시
       docker push $IMAGE_REGISTRY_PATH:latest
       ```

    e. **새 이미지로 업데이트 (롤아웃):**
       표준 `Deployment` 리소스는 `ImageStream`의 태그 변경을 자동으로 감지하여 새 배포를 시작하지 않습니다. CI/CD 파이프라인이 Git의 `deployment.yaml` 파일에 있는 이미지 태그를 직접 업데이트하는 것이 일반적입니다.

       수동으로 업데이트를 적용하려면, 새 이미지를 푸시한 후 다음 명령어로 롤아웃을 다시 시작하여 `latest` 태그의 새 이미지를 가져오도록 할 수 있습니다.
       ```bash
       oc rollout restart deployment/fastapi-hello-world -n your-app-namespace
       ```

5.  **Argo CD Application 적용:**

    마지막으로, Argo CD가 애플리케이션을 관리하도록 `argocd-application.yaml` 파일을 적용합니다.

    ```bash
    # Argo CD가 설치된 네임스페이스에 적용해야 합니다.
    oc apply -f deploy/argocd-application.yaml -n argocd
    ```

    이제 Argo CD UI에 접속하면 `fastapi-hello-world-app` 애플리케이션이 생성되고, Git 리포지토리의 `deploy` 디렉토리와 동기화되는 것을 볼 수 있습니다.

6.  **배포 확인:**

    `Route`를 통해 할당된 URL을 확인하고 애플리케이션에 접속합니다.

    ```bash
    oc get route fastapi-hello-world -n your-app-namespace
    ```
