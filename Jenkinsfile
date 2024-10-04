pipeline {
    agent any

    options {
        disableConcurrentBuilds()
    }

    parameters {
        string(name: "label_string", defaultValue: "REPO UPDATE", trim: true, description: "Sample string parameter")
    }

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
                sh "docker run --rm -e DISCORD_WEBHOOK_URL=$DISCORD_WEBHOOK_URL --name frontend-tests reservant-front-tests"
            }
        }
    }
}
