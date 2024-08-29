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
                // Run the Python tests
                bat 'python -m pytest -v tests/factorial_test.py --junit-xml=results.xml || [[ $? -eq 1 ]]'
                junit 'results.xml'
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
