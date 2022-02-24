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
    }
}