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
        INFO_LABEL = "${params.label_string}"
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
                sh "docker run --rm -e DISCORD_WEBHOOK_URL=$DISCORD_WEBHOOK_URL -e INFO_LABEL='$INFO_LABEL' --name frontend-tests reservant-front-tests"
            }
        }
    }
}
