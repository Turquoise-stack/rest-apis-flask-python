# CONTRIBUTING

## How to run the Dockerfile locally

"
- docker build -t DOCKER_IMAGE_NAME
- docker run -dp 5000:5000 -w /app -v "/c/PATH/app" DOCKER_IMAGE_NAME sh -c flask run --host 0.0.0.0
"