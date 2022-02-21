pipeline {
    agent any

    stages {
        stage('Build Simple WebServer') {
            when { anyOf { branch "master"; branch "dev" }}
            steps {
                echo 'Building..'
                sh '''
                cd simple_webserver
                # docker build
                '''
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
                sh 'pip3 install -r simple_webserver/requirements.txt'
                sh 'python3 -m unittest simple_webserver/tests/test_flask_web.py'
            }
        }
        stage('Deploy - dev') {
            when { branch "dev" }
            steps {
                echo 'Deploying....'
            }
        }
        stage('Deploy - prod') {
            when { branch "master" }
            steps {
                echo 'Deploying....'
            }
        }
        stage('Provisioning - Dev') {
            when { allOf { branch "dev"; changeset "infra/**/*.tf" } }
            steps {
                echo 'Provisioning....'
                sh 'cd infra/dev'
                // sh 'terraform init'
                // copyArtifacts filter: 'infra/dev/terraform.tfstate', projectName: '${JOB_NAME}'
                // archiveArtifacts artifacts: 'infra/dev/terraform.tfstate', onlyIfSuccessful: true
            }
        }
    }
}