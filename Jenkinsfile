pipeline {
    agent any
    environment {
            imagename = "python:3.8.12-slim-buster"
            registryCredential = 'simpleImage'
            dockerImage = ''

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                sh '''
                cd simple_webserver
                dockerImage = docker.build python:3.8.12-slim-buster


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