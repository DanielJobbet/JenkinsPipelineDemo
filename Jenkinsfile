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
            // steps {
            //     bat '''
            //         call venv\\Scripts\\activate
            //         python -m pylint src tests > pylint_report.txt
            //         type pylint_report.txt
            //     '''
            // }
            steps {
            bat 'python -m pylint -f parseable --reports=no * > pylint.log' //remove pythonpath if not needed in your environment
            }
            post {
                always {
                    bat 'cat pylint.log'
                        recordIssues healthy: 1, tools: [pyLint(name: 'report name', pattern: '**/pylint.log')], unhealthy: 2
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
