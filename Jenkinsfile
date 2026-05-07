// pipeline {
//     agent any



//     stages {


//         stage('Setup Environment') {
//             steps {
//                 bat '''
//                 python -m venv venv
//                 call venv\\Scripts\\activate
//                 python -m pip install --upgrade pip
//                 pip install -r requirements.txt
//                 '''
//             }
//         }

//         stage('Run UI + API Tests (Parallel Execution)') {
//             steps {
//                 bat '''
//                 call venv\\Scripts\\activate
//                 pytest -n auto -v --html=reports/report.html --self-contained-html
//                 '''
//             }
//         }

//         stage('Generate Logs & Screenshots') {
//             steps {
//                 bat '''
//                 echo Tests completed. Checking reports...
//                 dir reports
//                 '''
//             }
//         }

//         stage('Publish HTML Report') {
//             steps {
//                 publishHTML (target: [
//                     allowMissing: false,
//                     alwaysLinkToLastBuild: true,
//                     keepAll: true,
//                     reportDir: 'reports',
//                     reportFiles: 'report.html',
//                     reportName: 'Automation Test Report'
//                 ])
//             }
//         }

//         stage('Archive Artifacts') {
//             steps {
//                 archiveArtifacts artifacts: '''
//                     reports/**,
//                     reports/screenshots/**,
//                     logs/**
//                 ''', allowEmptyArchive: true
//             }
//         }
//     }

//     post {
//         always {
//             echo 'Pipeline Execution Completed'
//         }

//         success {
//             echo 'Build Successful ✔'
//         }

//         failure {
//             echo 'Build Failed ❌ Check logs'
//         }
//     }
// }



pipeline {
    agent any

    stages {

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

        stage('Run UI + API Tests (Parallel Execution)') {
            steps {
                bat '''
                call venv\\Scripts\\activate
                pytest -n auto -v ^
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

        stage('Generate Logs & Screenshots') {
            steps {
                bat '''
                echo Tests completed. Checking reports...
                dir reports
                '''
            }
        }

        stage('Publish HTML Report') {
            steps {
                publishHTML (target: [
                    allowMissing: false,
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
                archiveArtifacts artifacts: '''
                    reports/**,
                    reports/screenshots/**,
                    logs/**,
                    reports/allure-results/**
                ''', allowEmptyArchive: true
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
            echo 'Build Failed ❌ Check logs'
        }
    }
}