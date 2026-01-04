pipeline {
  agent any

  environment {
    AWS_DEFAULT_REGION = 'us-east-1'
  }

  parameters {
    booleanParam(
      name: 'DESTROY',
      defaultValue: true,
      description: '⚠️ Check this to DESTROY all AWS infrastructure'
    )
  }

  stages {

    stage('Package Lambda') {
      when {
        expression { params.DESTROY == false }
      }
      steps {
        sh '''
          cd lambda
          zip -r processor.zip processor.py
          zip -r report.zip report_generator.py
        '''
      }
    }

    stage('Terraform Init') {
      steps {
        withCredentials([[$class: 'AmazonWebServicesCredentialsBinding',
                          credentialsId: 'aws-root-creds']]) {
          sh 'cd terraform && terraform init -reconfigure'
        }
      }
    }

    stage('Terraform Plan') {
      when {
        expression { params.DESTROY == false }
      }
      steps {
        withCredentials([[$class: 'AmazonWebServicesCredentialsBinding',
                          credentialsId: 'aws-root-creds']]) {
          sh 'cd terraform && terraform plan'
        }
      }
    }

    stage('Terraform Apply') {
      when {
        expression { params.DESTROY == false }
      }
      steps {
        withCredentials([[$class: 'AmazonWebServicesCredentialsBinding',
                          credentialsId: 'aws-root-creds']]) {
          sh 'cd terraform && terraform apply -auto-approve'
        }
      }
    }

    stage('Terraform Destroy') {
      when {
        expression { params.DESTROY == true }
      }
      steps {
        withCredentials([[$class: 'AmazonWebServicesCredentialsBinding',
                          credentialsId: 'aws-root-creds']]) {
          sh 'cd terraform && terraform destroy -auto-approve'
        }
      }
    }
  }

  post {
    success {
      echo '✅ Pipeline completed successfully!'
    }
    failure {
      echo '❌ Pipeline failed!'
    }
  }
}
