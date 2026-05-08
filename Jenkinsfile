pipeline {
    agent any

    environment {
        VENV = "venv"
    }

    stages {

        stage('Clean Workspace') {
            steps {
                cleanWs()

                bat '''
                if exist reports rmdir /s /q reports
                if exist .pytest_cache rmdir /s /q .pytest_cache
                if exist allure-results rmdir /s /q allure-results
                if exist allure-report rmdir /s /q allure-report
                '''
            }
        }

        stage('Checkout Latest Code') {
            steps {
                git branch: 'main',
                url: 'https://github.com/PoojithaSanda/pytest-capstone-project.git'
            }
        }

        stage('Setup Environment') {
            steps {
                bat '''
                python -m venv venv

                call venv\\Scripts\\activate

                python -m pip install --upgrade pip

                pip install -r requirements.txt
                '''
            }
        }

        stage('Run UI + API Tests') {
            steps {
                bat '''
                call venv\\Scripts\\activate

                pytest tests -n auto -v --cache-clear ^
                --html=reports/report.html --self-contained-html ^
                --alluredir=reports/allure-results
                '''
            }
        }

        stage('Generate Allure Report') {
            steps {
                allure([
                    includeProperties: false,
                    jdk: '',
                    properties: [],
                    reportBuildPolicy: 'ALWAYS',
                    results: [[path: 'reports/allure-results']]
                ])
            }
        }

        stage('Verify Reports') {
            steps {
                bat '''
                echo ===== REPORT FILES =====
                dir reports
                '''
            }
        }

        stage('Publish HTML Report') {
            steps {
                publishHTML(target: [
                    allowMissing: true,
                    alwaysLinkToLastBuild: true,
                    keepAll: true,
                    reportDir: 'reports',
                    reportFiles: 'report.html',
                    reportName: 'Automation Test Report'
                ])
            }
        }

        stage('Archive Artifacts') {
            steps {
                archiveArtifacts artifacts: 'reports/**', allowEmptyArchive: true
            }
        }
    }

    post {

        always {
            echo 'Pipeline Execution Completed'
        }

        success {
            echo 'Build Successful ✔'
        }

        failure {
            echo 'Build Failed Check Console Output'
        }
    }
}