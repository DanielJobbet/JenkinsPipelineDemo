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
                    pip install -r requirements.txt
                '''
            }
        }
        stage('Linting') {
            steps {
                // bat '''
                //     call venv\\Scripts\\activate
                //     where pylint
                //     venv\\Scripts\\python -m pylint src tests > pylint_report.txt 2>&1
                //     type pylint_report.txt
                // '''
                script {
                    bat 'find . -name \\*.py | xargs pylint -f parseable | tee pylint.log'
                    recordIssues(
                        tool: pyLint(pattern: 'pylint.log'),
                        unstableTotalHigh: 100,
                    )
                }
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
