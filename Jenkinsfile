pipeline {
    agent any
    stages {
        stage('Initialize') {
            steps {
                echo 'Initializing..'
                echo "Running ${env.BUILD_ID} on ${env.JENKINS_URL}"
            }
        }
        stage('Run Tests') {
            steps {
                bat '''
                    python3 -m venv venv
                    venv\\Scripts\\activate
                    pip install pytest==8.3.2
                    python -m pytest --junitxml=test.xml tests/factorial_test.py
                    ./gradlew check
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
            junit 'build/reports/**/*.xml'
            // cleanWs()
        }
    }
}
