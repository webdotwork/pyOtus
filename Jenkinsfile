pipeline {
    agent any

    environment {
        PYTHON_ENV = '.venv'  // Specify your Python virtual environment directory
        ALLURE_RESULTS = 'allure-results'
        ALLURE_REPORT = 'allure-report'
    }

    stages {
        stage('Checkout Code') {
            steps {
                // Pull the source code from the master branch
                git branch: 'main', url: 'https://github.com/webdotwork/pyOtus.git'
            }
        }

        stage('Setup Environment') {
            steps {
                script {
                    // Clean up any existing environment
                    sh 'rm -rf $PYTHON_ENV'

                    // Create a new virtual environment
                    sh 'python3 -m venv $PYTHON_ENV'

                    // Install environment
                    sh './$PYTHON_ENV/bin/pip3 install -r requirements.txt'
                }
            }
        }


        stage('Run Tests with selenium') {
            steps {
                script {
                    // run tests with pytest and selenium
                    sh '''
                        ./$PYTHON_ENV/bin/pip3 install -r requirements.txt
                        ./$PYTHON_ENV/bin/pytest --browser=chrome --headless --url=http://10.0.47.57:8081/administration/ tests/test_add_new_goods.py --alluredir=allure-results
                        ./$PYTHON_ENV/bin/pytest --browser=chrome --headless --url=http://10.0.47.57:8081/administration/ tests/test_del_goods.py --alluredir=allure-results
                        ./$PYTHON_ENV/bin/pytest --browser=chrome --headless --url=http://10.0.47.57:8081 tests/test_curency_check.py --alluredir=allure-results
                        # ./$PYTHON_ENV/bin/pytest --browser=chrome --headless --url=http://10.0.47.57:8081 tests/test_add_new_user.py --alluredir=allure-results
                        # ./$PYTHON_ENV/bin/pytest --browser=chrome --headless --url=http://10.0.47.57:8081 tests/test_login.py --alluredir=allure-results

                    '''
                }
            }
        }

        // stage('Run API Tests') {
        //     steps {
        //         script {
        //             // run API tests with pytest
        //             sh '''

        //                 ./$PYTHON_ENV/bin/pytest --browser=chrome --headless --url=http://10.0.47.57:8081/administration/ tests/test_add_new_goods.py --alluredir=allure-results
        //                 ./$PYTHON_ENV/bin/pytest --browser=chrome --headless --url=http://10.0.47.57:8081/administration/ tests/test_del_goods.py --alluredir=allure-results
        //                 ./$PYTHON_ENV/bin/pytest --browser=chrome --headless --url=http://10.0.47.57:8081 tests/test_curency_check.py --alluredir=allure-results
        //                 ./$PYTHON_ENV/bin/pytest --browser=chrome --headless --url=http://10.0.47.57:8081 tests/test_add_new_user.py --alluredir=allure-results
        //                 ./$PYTHON_ENV/bin/pytest --browser=chrome --headless --url=http://10.0.47.57:8081 tests/test_login.py --alluredir=allure-results

        //             '''
        //         }
        //     }
        // }

        // stage('Generate Allure Report') {
        //     steps {
        //         script {
        //             // Generate the Allure report
        //             sh '''
        //                 source $PYTHON_ENV/bin/activate
        //                 allure generate $ALLURE_RESULTS -o $ALLURE_REPORT --clean
        //             '''
        //         }
        //     }
        // }

        stage('Archive Allure Report') {
            steps {
                // Archive the Allure report as a Jenkins artifact
                archiveArtifacts artifacts: "$ALLURE_RESULTS/**", allowEmptyArchive: true
            }
        }

        // stage('Publish Allure Report') {
        //     steps {
        //         // Publish the Allure report in Jenkins (requires Allure Jenkins plugin)
        //         allure([
        //             results: [[path: "$ALLURE_RESULTS"]]
        //         ])
        //     }
        // }
    }

    // post {
    //     always {
    //         // Clean up the workspace after the build
    //         cleanWs()
    //     }
    // }
}
