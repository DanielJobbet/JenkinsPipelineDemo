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
                bat '''
                    python3 -m venv venv
                    venv\\Scripts\\activate
                    pip install pytest==8.3.2
                    pytest --capture=no  > pytest_output.log tests/factorial_test.py
                '''
                // Run the Python test file
                // Modify this command based on the test framework you're using
                // bat 'python -m unittest factorial_test.py'
                // or, if using pytest:
            }
        }
    }
    post {
        always {
            // Clean up workspace after the build!
            archiveArtifacts artifacts: 'pytest_output.log', allowEmptyArchive: true
            cleanWs()
        }
    }
}
