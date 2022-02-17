pipeline {
    agent any

    stages {
        stage('login'){
           steps{
              sh '''
              aws ecr get-login-password --region us-west-2 | docker login --username AWS --password-stdin 352708296901.dkr.ecr.us-west-2.amazonaws.com
              '''
           }

        }

        stage('Build') {
            steps {
                echo 'Building..'
                sh '''
                cd simple_webserver
                docker build -t web_server_adham .
                docker tag web_server_adham:latest 352708296901.dkr.ecr.us-west-2.amazonaws.com/web_server_adham:latest

                '''
            }
        }
        stage('push'){
           steps{
              sh '''
              docker push 352708296901.dkr.ecr.us-west-2.amazonaws.com/web_server_adham:latest
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
