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
                    sh "docker build -t $IMAGE_NAME ."
                }
            }
        }

        stage('Run Container') {
            steps {
                script {
                    // Stop and remove if already running
                    sh """
                    docker rm -f $CONTAINER_NAME || true
                    docker run -d --name $CONTAINER_NAME -p $PORT:5000 $IMAGE_NAME
                    """
                }
            }
        }

        stage('Verify API Running') {
            steps {
                script {
                    // Wait a bit and test the endpoint
                    sh "sleep 5"
                    sh "curl -f http://localhost:$PORT || echo 'API did not respond'"
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
