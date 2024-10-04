pipeline {
    agent any

    environment {
        DISCORD_WEBHOOK_URL = credentials('jenkins-front-tests-discord-webhook')
    }

    stages {
        stage('Build') {
            when {
                branch 'main'
            }
            steps {
                sh "docker build -t reservant-front-tests:latest ."
            }
        }

        stage('Deploy') {
            when {
                branch 'main'
            }
            steps {
                sh "docker stop frontend-tests && docker rm frontend-tests || true"
                sh "docker run --rm -e DISCORD_WEBHOOK_URL=$DISCORD_WEBHOOK_URL --name frontend-tests reservant-front-tests"
            }
        }
    }
}
