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
                    pip install pytest
                '''
            }
        }
        stage('Run Tests') {
            steps {
                // Run the Python test file
                bat '''
                    python -m pytest -v --color=yes tests/factorial_test.py
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
