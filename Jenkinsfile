pipeline {
  agent any
  stages {
    stage('asdf123.ddtdg.com') {
      steps {
        git(url: 'https://github.com/cloudberry666/small-tests.git', branch: 'master')
      }
    }

    stage('Install ddtrace') {
      steps {
        sh 'pip install ddtrace'
      }
    }

    stage('Run script <test/>\'"') {
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