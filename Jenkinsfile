// pipeline {
//     agent any

//     environment {
//         IMAGE_NAME = 'titanic-data-quality-api'
//         CONTAINER_NAME = 'titanic-api-container'
//         PORT = '5000'
//     }

//     stages {
//         stage('Checkout') {
//             steps {
//                 checkout scm
//             }
//         }

//         stage('Build Docker Image') {
//             steps {
//                 script {
//                     sh "docker build -t $IMAGE_NAME -f DockerFile ."
//                 }
//             }
//         }

//         stage('Run Container') {
//             steps {
//                 script {
//                     // Stop and remove if already running
//                     sh """
//                     docker rm -f $CONTAINER_NAME || true
//                     docker run -d --name $CONTAINER_NAME -p $PORT:5000 $IMAGE_NAME
//                     """
//                 }
//             }
//         }

//         stage('Verify API Running') {
//             steps {
//                 script {
//                     // Wait a bit and test the endpoint
//                     sh "sleep 5"
//                     sh "curl -f http://localhost:$PORT || echo 'API did not respond'"
//                 }
//             }
//         }
//     }

//     post {
//         always {
//             echo "Cleaning up Docker containers"
//             sh "docker rm -f $CONTAINER_NAME || true"
//         }
//     }
// }

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
                    sh "docker build -t $IMAGE_NAME -f Dockerfile ."
                }
            }
        }

        stage('Run Container') {
            steps {
                script {
                    sh """
                    docker rm -f $CONTAINER_NAME || true
                    docker run -d --name $CONTAINER_NAME --network jenkins -p $PORT:5000 $IMAGE_NAME
                    """
                }
            }
        }

        stage('Verify API Running') {
            steps {
                script {
                    sh """
                    for i in {1..5}; do
                        curl -f http://$CONTAINER_NAME:5000 && exit 0
                        echo 'API not ready, retrying...'
                        sleep 5
                    done
                    docker logs $CONTAINER_NAME
                    echo 'API did not respond'
                    exit 1
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