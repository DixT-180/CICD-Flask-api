pipeline {
    agent any

    environment {
        IMAGE_NAME = 'titanic-data-quality-api'
        CONTAINER_NAME = 'titanic-api-container'
        PORT = '5000'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh "docker build -t $IMAGE_NAME -f DockerFile ."
                }
            }
        }

        stage('Run Container') {
            steps {
                script {
                    // Stop and remove if already running
                    sh """
                    docker rm -f $CONTAINER_NAME || true
                    docker run -d --name $CONTAINER_NAME --network test-net -p $PORT:5000 $IMAGE_NAME
                    """
                }
            }
        }

        stage('Verify API Running') {
            steps {
                script {
                    sh "docker network create test-net || true"
                    sh "docker network connect test-net $CONTAINER_NAME"
                    sh """
                    docker run --rm --network test-net curlimages/curl:7.87.0 curl http://$CONTAINER_NAME:5000
                    """
                }
            }
        }
    }

    post {
        always {
            echo "Cleaning up Docker containers"
            sh "docker rm -f $CONTAINER_NAME || true"
        }
    }
}
