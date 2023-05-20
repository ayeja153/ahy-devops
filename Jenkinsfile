pipeline {
   agent any
    
    stages {
        
    stage('Prepare') {
      steps {
          sh 'docker pull ayeja153/flask-app:v1 && docker stop flask-app 2>/dev/null || true && docker rm -f flask-app 2>/dev/null || true'
      }
    }
    
    stage('Deploy') {
      steps {
        // Deploy the Docker container to a server
          sh 'docker run -d --name flask-app -p 8081:8080 ayeja153/flask-app:v1'
       }
    }
  }
}
