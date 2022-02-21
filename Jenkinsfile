pipeline {
    agent any
    environment {
    DockerHost = '352708296901.dkr.ecr.us-east-1.amazonaws.com'
    Image = 'eliasrepo:${BRANCH_NAME}_{BUILD_NUMBER}'
    }

    stages {
        stage('Build Simple Webserver') {
        when { anyOf {branch "master" ; branch "dev"}}
            steps {
                echo 'Building.'
                sh '''
                 IMAGE="eliasrepo:${BRANCH_NAME}_${BUILD_NUMBER}"
                     cd simple_webserver
                  aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin ${DockerHost}
                  docker build  -t ${IMAGE} .
                  docker tag ${IMAGE} ${DockerHost}/${IMAGE}
                  docker push ${DockerHost}/${IMAGE}
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