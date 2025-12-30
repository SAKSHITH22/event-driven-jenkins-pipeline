pipeline {
    agent any

    parameters {
        choice(
            name: 'ACTION',
            choices: ['apply', 'destroy'],
            description: 'Choose apply to create resources or destroy to delete resources'
        )
    }

    environment {
        AWS_DEFAULT_REGION = 'us-east-1'
    }

    stages {

        stage('Package Lambda') {
            when {
                expression { params.ACTION == 'apply' }
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
                    sh 'cd terraform && terraform init'
                }
            }
        }

        stage('Terraform Plan') {
            when {
                expression { params.ACTION == 'apply' }
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
                expression { params.ACTION == 'apply' }
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
                expression { params.ACTION == 'destroy' }
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
            echo "Terraform ${params.ACTION} completed successfully!"
        }
        failure {
            echo "Terraform ${params.ACTION} failed!"
        }
    }
}
