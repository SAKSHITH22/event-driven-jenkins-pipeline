pipeline {
    agent any

    environment {
        AWS_DEFAULT_REGION = 'us-east-1'
    }

    stages {

        stage('Package Lambda') {
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
                    sh 'cd terraform && terraform init'
                }
            }
        }

        stage('Terraform Refresh & Plan') {
            steps {
                withCredentials([[$class: 'AmazonWebServicesCredentialsBinding',
                                  credentialsId: 'aws-root-creds']]) {
                    sh '''
                    cd terraform
                    terraform refresh
                    terraform plan
                    '''
                }
            }
        }

        stage('Terraform Apply') {
            steps {
                withCredentials([[$class: 'AmazonWebServicesCredentialsBinding',
                                  credentialsId: 'aws-root-creds']]) {
                    sh 'cd terraform && terraform apply -auto-approve'
                }
            }
        }
        stage('Terraform Destroy') {
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
            echo 'Deployment Successful!'
        }
        failure {
            echo 'Deployment Failed!'
        }
    }
}
