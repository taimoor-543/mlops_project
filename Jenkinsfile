pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'taimooraliata/mlops_project'
    }

    stages {
        stage('Checkout') {
            steps {
                script {
                    checkout scm
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t %DOCKER_IMAGE% .'
            }
        }

        stage('Push to Docker Hub') {
            steps {
                withDockerRegistry([credentialsId: 'docker-hub', url: '']) {
                     bat 'docker tag mlops_project %DOCKER_IMAGE%'
                     bat 'docker push %DOCKER_IMAGE%'
            }
    }
}


        stage('Deploy') {
            steps {
                bat 'docker run -d -p 5000:5000 ${DOCKER_IMAGE}'
            }
        }

        stage('Notify Admin') {
            steps {
                emailext subject: 'Deployment Successful',
                         body: 'The project has been successfully deployed.',
                         to: 'taimoorwastaken@gmail.com.com'
            }
        }
    }
}
