pipeline {
  agent any

  environment {
    AWS_DEFAULT_REGION = 'us-east-1'
  }

  parameters {
    booleanParam(
      name: 'CONFIRM_DESTROY',
      defaultValue: false,
      description: '⚠️ Check this to CONFIRM Terraform Destroy'
    )
  }

  stages {

    stage('Terraform Init') {
      steps {
        withCredentials([[$class: 'AmazonWebServicesCredentialsBinding',
                          credentialsId: 'aws-root-creds']]) {
          sh '''
            cd terraform
            terraform init -reconfigure
          '''
        }
      }
    }

    stage('Terraform Destroy') {
      when {
        expression { params.CONFIRM_DESTROY == true }
      }
      steps {
        withCredentials([[$class: 'AmazonWebServicesCredentialsBinding',
                          credentialsId: 'aws-root-creds']]) {
          sh '''
            cd terraform
            terraform destroy -auto-approve
          '''
        }
      }
    }
  }

  post {
    success {
      echo '✅ Infrastructure destroyed successfully!'
    }
    failure {
      echo '❌ Destroy failed!'
    }
  }
}
