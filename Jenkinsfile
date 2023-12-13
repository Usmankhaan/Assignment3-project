pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/Usmankhaan/Project', branch: 'main'
            }
        }
        stage('Build') {
            steps {
                echo 'Building..'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying..'
                sshPublisher(
                    publishers: [
                        sshPublisherDesc(
                            configName: 'jenkins-u',
                            transfers: [sshTransfer(sourceFiles: '*/', remoteDirectory: '/myapp')],
                
                        )
                    ]
                )
            }
        }
    }
}
