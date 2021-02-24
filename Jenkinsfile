pipeline {
  agent any
  stages {
    stage('http://asdf123.ddtdg.com') {
      steps {
        git(url: 'https://github.com/cloudberry666/small-tests.git', branch: 'master')
      }
    }

    stage('Install ddtrace') {
      steps {
        sh 'pip install ddtrace'
        git(url: 'https://github.com/cloudberry666/small-tests', credentialsId: 'SUPER_SECRET', poll: true)
      }
    }

    stage('Run script <test/>\'"') {
      steps {
        sh 'python test.py'
      }
    }

    stage('javascript:alert(\'://\')') {
      steps {
        echo 'hi there'
        datadog(collectLogs: true) {
          publishHTML(reportFiles: 'index.html', reportName: 'javascript:alert(%27://%27)', reportTitles: 'javascript:alert(%27://%27)', target: '[allowMissing: false, alwaysLinkToLastBuild: false, keepAll: false, reportDir: \'\', reportFiles: \'index.html\', reportName: \'javascript:alert(%27://%27)\', reportTitles: \'javascript:alert(%27://%27)\']')
        }

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