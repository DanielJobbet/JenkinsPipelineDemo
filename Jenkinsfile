pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                // Checkout the code from the Git repository
                checkout scm
            }
        }
        // stage('Install Dependencies') {
        //     steps {
        //         // Install Python dependencies using pip
        //         // This assumes you have a `requirements.txt` file in your repository
        //         // sh 'pip install -r requirements.txt'
        //     }
        // }
        stage('Run Tests') {
            steps {
                // Run the Python test file
                // Modify this command based on the test framework you're using
                sh 'python -m unittest factorial_test.py'
                // or, if using pytest:
                // sh 'pytest test_my_app.py'
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
