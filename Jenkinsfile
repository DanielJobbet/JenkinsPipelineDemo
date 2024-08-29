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
                bat 'python3 -m venv venv'
            }
        }
        stage('Run Tests') {
            steps {
                bat '''
                    venv\\Scripts\\activate
                    pip install pytest==8.3.2
                    pytest --verbose --junit-xml test-reports/results.xml tests/factorial_test.py
                '''
                // Run the Python test file
                // Modify this command based on the test framework you're using
                // bat 'python -m unittest factorial_test.py'
                // or, if using pytest:
            }
            post {
                always {
                    // Clean up workspace after the build
                    junit allowEmptyResults: true, testResults: '**/test-results/*.xml'
                    // cleanWs()
                }
            }
        }
    }
}
