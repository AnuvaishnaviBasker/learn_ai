pipeline {
    agent any

    environment {
        PYTHON_BIN = 'python3'
    }

    stages {
        stage('Setup Python environment') {
            steps {
                sh '''
                    ${PYTHON_BIN} -m pip install --upgrade pip
                    ${PYTHON_BIN} -m pip install -r requirements.txt
                    ${PYTHON_BIN} -m pip install pytest-html
                    ${PYTHON_BIN} -m playwright install webkit
                '''
            }
        }

        stage('Run tests') {
            steps {
                sh '''
                    mkdir -p reports
                    ${PYTHON_BIN} -m pytest -q
                '''
            }
        }

        stage('Publish HTML Report') {
            steps {
                publishHTML(target: [
                    reportDir: 'reports',
                    reportFiles: 'report.html',
                    reportName: 'Pytest HTML Report',
                    keepAll: true
                ])
            }
        }
    }
}
