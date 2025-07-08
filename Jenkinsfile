pipeline {
    agent any

    environment {
        IMAGE_NAME = 'titanic-data-quality-api'
        CONTAINER_NAME = 'titanic-api-container'
        PORT = '5000'
        NETWORK_NAME = 'test-net'
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
                    sh "docker build -t $IMAGE_NAME -f Dockerfile ."
                }
            }
        }

        stage('Create Network') {
            steps {
                script {
                    // Create network if not exists
                    sh "docker network inspect $NETWORK_NAME >/dev/null 2>&1 || docker network create $NETWORK_NAME"
                }
            }
        }

        stage('Run Container') {
            steps {
                script {
                    sh """
                        "docker rm -f $CONTAINER_NAME || true"
                        docker run -d --name $CONTAINER_NAME --network $NETWORK_NAME -p $PORT:5000 $IMAGE_NAME
                    """
                }
            }
        }

        stage('Verify API Running') {
            steps {
                script {
                    sh """
                        docker run --rm --network $NETWORK_NAME curlimages/curl:7.87.0 curl http://$CONTAINER_NAME:5000
                    """
                }
            }
        }
    }

    post {
        always {
            echo "Cleaning up Docker container"
            sh "docker rm -f $CONTAINER_NAME || true"
        }
    }
}
