pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                sh '''
                cd simple_webserver
                docker build -t my-app .

                '''
            }
        }
        stage('run') {
            steps {
                echo 'running..'
                sh '''
                docker run -p 3000:3000 my-app
                '''
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }

}
