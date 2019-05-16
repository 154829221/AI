pipeline {
    environment {
        def CC='clang'
    }
    agent any
    options {
        buildDiscarder(logRotator(numToKeepStr: '1')) 
        disableConcurrentBuilds()
        skipDefaultCheckout()
        skipStagesAfterUnstable()
        timeout(time: 1, unit: 'HOURS')
        retry(3)
    }
    stages {
        stage('first'){
            steps {
            echo 'first'
            echo "${CC}"
            }
            options { 
                retry(3)
                timeout(time: 1, unit: 'MINUTES')
            }
        }
        stage('second'){
            steps {
            echo 'second'
            }
            options { 
                retry(3)
                timeout(time: 10, unit: 'SECONDS')
            }
        }
        stage('third'){
            steps {
                echo 'third'
                script {
                    def browsers = ['chrome', 'firefox']
                    for (int i = 0; i < browsers.size(); ++i) {
                        echo "Testing the ${browsers[i]} browser"
                    }
                }
            }
            options { 
                retry(3)
                timeout(time: 10, unit: 'SECONDS')
            }
        }
        stage('forth'){
            steps {
            echo 'forth'
            echo "${params.DEPLOY_ENV} ${params.DEBUG_BUILD}"
            }
        }
        stage('Final Build') {
            environment { 
                AN_ACCESS_KEY = credentials('245fcd13-b071-4c6f-9a81-42f15e84a74f') 
            }
            steps {
                sh 'echo "Start Final Build"'
                sh '''
                    echo "Start ls dir"
                    ls -lah
                    echo "Look at the keys"
                '''
                echo "echo ${AN_ACCESS_KEY}"
            }
        }
    }
    post {
        always {
            echo 'This will always run'
        }
        success {
            echo 'This will run only if successful'
        }
        failure {
            mail to: 'dengyunfei@gitv.cn',
            subject: "Failed Pipeline: ${currentBuild.fullDisplayName}",
            body: "Something is wrong with ${env.BUILD_URL}"
        }
        unstable {
            echo 'This will run only if the run was marked as unstable'
        }
        changed {
            echo 'This will run only if the state of the Pipeline has changed'
            echo 'For example, if the Pipeline was previously failing but is now successful'
        }
    }
}
