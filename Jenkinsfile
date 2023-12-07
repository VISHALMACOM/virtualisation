pipeline {
    agent any

    stages {
        stage('Transfer sonar_script.sh to SonarQube EC2') {
            steps {
                script {
                    sh 'scp ./sonar_script.sh ubuntu@34.227.200.69:/home/ubuntu/.'
                }
            }
        }

        stage('Run sonar_script.sh on SonarQube EC2') {
            steps {
                script {
                    sh 'ssh ubuntu@34.227.200.69 "sh /home/ubuntu/sonar_script.sh"'
                }
            }
        }

        stage('Start SonarQube on SonarQube EC2') {
            steps {
                script {
                    sh 'ssh ubuntu@34.227.200.69 "nohup ./sonarqube-9.9.0.65466/bin/linux-x86-64/sonar.sh console > /dev/null 2>&1 &"'
                }
            }
        }

        stage('Prepare Docker Environment on Docker EC2') {
            steps {
                script {
                    sh 'ssh ubuntu@44.221.36.95 "mkdir -p /home/ubuntu/database"'
                    sh 'scp -r ./database/* ubuntu@44.221.36.95:/home/ubuntu/database/.'
                    sh 'ssh ubuntu@44.221.36.95 "sleep 20; echo $?"'
                    sh 'ssh ubuntu@44.221.36.95 "docker-compose down 2>/dev/null; echo $?"'
                    sh 'ssh ubuntu@44.221.36.95 "docker system prune -af>/dev/null; echo $?"'
                    sh 'ssh ubuntu@44.221.36.95 "chmod a+x /home/ubuntu/database/Student/scripts/steps.sh"'
                    sh 'ssh ubuntu@44.221.36.95 "cd /home/ubuntu/database/. ; docker-compose up -d"'
                }
            }
        }
    }
}