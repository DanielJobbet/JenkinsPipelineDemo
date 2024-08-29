pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                // Checkout the code from the Git repository
                checkout scm
            }
        }
        stages {
            stage('Setup Python Environment') {
                steps {
                    // Step 1: Install Python if needed
                    bat 'python3 -m venv venv'
                    
                    // Step 2: Activate the virtual environment
                    bat '''
                        source venv/bin/activate
                        pip install pytest>=7.0.0
                    '''
                }
        }
        stage('Run Tests') {
            steps {
                // Run the Python test file
                // Modify this command based on the test framework you're using
                // bat 'python -m unittest factorial_test.py'
                // or, if using pytest:
                bat '''
                    source venv/bin/activate
                    pytest -s tests/factorial_test.py
                '''
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
