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
        // stage('Run Unit Tests') {
        //     steps {
        //         // Run the Python tests and save logs
        //         bat '''
        //             python -m pytest -v tests/factorial_test.py --junit-xml=results.xml
        //             if %ERRORLEVEL% neq 0 exit 0
        //         '''
        //         junit allowEmptyResults: true, testResults: 'results.xml', skipPublishingChecks: true
        //     }
        // }
        stage('Run Unit Test') {
            steps {
                script {
                    // Run the tests without generating XML
                    bat '''
                        python -m pytest -v tests/factorial_test.py > test_output.log
                        if %ERRORLEVEL% neq 0 exit 0
                    '''
                    
                    // Convert test output to JUnit XML (hypothetical tool or script)
                    bat '''
                        python generate_junit_xml.py test_output.log results.xml
                    '''

                    // Process the test results
                    junit allowEmptyResults: true, testResults: 'results.xml', skipPublishingChecks: true
                }
            }
        }
    }
    post {
        always {
            // Clean up workspace post-stages
            cleanWs()
        }
    }
}
