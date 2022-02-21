// Jenkins env var reference https://www.jenkins.io/doc/book/pipeline/jenkinsfile/#working-with-your-jenkinsfile

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
            when { changeRequest() }
            steps {
                echo 'Testing..'
                sh 'pip3 install -r simple_webserver/requirements.txt'
                sh 'python3 -m unittest simple_webserver/tests/test_flask_web.py'
            }
        }
        stage('Provisioning - Dev') {
            when { allOf { branch "dev"; changeset "infra/**/*.tf" } }
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