#!/bin/bat
pipeline {
    agent any
    stages {
        stage('Initialize') {
            steps {
                echo 'Initializing..'
                echo "Running ${env.BUILD_ID} on ${env.JENKINS_URL}"
            }
        }
        stage('Build') {
            steps {
                // Build the Python virtual environment
                bat '''
                    python -m venv venv
                    venv\\Scripts\\activate
                    pip install -r requirements.txt
                '''
            }
        }
        stage('Run Unit Tests') {
            steps {
                // Run the Python tests and save logs
                bat 'python -m pytest -v tests/factorial_test.py --junit-xml=results.xml'
                junit testResults: 'results.xml', skipPublishingChecks: true
            }
        }
    }
    post {
        always {
            // Clean up workspace post-stages
            cleanWs()
        }
    }
}
