pipeline {
  agent any
  stages {
    stage('Checkout') {
      steps {
        git(url: 'https://github.com/cloudberry666/small-tests.git', branch: 'master')
      }
    }

    stage('Install ddtrace') {
      steps {
        sh 'pip install ddtrace'
      }
    }

    stage('Run script') {
      steps {
        sh 'python test.py'
      }
    }

  }
  environment {
    DD_GIT_DEFAULT_BRANCH = 'master'
  }
  options {
    datadog(collectLogs: true, tags: ["repo:small-tests", "script:test.py"])
  }
}