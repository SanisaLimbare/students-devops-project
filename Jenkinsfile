
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    python3 -m venv .venv
                    .venv/bin/python -m pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '.venv/bin/python -m pytest -v'
            }
        }

        stage('Build Docker Image') {
             steps {
                 sh '/Users/sanisalimbare/.docker/bin/docker build -t student-devops-app .'
    }
}

        stage('Deploy Container') {
             steps {
                 sh '''
            /Users/sanisalimbare/.docker/bin/docker rm -f student-app || true
            /Users/sanisalimbare/.docker/bin/docker run -d --name student-app -p 5001:5001 student-devops-app
        '''
    }
}

        stage('Verify Deployment') {
            steps {
                sh '''
                    for i in 1 2 3 4 5 6 7 8 9 10; do
                        if curl -fsS http://127.0.0.1:5001/health; then
                            exit 0
                        fi
                        sleep 2
                    done
                    echo "Health check failed"
                    exit 1
                '''
            }
        }
    }

    post {
        success {
            echo 'CI/CD pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed. Check the console output.'
        }
    }
}
pipeline {
    agent any

    environment {
        PATH = "/Users/sanisalimbare/.docker/bin:/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin"
    }

    // Keep your existing stages and post section here
}