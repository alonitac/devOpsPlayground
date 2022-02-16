pipeline {
    agent any
    environment {
              AWS_ACCOUNT_ID=”3527-0829-6901”
              AWS_DEFAULT_REGION=”us-west-2”
              IMAGE_REPO_NAME=”web_server_adham”
              IMAGE_TAG=”latest”
              REPOSITORY_URI = “${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_DEFAULT_REGION}.amazonaws.com/${IMAGE_REPO_NAME}”
                }

    stages {
        stage(‘Logging into AWS ECR’) {
                steps {
                script {
                sh “aws ecr get-login-password — region ${AWS_DEFAULT_REGION} | docker login — username AWS — password-stdin ${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_DEFAULT_REGION}.amazonaws.com”
                }

                }
                }
        stage('Build') {
            steps {
                echo 'Building..'
                script {
                dockerImage = docker.build “${IMAGE_REPO_NAME}:${IMAGE_TAG}"
                }
            }
        }
        stage(‘Pushing to ECR’) {
                steps{
                script {
                sh “docker tag ${IMAGE_REPO_NAME}:${IMAGE_TAG} ${REPOSITORY_URI}:$IMAGE_TAG”
                sh “docker push ${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_DEFAULT_REGION}.amazonaws.com/${IMAGE_REPO_NAME}:${IMAGE_TAG}”
                }
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
