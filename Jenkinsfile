pipeline {
  agent any
  stages {
    stage('Build') {
      parallel {
        stage('Build') {
          steps {
            echo 'Building..'
            sh '''
                cd simple_webserver
                echo "docker build command should be here"
                '''
          }
        }

        stage('') {
          steps {
            echo 'another stage '
          }
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