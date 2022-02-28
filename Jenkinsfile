// Jenkins env var reference https://www.jenkins.io/doc/book/pipeline/jenkinsfile/#working-with-your-jenkinsfile

pipeline {
    agent { label 'ec2-fleet' }

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

         stage('Provision - dev') {
            when { changeset "infra/dev/**" }
            input {
                message "Do you want to proceed for infrastructure provisioning?"
            }
            steps {
                // copyArtifacts filter: 'infra/dev/terraform.tfstate', projectName: '${JOB_NAME}'
                sh '''
                cd infra/dev
                terraform init && terraform plan && terraform apply -auto-approve
                '''
                archiveArtifacts artifacts: 'infra/dev/terraform.tfstate', onlyIfSuccessful: true
            }
        }
    }
}