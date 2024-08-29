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
                bat '''
                    python -m venv venv
                    venv\\Scripts\\activate
                '''
            }
        }
        stage('Run Tests') {
            steps {
                // Run the Python test file
                // Modify this command based on the test framework you're using
                bat '''
                    venv\\Scripts\\activate
                    python -m unittest -v tests/factorial_test.py > unittest_output.log 2>&1
                    type unittest_output.log
                '''
                // or, if using pytest:
            }
            post {
                always {
                    // Clean up workspace after the build
                    // junit allowEmptyResults: true, testResults: 'results.xml'
                    cleanWs()
                }
            }
        }
    }
}
