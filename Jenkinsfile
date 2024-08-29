pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                // Checkout the code from the Git repository
                checkout scm
            }
        }
        stage('Run Tests') {
            steps {
                // Run the Python test file
                // Modify this command based on the test framework you're using
                // bat 'python -m unittest factorial_test.py'
                // or, if using pytest:
                sh 'python -m venv .factorialtest/venv'
                sh 'pytest -s tests/factorial_test.py'
            }
        }
    }
    post {
        always {
            // Clean up workspace after the build!
            cleanWs()
        }
    }
}
