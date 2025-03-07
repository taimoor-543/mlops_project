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
                bat 'docker build -t taimooraliata/mlops_project:latest .'
    }
}

        stage('Push to Docker Hub') {
            steps {
                withDockerRegistry([credentialsId: 'docker-hub', url: 'https://index.docker.io/v1/']) {
                    bat 'docker tag taimooraliata/mlops_project:latest taimooraliata/mlops_project'
                    bat 'docker push taimooraliata/mlops_project'
        }
    }
}



        stage('Deploy') {
            steps {
                 bat 'docker run -d -p 5000:5000 taimooraliata/mlops_project:latest'
    }
}


        stage('Notify Admin') {
            steps {
                emailext subject: 'Deployment Successful',
                         body: 'The project has been successfully deployed.',
                         to: 'taimoorwastaken@gmail.com'
            }
        }
    }
}
