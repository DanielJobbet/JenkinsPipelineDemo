pipeline {
    agent any
    stages {
        stage('Initialize') {
            steps {
                echo 'Initializing..'
                echo "Running ${env.BUILD_ID} on ${env.JENKINS_URL}"
            }
        }
        stage('Checkout') {
            steps {
                // Checkout the code from the Git repository
                checkout scm
            }
        }
        stage('Build') {
            steps {
                // Build the Python virtual environment
                bat '''
                    python -m venv venv
                    venv\\Scripts\\activate
                    pip install requirements.txt
                '''
            }
        }
        stage('Linting') {
            steps {
                bat '''
                    call venv\\Scripts\\activate
                    flake8 --output-file=flake8_report.txt --tee src tests
                    type flake8_report.txt
                '''
            }
        }
        stage('Run Unit Tests') {
            steps {
                // Run the Python tests
                bat '''
                    python -m pytest -v tests/factorial_test.py
                '''
            }
        }
    }
    post {
        always {
            // Clean up workspace after the build
            cleanWs()
        }
    }
}
