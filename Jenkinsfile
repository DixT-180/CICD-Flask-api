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
                   
//                     docker run -d --name $CONTAINER_NAME -p $PORT:5000 $IMAGE_NAME
//                     """
//                 }
//             }
//         }
//  // docker rm -f $CONTAINER_NAME || true
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
                    // Stop and remove container if already running
                    sh """
                    if [ \$(docker ps -a -q -f name=$CONTAINER_NAME) ]; then
                        docker stop $CONTAINER_NAME
                        docker rm -f $CONTAINER_NAME

                    fi

                    docker run -d --name $CONTAINER_NAME -p $PORT:5000 $IMAGE_NAME
                    """
                }
            }
        }

        stage('Verify API Running') {
            steps {
                script {
                    // Wait for container to be ready, then check API
                    sh "sleep 5"
                    sh "curl -f http://localhost:$PORT || (echo 'API did not respond' && exit 1)"
                }
            }
        }
    }
}
