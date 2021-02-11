pipeline {
    agent any
    options {
        datadog(collectLogs: true, tags: ["repo:small-tests", "script:test.py"])
    }
     environment {
        DD_GIT_DEFAULT_BRANCH = 'master'
    }
    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/cloudberry666/small-tests.git', branch: "master"
            }
    }
        stage('Run script') {
            steps {
                sh "python test.py"
            }
        }
    }
}
